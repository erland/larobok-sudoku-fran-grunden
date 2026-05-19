# Kapitel 9: Vanliga misstag

## Varför detta kapitel finns

När man lär sig sudoku är misstagen nästan alltid logiska, inte personliga. Det handlar sällan om att man är dålig på sudoku. Oftare handlar det om att man placerar en siffra lite för snabbt, glömmer att uppdatera kandidater eller blandar ihop vad som är möjligt med vad som är säkert.

I tidigare kapitel har du lärt dig regler, kandidater, singlar, par, låsta kandidater och felsökning. Nu samlar vi de vanligaste fallgroparna så att du kan känna igen dem innan de förstör resten av lösningen.

Kapitlets mål är inte att göra dig försiktig på ett långsamt sätt. Målet är att göra dig tryggare och mer metodisk.

## Lärandemål

Efter kapitlet ska du kunna:

- känna igen vanliga nybörjarmisstag i sudoku,
- skilja mellan en säker slutsats och en gissning,
- upptäcka när kandidater är gamla eller felaktiga,
- använda enkla kontrollfrågor innan du placerar en siffra,
- reparera mindre misstag utan att börja om från början.

## Innan vi börjar

Du behöver känna till:

- **säker placering**,
- **möjlig placering**,
- **kandidat** och **kandidatlista**,
- **enkel singel** och **dold singel**,
- **naket par** och **låsta kandidater**,
- **kontrollpunkt** och **felsökningsrutin**.

Det viktigaste från tidigare kapitel är detta:

> En siffra ska inte fyllas i för att den verkar trolig. Den ska fyllas i för att andra möjligheter har uteslutits.

## Huvudförklaring

### Misstag 1: Att förväxla möjlig med säker

En av de vanligaste fallgroparna är att se en ruta där en siffra verkar passa och sedan skriva in den direkt.

Det räcker inte att siffran kan stå där. Du behöver veta att den måste stå där.

| Typ av slutsats | Vad den betyder | Ska du fylla i siffran? |
|---|---|---|
| Möjlig placering | Siffran bryter inte mot reglerna just nu. | Nej, inte ännu. |
| Stark misstanke | Siffran känns rimlig efter en snabb blick. | Nej. Kontrollera mer. |
| Säker placering | Alla andra möjligheter är uteslutna. | Ja. |
| Enkel singel | Rutan har bara en kandidat kvar. | Ja. |
| Dold singel | Siffran kan bara stå på en plats i gruppen. | Ja. |

En bra kontrollfråga är:

**Kan jag förklara varför den här siffran måste stå här?**

Om svaret är nej ska siffran inte placeras ännu.

### Misstag 2: Att inte uppdatera kandidater

När du placerar en siffra påverkar det alltid tre områden:

- raden,
- kolumnen,
- boxen.

Om du placerar en 7:a måste 7 tas bort som kandidat från alla tomma rutor i samma rad, kolumn och box.

| Efter en placering | Kontrollera |
|---|---|
| Samma rad | Finns siffran kvar som kandidat någonstans? |
| Samma kolumn | Finns siffran kvar som kandidat någonstans? |
| Samma box | Finns siffran kvar som kandidat någonstans? |

Om kandidaterna inte uppdateras kan gamla anteckningar lura dig senare. Då kan du tro att en ruta har två möjligheter fast den egentligen bara har en.

### Misstag 3: Att leta för brett när man borde leta smalt

När ett sudoku känns svårt är det lätt att börja hoppa runt över hela rutnätet. Man tittar lite här, lite där och hoppas att något ska dyka upp.

Det fungerar ibland, men det gör också att man missar enkla saker.

Prova i stället att smalna av sökningen:

| Om du känner dig fast | Gör detta |
|---|---|
| Du ser inga nya siffror | Gå igenom en siffra i taget, 1–9. |
| Kandidaterna känns röriga | Välj en box och kontrollera den noggrant. |
| Du har många tomma rutor | Leta efter rutor med bara två kandidater. |
| Du hittar inget mönster | Leta efter par eller låsta kandidater. |

Att arbeta smalt betyder inte att du tänker mindre. Det betyder att du ger hjärnan ett tydligare uppdrag.

### Misstag 4: Att rensa kandidater utan tillräckligt skäl

