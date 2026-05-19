# Övningar till kapitel 7: Mönster i rader och kolumner

## Syfte

De här övningarna tränar dig i att känna igen rad-box-interaktion och kolumn-box-interaktion. Målet är inte att lösa hela sudoku, utan att se när kandidater kan rensas på ett säkert sätt.

## Övning A: Rad-box-interaktion

Titta bara på kandidaten 5 i den här boxen.

| Rad/kolumn | C1 | C2 | C3 |
|---|---:|---:|---:|
| R1 | x | x | x |
| R2 | 5 | 5 | . |
| R3 | x | x | x |

Svara:

1. Är kandidaten 5 låst till en rad?
2. Vilken rad?
3. Får du ta bort 5 från andra rutor på samma rad utanför boxen?

## Övning B: Kolumn-box-interaktion

Titta bara på kandidaten 9.

| Rad/kolumn | C7 | C8 | C9 |
|---|---:|---:|---:|
| R1 | x | 9 | x |
| R2 | x | 9 | x |
| R3 | x | . | x |

Svara:

1. Är kandidaten 9 låst till en kolumn?
2. Vilken kolumn?
3. Får du ta bort 9 från andra rutor i samma kolumn utanför boxen?

## Övning C: Får du rensa?

Fyll i “ja” eller “nej”.

| Fall | Möjliga platser för kandidaten i boxen | Rensning möjlig? | Varför? |
|---|---|---|---|
| 1 | R4C1 och R4C2 | | |
| 2 | R4C1 och R5C1 | | |
| 3 | R4C1 och R5C2 | | |
| 4 | R6C1, R6C2 och R6C3 | | |
| 5 | R4C2, R5C2 och R6C2 | | |

## Övning D: Vad händer efter rensningen?

En rad-box-interaktion gör att du får ta bort kandidaten 6 från tre rutor utanför boxen.

| Ruta | Kandidater före | Kandidater efter |
|---|---|---|
| R2C4 | 1, 6 | |
| R2C6 | 3, 6, 8 | |
| R2C8 | 6, 9 | |

Fyll i kandidaterna efter rensningen. Markera sedan om någon ruta blev en enkel singel.

## Övning E: Förklara med egna ord

Skriv två meningar:

1. En mening som förklarar rad-box-interaktion.
2. En mening som förklarar varför du inte får placera siffran direkt om det fortfarande finns två möjliga rutor.

## Facit

### Facit A

1. Ja.
2. Rad 2.
3. Ja, kandidaten 5 kan tas bort från andra rutor på rad 2 utanför den aktuella boxen.

### Facit B

1. Ja.
2. Kolumn 8.
3. Ja, kandidaten 9 kan tas bort från andra rutor i kolumn 8 utanför den aktuella boxen.

### Facit C

| Fall | Rensning möjlig? | Varför? |
|---|---|---|
| 1 | Ja | Båda platserna ligger på samma rad. |
| 2 | Ja | Båda platserna ligger i samma kolumn. |
| 3 | Nej | Platserna ligger varken på samma rad eller i samma kolumn. |
| 4 | Ja | Alla platser ligger på samma rad. |
| 5 | Ja | Alla platser ligger i samma kolumn. |

### Facit D

| Ruta | Kandidater före | Kandidater efter | Kommentar |
|---|---|---|---|
| R2C4 | 1, 6 | 1 | Enkel singel. |
| R2C6 | 3, 6, 8 | 3, 8 | Ingen singel ännu. |
| R2C8 | 6, 9 | 9 | Enkel singel. |

### Facit E

Exempel på godkända svar:

1. Rad-box-interaktion betyder att en kandidat i en box bara kan ligga på en viss rad, vilket gör att samma kandidat kan rensas från resten av raden utanför boxen.
2. Man får inte placera siffran direkt om det fortfarande finns två möjliga rutor, eftersom man ännu inte vet vilken av rutorna som är rätt.
