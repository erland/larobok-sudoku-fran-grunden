# Sudoku från grunden – projekt

Detta är bokprojektet för **Sudoku från grunden** av Erland Lindmark.

## Struktur
- `docs/` – bokspecifikation, kapitelplan, canon, terminologi, status och exportmetadata.
- `chapters/` – inledning och bokkapitel.
- `exercises/` – separata övningsfiler.
- `examples/` – exempelrutnät och scenarier.
- `code/` – ej använt i denna bok.
- `assets/` – omslag, bilder, bildpromptar och eventuella stilresurser.
- `exports/` – framtida EPUB/PDF/DOCX/Markdown-exporter.

## Aktuell fas
Projektet är under kapitelgenerering. Kapitel 1–10 finns som utkast.

## Senaste ändring

Kapitel 10, övningar till kapitel 10 samt projektstatus, canon, terminologi och exportmetadata har lagts till/uppdaterats.


## Senaste uppdatering
Kapitel 13: Nästa steg har lagts till tillsammans med övningar och uppdaterad metadata.


## Strukturerade sudoku-bräden

Sudokubrädor lagras i `examples/boards/boards.json` och genereras med `python code/generate_boards.py` till `assets/boards/*.svg`.
