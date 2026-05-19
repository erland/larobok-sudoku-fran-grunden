#!/usr/bin/env python3
"""
Genererar SVG-bilder av sudoku-bräden från examples/boards/boards.json.

Kör från projektroten:
    python code/generate_boards.py

Utdata:
    assets/boards/BOARD-XX-YY.svg

Datamodell:
- grid: 9 strängar med siffror och 0 eller . för tom ruta
- highlights: markering av cell, row, col eller box
- notes: små kandidat-/förklaringsmarkeringar per cell, t.ex. {"r1c3": "2,7"}
"""
from __future__ import annotations

import json
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "examples" / "boards" / "boards.json"
OUTPUT = ROOT / "assets" / "boards"

PALETTE = {
    "blue": "#d8ecff",
    "gold": "#fff1b8",
    "red": "#ffe0e0",
    "green": "#e0f4dc",
    "grey": "#eeeeee",
    "purple": "#eadfff",
}

def parse_grid(grid: list[str]) -> list[list[str]]:
    if len(grid) != 9:
        raise ValueError("grid måste innehålla exakt 9 rader")
    parsed = []
    for row in grid:
        row = row.replace(".", "0")
        if len(row) != 9:
            raise ValueError("varje grid-rad måste innehålla exakt 9 tecken")
        parsed.append(["" if ch in ("0", ".") else ch for ch in row])
    return parsed

def parse_cell_key(key: str) -> tuple[int, int]:
    key = key.lower().replace(" ", "")
    if not (key.startswith("r") and "c" in key):
        raise ValueError(f"ogiltig cellnyckel: {key}")
    r_txt, c_txt = key[1:].split("c", 1)
    return int(r_txt), int(c_txt)

def highlighted_cells(highlights: list[dict]) -> dict[tuple[int, int], str]:
    cells: dict[tuple[int, int], str] = {}
    for item in highlights or []:
        color = PALETTE.get(item.get("color", "gold"), item.get("color", "#fff1b8"))
        typ = item.get("type")
        if typ == "cell":
            r = int(item["row"])
            c = int(item["col"])
            cells[(r, c)] = color
        elif typ == "row":
            r = int(item["index"])
            for c in range(1, 10):
                cells[(r, c)] = color
        elif typ == "col":
            c = int(item["index"])
            for r in range(1, 10):
                cells[(r, c)] = color
        elif typ == "box":
            b = int(item["index"]) - 1
            r0 = (b // 3) * 3 + 1
            c0 = (b % 3) * 3 + 1
            for r in range(r0, r0 + 3):
                for c in range(c0, c0 + 3):
                    cells[(r, c)] = color
    return cells

def note_map(notes: dict | None) -> dict[tuple[int, int], str]:
    mapped: dict[tuple[int, int], str] = {}
    for key, value in (notes or {}).items():
        mapped[parse_cell_key(key)] = str(value)
    return mapped

def render_note(parts: list[str], text: str, x: float, y: float, cell: int) -> None:
    clean = escape(text)
    if len(clean) <= 3:
        size = 18
    elif len(clean) <= 5:
        size = 14
    else:
        size = 11
    color = "#7a2e2e" if clean.lower() in {"x", "nej"} else "#1f4e79"
    parts.append(
        f'<text x="{x + cell/2}" y="{y + cell/2 + size/3}" text-anchor="middle" '
        f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="700" fill="{color}">{clean}</text>'
    )

def render_svg(board: dict) -> str:
    grid = parse_grid(board["grid"])
    marks = highlighted_cells(board.get("highlights", []))
    notes = note_map(board.get("notes"))

    cell = int(board.get("cell_size", 52))
    margin = 24
    label_h = 34
    foot_h = 24 if board.get("caption") else 0
    size = cell * 9
    width = size + margin * 2
    height = size + margin * 2 + label_h + foot_h

    title = board.get("title", board["id"])
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{width/2}" y="22" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="700" fill="#222">{escape(title)}</text>',
    ]

    x0 = margin
    y0 = margin + label_h

    for r in range(1, 10):
        for c in range(1, 10):
            x = x0 + (c - 1) * cell
            y = y0 + (r - 1) * cell
            fill = marks.get((r, c), "#ffffff")
            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{fill}"/>')

    for i in range(10):
        stroke_w = 3 if i % 3 == 0 else 1
        x = x0 + i * cell
        y = y0 + i * cell
        parts.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0 + size}" stroke="#222" stroke-width="{stroke_w}"/>')
        parts.append(f'<line x1="{x0}" y1="{y}" x2="{x0 + size}" y2="{y}" stroke="#222" stroke-width="{stroke_w}"/>')

    for r in range(1, 10):
        for c in range(1, 10):
            x = x0 + (c - 1) * cell
            y = y0 + (r - 1) * cell
            val = grid[r-1][c-1]
            if val:
                parts.append(
                    f'<text x="{x + cell/2}" y="{y + cell/2 + 12}" text-anchor="middle" '
                    f'font-family="Arial, Helvetica, sans-serif" font-size="32" font-weight="700" fill="#111">{escape(val)}</text>'
                )
            elif (r, c) in notes:
                render_note(parts, notes[(r, c)], x, y, cell)

    if board.get("caption"):
        parts.append(
            f'<text x="{width/2}" y="{height-8}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" '
            f'font-size="12" fill="#444">{escape(board["caption"])}</text>'
        )

    parts.append("</svg>")
    return "\n".join(parts)

def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    boards = json.loads(SOURCE.read_text(encoding="utf-8"))
    for board in boards:
        svg = render_svg(board)
        (OUTPUT / f'{board["id"]}.svg').write_text(svg, encoding="utf-8")
        print(f'Skapade {OUTPUT / (board["id"] + ".svg")}')

if __name__ == "__main__":
    main()
