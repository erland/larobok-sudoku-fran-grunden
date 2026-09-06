#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

import yaml

PANDOC_VERSION = "3.1.11.1"


def run(command: list[str], cwd: Path) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def pandoc_version() -> str:
    result = subprocess.run(["pandoc", "--version"], text=True, capture_output=True, check=True)
    match = re.search(r"pandoc\s+([^\s]+)", result.stdout.splitlines()[0])
    return match.group(1) if match else "unknown"


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
        "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def first_h1(text: str) -> str | None:
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            match = re.match(r"^#\s+(.+?)\s*$", line)
            if match:
                return match.group(1)
    return None


def validate(root: Path, metadata: dict) -> list[Path]:
    required = ["title", "author", "language", "project_slug", "cover_image", "chapters"]
    missing = [key for key in required if not metadata.get(key)]
    if missing:
        raise SystemExit("Metadata saknar obligatoriska fält: " + ", ".join(missing))
    if metadata["language"] not in {"sv", "en"}:
        raise SystemExit("language måste vara sv eller en")

    cover = root / metadata["cover_image"]
    if not cover.exists():
        raise SystemExit(f"Omslagsbild saknas: {metadata['cover_image']}")

    chapter_names = metadata.get("chapters") or []
    if not chapter_names or chapter_names[0] != "chapters/00-inledning.md":
        raise SystemExit("Kapitelordningen måste börja med chapters/00-inledning.md")

    chapters: list[Path] = []
    errors: list[str] = []
    for index, rel in enumerate(chapter_names):
        path = root / rel
        if not path.exists():
            errors.append(f"Saknar kapitel: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if text.count("```") % 2:
            errors.append(f"{rel}: ojämnt antal kodblocksmarkörer")

        heading = first_h1(text)
        if heading is None:
            errors.append(f"{rel}: saknar H1-rubrik")
        elif index == 0:
            if not heading.startswith("Inledning"):
                errors.append(f"{rel}: första H1 måste börja med 'Inledning'")
        elif not re.match(r"^Kapitel\s+\d+\s*:\s*.+$", heading):
            errors.append(f"{rel}: första H1 måste följa 'Kapitel N: Titel'")

        chapters.append(path)

    if errors:
        raise SystemExit("Valideringen stoppade publiceringen:\n- " + "\n- ".join(errors))
    return chapters


def postprocess_epub(epub: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="sudoku-fran-grunden-epub-") as tmp_name:
        tmp = Path(tmp_name)
        with zipfile.ZipFile(epub, "r") as archive:
            archive.extractall(tmp)
        opf_files = list(tmp.glob("**/*.opf"))
        if not opf_files:
            return
        opf = opf_files[0]
        text = opf.read_text(encoding="utf-8")
        text = re.sub(
            r'(<itemref\b[^>]*idref="nav"[^>]*)(/?>)',
            lambda m: m.group(1) + ("" if 'linear=' in m.group(1) else ' linear="no"') + m.group(2),
            text,
        )
        opf.write_text(text, encoding="utf-8")

        rebuilt = epub.with_suffix(".tmp.epub")
        with zipfile.ZipFile(rebuilt, "w") as archive:
            mimetype = tmp / "mimetype"
            if mimetype.exists():
                archive.write(mimetype, "mimetype", compress_type=zipfile.ZIP_STORED)
            for path in sorted(tmp.rglob("*")):
                if path.is_file() and path != mimetype:
                    archive.write(path, path.relative_to(tmp).as_posix(), compress_type=zipfile.ZIP_DEFLATED)
        rebuilt.replace(epub)


def prepare_pdf_chapters(chapters: list[Path], tmp: Path) -> list[Path]:
    """Create temporary Markdown chapters where local SVG images are converted to PDF."""
    chapter_dir = tmp / "chapters"
    media_dir = tmp / "svg-pdf"
    chapter_dir.mkdir(parents=True, exist_ok=True)
    media_dir.mkdir(parents=True, exist_ok=True)

    svg_pattern = re.compile(r'(!\[[^\]]*\]\()([^\s)]+\.svg)([^)]*\))', re.IGNORECASE)
    converted: dict[Path, Path] = {}
    prepared: list[Path] = []

    for chapter_index, chapter in enumerate(chapters):
        text = chapter.read_text(encoding="utf-8")

        def replace_svg(match: re.Match[str]) -> str:
            target = match.group(2)
            if target.startswith(("http://", "https://")):
                return match.group(0)
            source = (chapter.parent / target).resolve()
            if not source.exists():
                return match.group(0)
            if shutil.which("rsvg-convert") is None:
                raise SystemExit("rsvg-convert krävs för SVG-bilder i PDF-bygget")
            if source not in converted:
                output = media_dir / f"{len(converted) + 1:04d}-{source.stem}.pdf"
                run(["rsvg-convert", "-f", "pdf", "-o", str(output), str(source)], chapter.parent)
                converted[source] = output
            return match.group(1) + converted[source].as_posix() + match.group(3)

        text = svg_pattern.sub(replace_svg, text)
        out = chapter_dir / f"{chapter_index:02d}-{chapter.name}"
        out.write_text(text, encoding="utf-8")
        prepared.append(out)

    return prepared


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", default="dist")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    metadata_path = root / "docs" / "export-metadata.yaml"
    metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
    chapters = validate(root, metadata)
    print(f"OK: validerade {metadata['title']} ({len(chapters)} kapitel)")
    if args.validate_only:
        return 0

    if shutil.which("pandoc") is None:
        raise SystemExit("Pandoc saknas")
    version = pandoc_version()
    if version != PANDOC_VERSION:
        raise SystemExit(f"Pandoc {PANDOC_VERSION} krävs; hittade {version}")

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    slug = metadata["project_slug"]
    resource_path = f"{root}:{root / 'chapters'}"
    chapter_filter = root / "publishing" / "chapter-headings.lua"

    epub = output_dir / f"{slug}.epub"
    run([
        "pandoc", *map(str, chapters),
        "--from=markdown", "--to=epub3",
        "--output", str(epub),
        "--metadata-file", str(metadata_path),
        "--resource-path", resource_path,
        "--lua-filter", str(chapter_filter),
        "--toc", "--toc-depth=1",
        "--css", str(root / "publishing" / "epub.css"),
        "--epub-cover-image", str(root / metadata["cover_image"]),
    ], root)
    postprocess_epub(epub)

    if shutil.which("xelatex") is None:
        raise SystemExit("xelatex krävs för PDF-bygget")

    pdf = output_dir / f"{slug}.pdf"
    with tempfile.TemporaryDirectory(prefix="sudoku-fran-grunden-pdf-") as tmp_name:
        tmp = Path(tmp_name)
        front = tmp / "frontmatter.tex"
        tex = tmp / "book.tex"
        pdf_chapters = prepare_pdf_chapters(chapters, tmp)
        title = latex_escape(str(metadata.get("title", "")))
        subtitle = latex_escape(str(metadata.get("subtitle", "")))
        author = latex_escape(str(metadata.get("author", "")))
        cover = (root / metadata["cover_image"]).as_posix()
        front.write_text(
            "\\pagenumbering{gobble}\n"
            "\\thispagestyle{empty}\n"
            f"\\AddToShipoutPictureBG*{{\\AtPageLowerLeft{{\\includegraphics[width=\\paperwidth,height=\\paperheight]{{{cover}}}}}}}\n"
            "\\null\\clearpage\n"
            "\\thispagestyle{empty}\n"
            "\\vspace*{0.22\\textheight}\n"
            "\\begin{center}\n"
            f"{{\\Huge\\bfseries {title}}}\\par\n"
            f"\\vspace{{1em}}{{\\Large {subtitle}}}\\par\n"
            "\\vfill\n"
            f"{{\\Large {author}}}\\par\n"
            "\\end{center}\\clearpage\n"
            "\\pagenumbering{roman}\n"
            "\\phantomsection\n"
            "\\pdfbookmark[1]{Innehåll}{toc}\n"
            "\\tableofcontents\n"
            "\\clearpage\n",
            encoding="utf-8",
        )

        run([
            "pandoc", *map(str, pdf_chapters),
            "--from=markdown+raw_tex+pipe_tables", "--to=latex", "--standalone",
            "--output", str(tex),
            "--resource-path", f"{root}:{tmp}:{root / 'chapters'}",
            "--lua-filter", str(chapter_filter),
            "--include-in-header", str(root / "publishing" / "pdf-header.tex"),
            "--include-before-body", str(front),
            "--metadata", "title=",
        ], root)

        xelatex = [
            "xelatex", "-interaction=nonstopmode", "-halt-on-error",
            f"-output-directory={tmp}", f"-jobname={slug}", str(tex),
        ]
        for _ in range(3):
            run(xelatex, root)

        built_pdf = tmp / f"{slug}.pdf"
        if not built_pdf.exists():
            raise SystemExit("PDF-bygget skapade ingen utfil")
        shutil.copy2(built_pdf, pdf)

    print(f"OK: {epub}")
    print(f"OK: {pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
