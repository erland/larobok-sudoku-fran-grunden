# Terminologi

| Begrepp | Första kapitel | Definition |
|---|---:|---|
| Ruta | 1 | En enskild cell i sudoku-rutnätet. |
| Rad | 1 | En vågrät linje med nio rutor. |
| Kolumn | 1 | En lodrät linje med nio rutor. |
| Box | 1 | Ett 3×3-område med nio rutor. |
| Rutnät | 1 | Hela sudokuplanen med 81 rutor. |
| Eliminering | 2 | Att ta bort omöjliga siffror eller placeringar genom sudoku-reglerna. |
| Säker placering | 2 | En siffra som logiskt bara kan stå på en viss plats. |
| Möjlig placering | 2 | En ruta där en siffra kan passa, men där placeringen ännu inte är säker. |
| Kandidat | 3 | En möjlig siffra som kan passa i en tom ruta. |
| Kandidatlista | 3 | En samlad lista över möjliga siffror för en ruta. |
| Anteckning | 3 | En markering av möjliga siffror som stöd för fortsatt logiskt tänkande. |
| Scanning | 4 | Att metodiskt söka efter var en vald siffra kan placeras genom att utesluta rutor. |
| Enkel singel | 4 | En ruta som bara har en kandidat kvar. |
| Dold singel | 4 | En siffra som bara kan stå på en plats i en rad, kolumn eller box. |
| Grupp | 4 | En rad, kolumn eller box som ska innehålla siffrorna 1–9 exakt en gång. |
| Lösningsrunda | 5 | Ett planerat varv genom rutnätet där lösaren söker efter vissa mönster i en bestämd ordning. |
| Kontrollpunkt | 5 | En kort paus för att kontrollera att regler, placeringar och kandidater fortfarande stämmer. |
| Arbetsrutin | 5 | En återkommande arbetsordning som hjälper lösaren att gå från scanning till placering, uppdatering och kontroll. |
| Naket par | 6 | Två rutor i samma grupp som har exakt samma två kandidater och inga andra kandidater. |
| Dolt par | 6 | Två siffror som bara kan stå i samma två rutor i en grupp, även om rutorna har fler kandidater antecknade. |
| Låsta kandidater | 6 | En situation där en kandidat är begränsad till en viss rad, kolumn eller box och därför kan tas bort på andra platser. |
| Rad-box-interaktion | 7 | Ett mönster där alla möjliga platser för en kandidat i en box ligger på samma rad, vilket gör att kandidaten kan rensas från resten av raden utanför boxen. |
| Kolumn-box-interaktion | 7 | Ett mönster där alla möjliga platser för en kandidat i en box ligger i samma kolumn, vilket gör att kandidaten kan rensas från resten av kolumnen utanför boxen. |
| Felsökningsrutin | 8 | En ordnad serie kontroller som används när lösningen känns fast. |
| Perspektivbyte | 8 | Att växla mellan att undersöka enskilda rutor och att följa en viss siffra genom grupper. |
| Stoppregel | 8 | En regel som säger att en siffra inte ska placeras förrän den kan motiveras logiskt. |
| Riskfras | 9 | En formulering som visar att lösaren kanske håller på att gissa i stället för att dra en säker slutsats. |
| Falsk singel | 9 | En ruta som ser ut att ha en enda kandidat kvar därför att en annan kandidat har rensats bort felaktigt. |
| Logisk motivering | 9 | En kort förklaring av vilken regel eller strategi som gör en placering eller rensning säker. |
| X-Wing | 10 | Ett mönster där en kandidat är begränsad till samma två kolumner i två rader, eller samma två rader i två kolumner, vilket gör att kandidaten kan rensas från andra rutor i de berörda linjerna. |
| Swordfish | 10 | Ett större kandidat-mönster där tre rader och tre kolumner låser en viss kandidat. |
| Kedja | 10 | Ett logiskt resonemang där varje steg följer av ett tidigare kandidatval eller en tidigare uteslutning. |

| Lösningsflöde | 11 | Den ordning lösaren använder för att lösa rutnätet steg för steg, inklusive scanning, placering, kandidatuppdatering och kontrollpunkter. |
| Strategiurval | 11 | Beslutet om vilken strategi som är mest rimlig att prova härnäst utifrån vad rutnätet visar. |
| Ledtrådsnivå | 12 | Hur mycket hjälp en uppgift ger innan facit. |
| Övningslogg | 12 | En kort anteckning där läsaren skriver vilken strategi som användes och varför steget är säkert. |

| Träningsplan | En enkel plan för fortsatt övning efter boken. | 13 |
| Personlig checklista | En egen arbetsordning för att lösa sudoku mer systematiskt. | 13 |
| Sudokuvariant | En sudokuform som bygger på grundreglerna men lägger till eller ändrar begränsningar. | 13 |