Det är inte bara felaktiga placeringar som kan förstöra ett sudoku. Felaktig kandidatrensning kan vara minst lika farlig.

Om du tar bort en kandidat utan logiskt skäl kanske du senare skapar en falsk singel.

Exempel:

| Ruta | Kandidater före | Felaktig rensning | Vad som kan hända |
|---|---|---|---|
| R4C6 | 2, 5 | 5 tas bort utan skäl | Rutan ser ut som en enkel singel med 2. |
| R7C2 | 1, 8, 9 | 8 tas bort utan skäl | Ett par kan se ut att finnas fast det inte gör det. |

Regeln är:

**Rensa bara en kandidat om du kan säga vilken regel eller strategi som gör den omöjlig.**

### Misstag 5: Att gissa “bara en gång”

Många tänker att en liten gissning inte gör så mycket. Problemet är att en gissning ofta leder till flera nya placeringar. Då blir det svårt att veta var felet började.

I den här boken använder vi därför en tydlig stoppregel:

**Om du inte kan motivera placeringen med logik, skriv den inte som lösning.**

Du kan däremot markera en tanke vid sidan av:

| Osäker tanke | Bättre hantering |
|---|---|
| “Det är nog 4 här.” | Låt 4 stå kvar som kandidat. |
| “Jag tror att 8 passar bäst.” | Leta efter vad som utesluter andra kandidater. |
| “Om det är 6 här går resten bra.” | Behandla det som en hypotetisk tanke, inte som lösning. |

För nybörjare är det bäst att undvika hypotetiska kedjor tills grunderna sitter säkert.

## Exempel: Ett misstag i långsam bild

Titta på den här förenklade raden:

| Ruta | R1C1 | R1C2 | R1C3 | R1C4 | R1C5 | R1C6 | R1C7 | R1C8 | R1C9 |
|---|---|---|---|---|---|---|---|---|---|
| Värde/kandidater | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8,9 | 8,9 |

Här får du inte välja mellan 8 och 9 i de två sista rutorna. Båda är fortfarande möjliga. Det finns ett par, men ingen säker placering.

Om du skriver in 8 i R1C8 bara för att det känns rimligt har du gissat.

Den korrekta slutsatsen är:

- R1C8 och R1C9 innehåller 8 och 9.
- Vi vet ännu inte vilken ruta som är vilken.
- Vi måste söka information från kolumnerna eller boxarna.

Det här är ett bra exempel på skillnaden mellan information och lösning. Du har lärt dig något viktigt, men du har inte fått en ny siffra att fylla i ännu.

## En enkel kontrollrutin före varje placering

Innan du skriver en siffra i rutnätet, ställ tre frågor:

1. Bryter siffran mot rad, kolumn eller box?
2. Är den bara möjlig, eller är den säker?
3. Kan jag förklara varför andra alternativ inte fungerar?

Om du svarar ja på fråga 1 ska siffran inte skrivas in.

Om du inte kan svara på fråga 2 eller 3 ska du vänta.

| Kontrollfråga | Godkänt svar |
|---|---|
| Bryter siffran mot reglerna? | Nej. |
| Är placeringen säker? | Ja. |
| Kan jag motivera den? | Ja, med en regel eller strategi. |

## Vanliga misstag och bättre vanor

| Misstag | Varför det händer | Bättre vana |
|---|---|---|
| Fylla i en möjlig siffra | Den ser rimlig ut. | Kräv en logisk motivering. |
| Glömma uppdatera kandidater | Man går vidare för snabbt. | Uppdatera rad, kolumn och box direkt. |
| Hoppa runt i rutnätet | Man vill hitta något snabbt. | Gör en lösningsrunda. |
| Rensa kandidater för tidigt | Man tror att en kandidat “nog” inte behövs. | Rensa bara med tydlig regel. |
| Gissa vid stopp | Man blir otålig. | Använd felsökningsrutinen från kapitel 8. |
| Inte kontrollera gamla anteckningar | Kandidater känns färdiga. | Gör kontrollpunkter efter större steg. |

## Övningar

### Övning 1: Möjlig eller säker?

Läs varje påstående och markera om det beskriver en möjlig placering eller en säker placering.

