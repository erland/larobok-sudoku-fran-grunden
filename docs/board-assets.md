# Sudoku-bräden som strukturerade SVG-assets

Projektet lagrar sudokubrädor och kandidatdiagram i strukturerad form i:

- `examples/boards/boards.json`

SVG-filer genereras med:

```bash
python code/generate_boards.py
```

Utdata skrivs till:

- `assets/boards/BOARD-XX-YY.svg`

## Uppdatering

Alla pedagogiska sudokubrädor som tidigare låg som markdown-tabeller i kapitlen har flyttats till SVG-logiken där det är relevant. Kapiteltexten refererar nu till genererade SVG-filer med relativa bildlänkar.

Text som förklarade att punkttecken betyder tomma rutor har rensats bort där den hörde ihop med tabellbräden, eftersom tomma rutor visas visuellt i SVG-bilderna.

## Antal definierade bräden

45 bräden finns definierade i `examples/boards/boards.json`.

## Schema i korthet

Varje bräde kan innehålla:

- `id`: stabilt ID, exempel `BOARD-06-01`
- `title`: titel som visas i SVG
- `grid`: 9 strängar med siffror, där `0` eller `.` betyder tom ruta i datan
- `highlights`: markerade rader, kolumner, boxar eller celler
- `notes`: kandidatlistor eller pedagogiska markeringar i enskilda celler
- `caption`: kort beskrivning

