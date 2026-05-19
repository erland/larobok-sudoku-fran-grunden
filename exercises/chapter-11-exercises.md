# Övningar till kapitel 11: Fullständiga lösningar steg för steg

## Facit och stöd

### Övning 1: Välj nästa strategi

Rätt svar: **2. Leta efter dolda singlar i rader, kolumner och boxar.**

Motivering: Om enkla singlar saknas är dolda singlar en naturlig nästa strategi. Gissning ska undvikas, och Swordfish är för avancerat att prova innan enklare strategier är kontrollerade.

### Övning 2: Skriv en lösningslogg

Ett möjligt svar:

| Steg | Åtgärd | Motivering |
|---|---|---|
| 1 | Lista saknade siffror: 2, 6, 7, 9 | Man måste veta vad raden behöver. |
| 2 | Kontrollera varje tom ruta mot sin kolumn | Kolumnen kan utesluta vissa siffror. |
| 3 | Kontrollera varje tom ruta mot sin box | Boxen kan utesluta fler siffror. |
| 4 | Leta efter enkel singel | Om en ruta bara har en kandidat kan den fyllas i. |
| 5 | Leta efter dold singel | Om en siffra bara kan stå i en ruta i raden är den säker. |

### Övning 3: Hitta den svaga länken

Resonemanget saknar en logisk motivering. Att en siffra “ser ut att passa” betyder bara att den kanske är möjlig. För att placeringen ska vara säker måste lösaren visa att 7 inte kan stå någon annanstans i rätt grupp, eller att rutan inte kan innehålla någon annan siffra.

### Övning 4: Bygg en kontrollpunkt

Ett möjligt svar:

- Har jag brutit mot någon rad, kolumn eller box?
- Har jag uppdaterat kandidater efter de senaste placeringarna?
- Kan varje placering förklaras med en tydlig strategi?
- Har jag markerat något som säker placering fast det bara är en möjlighet?

## Extra träningsuppgift

Välj ett sudoku på lätt nivå. Lös bara tills du har gjort tio säkra steg. Skriv varje steg med följande mall:

| Steg | Vad jag gjorde | Varför det var säkert |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

När du är klar: markera vilka steg som var enkla singlar, dolda singlar eller kandidatrensningar.