| Påstående | Möjlig eller säker? |
|---|---|
| “5 bryter inte mot raden, kolumnen eller boxen.” | |
| “Rutan har bara kandidaten 3 kvar.” | |
| “7 kan bara stå på en plats i boxen.” | |
| “Jag tycker att 2 ser mest sannolik ut här.” | |
| “Alla andra kandidater i rutan är uteslutna.” | |

### Övning 2: Hitta riskfrasen

Vilka av följande meningar signalerar att lösaren är på väg att gissa?

1. “Den här rutan har bara en kandidat kvar.”
2. “Det borde vara 6 här.”
3. “Om jag sätter 4 här verkar resten fungera.”
4. “8 kan bara stå på en plats i den här kolumnen.”
5. “Jag väljer 9 så länge.”

### Övning 3: Kontrollera kandidatlistan

En lösare har placerat 6 i R3C5. Vilka områden måste uppdateras direkt?

| Område | Ska uppdateras? |
|---|---|
| Rad 3 | |
| Kolumn 5 | |
| Boxen som innehåller R3C5 | |
| Alla rutor i hela rutnätet | |
| Endast rutan R3C5 | |

### Övning 4: Reparera arbetsmetoden

Läs situationen:

> Du har arbetat i tio minuter utan framsteg. Kandidaterna är många, och du märker att vissa anteckningar kanske inte har uppdaterats efter de senaste placeringarna.

Skriv en kort arbetsplan i tre steg. Använd gärna orden kontrollpunkt, kandidater och lösningsrunda.

### Fördjupning

Välj ett sudoku du redan har försökt lösa. Gå inte vidare i lösningen direkt. Gör i stället följande:

1. Markera tre placeringar du är helt säker på.
2. Skriv varför varje placering är säker.
3. Hitta en kandidat du har rensat bort.
4. Skriv vilken regel eller strategi som gjorde rensningen giltig.

Om du inte kan motivera en placering eller rensning är det ett tecken på att du ska backa till en tidigare kontrollpunkt.

## Facit och kommentarer

### Övning 1

| Påstående | Svar |
|---|---|
| “5 bryter inte mot raden, kolumnen eller boxen.” | Möjlig. |
| “Rutan har bara kandidaten 3 kvar.” | Säker. |
| “7 kan bara stå på en plats i boxen.” | Säker. |
| “Jag tycker att 2 ser mest sannolik ut här.” | Möjlig eller gissning, inte säker. |
| “Alla andra kandidater i rutan är uteslutna.” | Säker. |

### Övning 2

Riskfraserna är:

- 2: “Det borde vara 6 här.”
- 3: “Om jag sätter 4 här verkar resten fungera.”
- 5: “Jag väljer 9 så länge.”

Mening 1 och 4 beskriver logiska slutsatser.

### Övning 3

| Område | Svar |
|---|---|
| Rad 3 | Ja. |
| Kolumn 5 | Ja. |
| Boxen som innehåller R3C5 | Ja. |
| Alla rutor i hela rutnätet | Nej, inte direkt. |
| Endast rutan R3C5 | Nej, det räcker inte. |

### Övning 4

Ett möjligt svar:

1. Gör en kontrollpunkt och kontrollera de senaste placeringarna.
2. Uppdatera kandidater i berörda rader, kolumner och boxar.
3. Gör en ny lösningsrunda: först singlar, sedan par, sedan låsta kandidater.

## Snabb sammanfattning

- En möjlig placering är inte samma sak som en säker placering.
- Kandidater måste uppdateras efter varje ny siffra.
- Felaktig kandidatrensning kan skapa falska lösningar.
- Gissningar gör det svårt att hitta var ett fel började.
- En bra sudoku-vana är att kunna förklara varje placering med en regel eller strategi.

## Quiz/reflektionsfrågor

1. Varför räcker det inte att en siffra “passar” i en ruta?
2. Vad ska alltid uppdateras efter en ny placering?
3. Hur kan en felaktigt borttagen kandidat skapa problem senare?
4. Vilken kontrollfråga hjälper dig att undvika gissningar?
5. Vad är skillnaden mellan att hitta information och att hitta en säker placering?

## Nästa steg

Nu har du både strategier och bättre kontroll över vanliga misstag. I nästa kapitel ska vi börja se hur mer avancerade strategier fungerar på ett lugnt och begripligt sätt. Fokus ligger inte på att memorera svåra namn, utan på att förstå hur större mönster kan avslöja vilka kandidater som måste bort.
