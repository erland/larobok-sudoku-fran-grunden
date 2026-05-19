# Projektstatus

## Bok
Titel: Sudoku från grunden  
Språk: Svenska  
Författare: Erland Lindmark  
Version: 0.13

## Nuvarande fas
- Kapitelgenerering

## Kapitelstatus

| Kapitel | Titel | Status | Kommentar |
|---|---|---|---|
| 0 | Inledning | Utkast | Skapad i startprojektet. |
| 1 | Sudokuns regler och uppbyggnad | Utkast | Första kapitelutkast skapat. |
| 2 | Börja med enkla siffror | Utkast | Skapat med övningar, exempel och facit. |
| 3 | Anteckningar och kandidater | Utkast | Skapat med kandidatlistor, anteckningsmetod och övningar. |
| 4 | Vanliga nybörjarstrategier | Utkast | Skapat med scanning, enkel singel, dold singel och övningar. |
| 5 | Arbeta systematiskt | Utkast | Skapat med lösningsrundor, kontrollpunkter och arbetsrutin. |
| 6 | Par och låsta möjligheter | Utkast | Skapat med naket par, dolt par, låsta kandidater och övningar. |
| 7 | Mönster i rader och kolumner | Utkast | Skapat med rad-box-interaktion, kolumn-box-interaktion och övningar. |
| 8 | När man kör fast | Utkast | Skapat med felsökningsrutin, perspektivbyte, stoppregel och övningar. |
| 9 | Vanliga misstag | Utkast | Skapat med vanliga fallgropar, kontrollfrågor, riskfraser och övningar. |
| 10 | Avancerade strategier på ett lugnt sätt | Utkast | Skapat med X-Wing, Swordfish, kedjor och övningar på igenkänningsnivå. |
| 11 | Fullständiga lösningar steg för steg | Utkast | Skapat med lösningsflöde, strategiurval, komplett exempel och övningar. |
| 12 | Träningskapitel | Utkast | Skapat med övningsblock, ledtrådar, facit och arbetsblad. |
| 13 | Nästa steg | Utkast | Skapat med träningsplan, nivåval, ledtrådsmetod och fortsatta sudokuvarianter. |

## Introducerade begrepp

| Begrepp | Kapitel | Kort definition |
|---|---|---|
| Ruta | 1 | En enskild cell i sudoku-rutnätet. |
| Rad | 1 | En vågrät linje med nio rutor. |
| Kolumn | 1 | En lodrät linje med nio rutor. |
| Box | 1 | Ett 3×3-område med nio rutor. |
| Rutnät | 1 | Hela sudokuplanen med 81 rutor. |
| Eliminering | 2 | Att utesluta omöjliga placeringar med hjälp av reglerna. |
| Säker placering | 2 | En siffra som logiskt måste stå på en viss plats. |
| Möjlig placering | 2 | En placering som kan fungera men ännu inte är bevisad. |
| Kandidat | 3 | En möjlig siffra som kan passa i en tom ruta. |
| Kandidatlista | 3 | En samlad lista över möjliga siffror för en ruta. |
| Anteckning | 3 | En liten markering av kandidater som stöd för fortsatt logiskt tänkande. |
| Scanning | 4 | Att metodiskt söka efter var en vald siffra kan placeras. |
| Enkel singel | 4 | En ruta som bara har en kandidat kvar. |
| Dold singel | 4 | En siffra som bara kan stå på en plats i en rad, kolumn eller box. |
| Grupp | 4 | En rad, kolumn eller box. |
| Lösningsrunda | 5 | Ett planerat varv genom rutnätet där läsaren letar efter vissa saker i bestämd ordning. |
| Kontrollpunkt | 5 | En kort paus där lösaren kontrollerar att placeringar, kandidater och regler fortfarande stämmer. |
| Arbetsrutin | 5 | En återkommande ordning för hur man scannar, placerar, uppdaterar och kontrollerar. |

| Naket par | 6 | Två rutor i samma grupp med exakt samma två kandidater. |
| Dolt par | 6 | Två siffror som bara kan stå i samma två rutor i en grupp. |
| Låsta kandidater | 6 | Kandidater som är begränsade till en viss rad, kolumn eller box och därför kan rensa andra platser. |
| Rad-box-interaktion | 7 | När alla möjliga platser för en kandidat i en box ligger på samma rad. |
| Kolumn-box-interaktion | 7 | När alla möjliga platser för en kandidat i en box ligger i samma kolumn. |

| Felsökningsrutin | 8 | En ordnad serie kontroller som används när lösningen känns fast. |
| Perspektivbyte | 8 | Att växla mellan att undersöka enskilda rutor och att följa en viss siffra genom grupper. |
| Stoppregel | 8 | En regel som säger att en siffra inte ska placeras förrän den kan motiveras logiskt. |

| Riskfras | 9 | En formulering som visar att lösaren kanske håller på att gissa. |
| Falsk singel | 9 | En ruta som ser ut som en singel på grund av felaktigt borttagen kandidat. |
| Logisk motivering | 9 | En kort förklaring av varför en placering eller rensning är säker. |

| X-Wing | 10 | Ett mönster där en kandidat är begränsad till samma två kolumner i två rader, eller samma två rader i två kolumner. |
| Swordfish | 10 | Ett större mönster där en kandidat är begränsad till tre rader och tre kolumner. |
| Kedja | 10 | Ett logiskt resonemang där konsekvenser följs steg för steg mellan kandidater. |
| Lösningsflöde | 11 | Den ordning lösaren använder för att lösa rutnätet steg för steg. |
| Strategiurval | 11 | Beslutet om vilken strategi som är mest rimlig att prova härnäst. |
| Ledtrådsnivå | 12 | Hur mycket hjälp en uppgift ger innan facit. |
| Övningslogg | 12 | En kort anteckning där läsaren skriver strategi, motivering och om steget är säkert. |
| Träningsplan | 13 | En enkel plan för hur läsaren fortsätter öva efter boken. |
| Personlig checklista | 13 | En egen arbetsordning som stöd vid nya sudoku. |
| Sudokuvariant | 13 | En sudokuform som bygger på grundreglerna men lägger till eller ändrar begränsningar. |

## Öppna beslut
- Om träningskapitlet ska kompletteras med fler hela sudoku-rutnät.
- Slutlig visuell stil för färgmarkeringar i EPUB/PDF.
- Om omslaget ska ersättas med en mer avancerad bildgenererad version senare.
- Om manus ska granskas och exporteras till EPUB/PDF/DOCX.

## Nästa rekommenderade steg
- Granska hela manus för progression, nivå och konsekvent terminologi.
- Kontrollera tabeller och rutnätsdiagram inför export.
- Förbered eventuell EPUB/PDF/DOCX-export.
## Tekniska förbättringar

- 2026-05-18: Sudoku-bräden flyttade från markdown-tabeller till strukturerad JSON-data med SVG-generering i `code/generate_boards.py`.

## Senaste uppdatering
- Sudoku-bräden har flyttats från markdown-tabeller till strukturerade board-data och genererade SVG-filer.
- `code/generate_boards.py` har uppdaterats för kandidatlistor och pedagogiska markeringar.
- Text som förklarade punkttecken som tomma rutor har rensats där den hörde ihop med tabellbräden.
