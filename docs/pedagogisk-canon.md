# Pedagogisk canon

## Språk
Svenska.

## Svårighetsgrad
Boken börjar på nybörjarnivå och rör sig gradvis mot grundnivå och lätt avancerad nivå.

## Läsarprofil
Vuxen nybörjare som vill förstå hur man löser sudoku logiskt och metodiskt.

## Ton
Vänlig, lugn, tydlig och uppmuntrande. Undvik att få läsaren att känna sig långsam eller dålig.

## Pedagogisk profil
- Förklara först konkret.
- Introducera 1–3 huvudbegrepp per kapitel.
- Visa ett kort exempel.
- Låt läsaren öva direkt.
- Repetera tidigare begrepp när de används igen.

## Visuellt arbetssätt
Inre illustrationer används inte i första versionen. I stället används:
- markdown-tabeller för rutnät,
- tydliga markeringar som **fet stil** och korta etiketter,
- färgförslag i export-CSS när det blir aktuellt.

## Återkommande exempelrutnät
Ett återkommande sudoku-exempel ska användas från kapitel 2 och framåt. Kapitel 1 använder huvudsakligen tomma eller nästan tomma rutnät för att lära ut strukturen.

## Avgränsning
Boken fokuserar på klassisk 9×9-sudoku och logiska metoder, inte gissning.

## Introducerade begrepp

## Kapitel 2-beslut

Kapitel 2 introducerar eliminering, säker placering och möjlig placering. Boken skiljer tydligt mellan att en siffra kan stå i en ruta och att den måste stå där. Detta är en central pedagogisk regel för resten av boken.

## Exempelstil från kapitel 2

- `x` används i tabeller för uteslutna rutor.
- `.` används för tomma rutor.
- **Fet stil** används sparsamt för den säkra placeringen.
- Läsaren ska uppmuntras att formulera en kort logisk motivering innan en siffra skrivs in.


## Kapitel 3-beslut

Kapitel 3 introducerar kandidat, kandidatlista och anteckning. En kandidat definieras som en möjlig siffra, inte som ett svar. Boken ska fortsätta betona skillnaden mellan “kan vara” och “måste vara”.

## Exempelstil från kapitel 3

- Kandidatlistor visas i enkla markdown-tabeller.
- Kandidater skrivs med komma, till exempel `2, 4, 8`.
- Fulla anteckningar introduceras som metod, men lätta anteckningar rekommenderas först för att undvika rörighet.
- När en säker siffra placeras ska kandidaten tas bort från samma rad, kolumn och box.

## Kapitel 4-beslut

Kapitel 4 introducerar scanning, enkel singel och dold singel. Boken ska fortsätta skilja mellan två frågor: “Vad kan stå i den här rutan?” och “Var kan den här siffran stå i gruppen?”.

## Exempelstil från kapitel 4

- Scanning visas med små rutnät och `x` för blockerade placeringar.
- Enkel singel förklaras som en ruta med en enda kandidat.
- Dold singel förklaras som en siffra som bara har en möjlig plats i en rad, kolumn eller box.
- Kapitel 4 använder tabeller i stället för illustrationer och undviker färgberoende resonemang i rå markdown.


## Kapitel 5-beslut

Kapitel 5 introducerar lösningsrunda, kontrollpunkt och arbetsrutin. Boken ska från och med detta kapitel uppmuntra läsaren att arbeta i återkommande rundor i stället för att hoppa planlöst mellan rutor.

## Exempelstil från kapitel 5

- Arbetsordning visas som numrerade steg.
- Kontrollpunkter visas som korta tabeller med fråga och syfte.
- Begreppet “nästa bästa steg” används för att prioritera enkla singlar, dolda singlar och kontrollpunkter.
- Kapitlet stärker regeln att varje placering ska kunna motiveras logiskt innan den skrivs in.

## Kapitel 6-beslut

Kapitel 6 introducerar naket par, dolt par och låsta kandidater. Kapitlet markerar övergången från att främst hitta nya siffror till att även rensa kandidatlistor som ett legitimt lösningssteg.

## Exempelstil från kapitel 6

- Kandidatrensning visas med före- och eftertabeller.
- `x` används för borttagna kandidater i förenklade rad- och boxexempel.
- För par betonas att ordningen ännu är okänd: tekniken reserverar möjligheter men gissar inte.
- Låsta kandidater förklaras först med box till rad/kolumn, därefter nämns motsatt riktning.


## Kapitel 7-beslut

Kapitel 7 introducerar rad-box-interaktion och kolumn-box-interaktion. Kapitlet fördjupar låsta kandidater genom att visa hur mönster mellan box och rad/kolumn kan användas för säker kandidatrensning.

## Exempelstil från kapitel 7

- Tabeller visar förenklade boxar och rader/kolumner.
- `x` används för uteslutna eller borttagna kandidater.
- Kapitlet skiljer tydligt mellan att rensa en kandidat och att placera en siffra.
- Efter varje rensning uppmuntras läsaren att leta efter nya enkla singlar eller dolda singlar.

## Kapitel 8-beslut

Kapitel 8 introducerar felsökningsrutin, perspektivbyte och stoppregel. Kapitlet ska normalisera att läsaren kör fast och visa att nästa logiska steg ofta är en uppdatering eller kandidatrensning, inte en ny placering.

## Exempelstil från kapitel 8

- Felsökningsrutinen visas som en enkel femstegsprocess.
- Tabeller används för att visa före- och efterkandidater.
- Kapitlet repeterar enkla singlar, dolda singlar, nakna par och låsta kandidater i felsökningssammanhang.
- Boken fortsätter betona att varje placering ska kunna motiveras logiskt innan den skrivs in.


## Kapitel 9-beslut

Kapitel 9 repeterar och förtydligar vanliga misstag: att förväxla möjlig med säker, att glömma kandidatuppdatering, att rensa utan skäl och att gissa vid stopp. Kapitlet introducerar riskfras, falsk singel och logisk motivering.

## Exempelstil från kapitel 9

- Misstag visas som tabeller med orsak och bättre vana.
- Kapitlet använder kontrollfrågor före placeringar.
- Riskfraser används för att hjälpa läsaren upptäcka när resonemang glider från logik till gissning.
- Kandidatrensning ska alltid kopplas till en namngiven regel eller strategi.


## Kapitel 10-beslut

Kapitel 10 introducerar X-Wing, Swordfish och kedja på en lugn igenkänningsnivå. Kapitlet ska inte kräva att läsaren behärskar avancerade strategier fullt ut, utan ge förståelse för hur större kandidat-mönster kan leda till säker kandidatrensning.

## Exempelstil från kapitel 10

- Avancerade strategier visas med förenklade tabeller, inte kompletta rutnät.
- En kandidat i taget analyseras.
- X-Wing förklaras först som två rader och två kolumner.
- Swordfish beskrivs som en större variant av samma tanke, utan att kräva full expertbehärskning.
- Kedjor presenteras som logiska konsekvenser, inte som gissning.
- Kapitlet betonar att avancerade strategier oftast rensar kandidater snarare än placerar siffror direkt.

## Kapitel 11-beslut

Kapitel 11 introducerar lösningsflöde och strategiurval. Kapitlet ska visa hur tidigare strategier kombineras i en hel lösningsprocess, utan att läsaren behöver behärska hela lösningen perfekt.

## Exempelstil från kapitel 11

- Kompletta lösningar visas som arbetsflöde snarare än som facitlista.
- Tabeller används för rutnät, saknade siffror, strategiordning och lösningslogg.
- Kapitlet betonar att den enklaste fungerande strategin ska väljas först.
- Kandidatuppdatering efter placeringar är en obligatorisk vana.
- Lösningslogg används som pedagogiskt verktyg för att skilja säker logik från gissning.


## Kapitel 12-beslut

Kapitel 12 är ett träningskapitel och introducerar ledtrådsnivå och övningslogg. Kapitlet ska främst förstärka tidigare strategier genom korta delproblem, inte introducera tung ny teori.

## Exempelstil från kapitel 12

- Övningar grupperas efter strategi: singlar, dolda singlar, par, låsta kandidater och strategiurval.
- Ledtrådar ges stegvis före facit.
- Facit innehåller kort logisk motivering, inte bara svar.
- Arbetsblad används för att hjälpa läsaren skriva strategi och motivering.
- Kapitlet betonar att kandidatrensning är ett giltigt träningsresultat.


## Kapitel 13: Nästa steg
- Kapitlet avslutar boken och hjälper läsaren fortsätta träna efter första genomgången.
- Nya begrepp: träningsplan, personlig checklista och sudokuvariant.
- Pedagogisk funktion: flytta läsaren från bokstyrd övning till egen metodisk träning.
- Ton: uppmuntrande, realistisk och tydligt inriktad på fortsatt utveckling utan stress.
- Viktig princip: framsteg mäts i bättre resonemang och färre gissningar, inte bara i snabbare lösningstid.

## Brädlogik
- Sudoku-bräden lagras strukturerat i `examples/boards/boards.json`.
- Genererade SVG-filer i `assets/boards/` används i kapiteltexten i stället för markdown-tabeller för visuella sudoku-exempel.
- Tomma rutor förklaras visuellt i SVG och behöver normalt inte beskrivas med punktnotation i brödtexten.
