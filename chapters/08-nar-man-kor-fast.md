# Kapitel 8: När man kör fast

## Varför detta kapitel finns

Alla som löser sudoku kör fast ibland. Det betyder inte att du har misslyckats. Ofta betyder det bara att nästa logiska steg inte är lika synligt som de tidigare stegen.

I de första kapitlen har du lärt dig att hitta säkra placeringar, skriva kandidater, rensa med par och se mönster mellan boxar, rader och kolumner. Nu behöver du en metod för stunderna när inget verkar hända.

Det här kapitlet lär dig att felsöka lugnt och metodiskt utan att börja gissa.

## Lärandemål

Efter kapitlet ska du kunna:

- använda en enkel felsökningsrutin när du kör fast,
- kontrollera kandidater utan att börja om från början,
- hitta missade singlar, par och låsta kandidater,
- skilja mellan en återvändsgränd och en tillfällig paus i lösningen.

## Innan vi börjar

Du behöver känna till:

- **kandidat**: en möjlig siffra i en tom ruta,
- **enkel singel** och **dold singel**,
- **naket par** och **dolt par**,
- **låsta kandidater**,
- **kontrollpunkt** från kapitel 5.

Kapitlets viktigaste idé är enkel: när du kör fast ska du inte leta vildare, utan mer ordnat.

## Huvudförklaring

### Varför det känns som att allt tar stopp

När ett sudoku är enkelt finns ofta en tydlig nästa ruta. När svårighetsgraden ökar händer något annat: nästa steg kan vara en rensning, inte en ny siffra.

Det kan därför kännas som att du inte gör framsteg, trots att du faktiskt gör det. Om du tar bort en felaktig kandidat kan du skapa en enkel singel senare.

När du kör fast ska du därför fråga:

1. Har jag missat en säker placering?
2. Har jag missat en kandidat som kan rensas?
3. Har jag uppdaterat anteckningarna efter senaste placeringen?
4. Har jag kontrollerat samma område flera gånger men på olika sätt?

## En felsökningsrutin i fem steg

Använd den här rutinen när du inte ser nästa drag.

| Steg | Fråga | Vad du gör |
|---|---|---|
| 1 | Är alla senaste placeringar uppdaterade? | Ta bort samma siffra från rad, kolumn och box. |
| 2 | Finns enkla singlar? | Leta efter rutor med bara en kandidat. |
| 3 | Finns dolda singlar? | Titta i varje rad, kolumn och box efter siffror med bara en möjlig plats. |
| 4 | Finns par eller låsta kandidater? | Sök efter kandidater som kan rensas. |
| 5 | Behöver jag byta perspektiv? | Gå från ruta-för-ruta till siffra-för-siffra, eller tvärtom. |

Det viktigaste är att göra stegen i ordning. Om du hoppar mellan tekniker blir det lättare att missa något.

## Exempel 1: En missad uppdatering

Anta att du nyss placerade siffran 8 i R4C5. Då måste 8 tas bort som kandidat från:

- rad 4,
- kolumn 5,
- boxen där R4C5 ligger.

Före uppdatering:

| Ruta | Kandidater |
|---|---|
| R4C2 | 2, 8 |
| R4C8 | 1, 6, 8 |
| R2C5 | 3, 8, 9 |
| R5C6 | 4, 8 |

Efter att 8 har placerats i R4C5:

| Ruta | Kandidater efter uppdatering |
|---|---|
| R4C2 | 2 |
| R4C8 | 1, 6 |
| R2C5 | 3, 9 |
| R5C6 | 4 |

Nu har två rutor blivit enkla singlar: R4C2 och R5C6. De fanns inte tydligt förrän uppdateringen var gjord.

Det här är en vanlig orsak till att man kör fast: problemet är inte att tekniken saknas, utan att anteckningarna inte är uppdaterade.

## Exempel 2: Byt från rutor till siffror

Ibland tittar man länge på en tom ruta och försöker avgöra vilken siffra som passar. Om det inte fungerar kan du byta perspektiv.

I stället för att fråga:

“Vad kan stå i den här rutan?”

frågar du:

“Var kan siffran 7 stå i den här boxen?”

Titta på kandidaten 7 i en box:

| Rad/kolumn | C1 | C2 | C3 |
|---|---:|---:|---:|
| R1 | x | 7 | x |
| R2 | x | x | x |
| R3 | x | x | x |

Här har 7 bara en möjlig plats i boxen: R1C2. Det är en dold singel.

Du hittade inte svaret genom att stirra på rutan. Du hittade det genom att följa siffran.

## Exempel 3: När en rensning är nästa steg

Ibland finns ingen ny siffra att skriva in. Då kan nästa steg vara att rensa kandidater.

Titta på den här raden:

| Ruta | R6C1 | R6C2 | R6C3 | R6C4 |
|---|---:|---:|---:|---:|
| Kandidater | 2, 5 | 2, 5 | 2, 5, 8 | 3, 5, 8 |

R6C1 och R6C2 bildar ett naket par: båda rutorna har exakt kandidaterna 2 och 5.

Det betyder att 2 och 5 måste hamna i de två rutorna, i någon ordning. Därför kan 2 och 5 tas bort från andra rutor i samma rad.

Efter rensning:

| Ruta | R6C1 | R6C2 | R6C3 | R6C4 |
|---|---:|---:|---:|---:|
| Kandidater | 2, 5 | 2, 5 | 8 | 3, 8 |

Nu blev R6C3 en enkel singel. Den säkra placeringen uppstod först efter rensningen.

## Vanliga tecken på att du behöver pausa

Det är ofta bättre att ta en kort metodisk paus än att fortsätta på samma sätt.

| Tecken | Trolig orsak | Bra nästa steg |
|---|---|---|
| Du tittar på samma tre rutor om och om igen | Du har fastnat i samma perspektiv | Byt till siffra-för-siffra-scanning. |
| Kandidatlistorna känns röriga | Alla uppdateringar är inte gjorda | Gör en kontrollpunkt. |
| Du vill börja gissa | Nästa steg är troligen en rensning | Leta efter par eller låsta kandidater. |
| Du hittar “nästan” ett mönster | Du kanske blandar ihop tekniker | Skriv en kort motivering innan du agerar. |

En paus är inte ett avbrott i lösningen. Den är en del av lösningsmetoden.

## En praktisk stoppregel

Använd den här regeln:

Om du inte kan förklara varför en siffra ska placeras, ska du inte placera den.

Du får gärna skriva:

- “Den här kandidaten verkar lovande.”
- “Den här rutan behöver kontrolleras senare.”
- “Här kan det finnas ett par.”

Men du ska inte skriva in en siffra i rutnätet förrän den är logiskt säker.

## Vanliga misstag

### Misstag 1: Att gissa “bara en gång”

Varför det händer: Du vill komma vidare och en siffra känns rimlig.

Hur du undviker det: Be om en motivering. Om motiveringen är “det känns rätt” är siffran inte säker.

### Misstag 2: Att kontrollera kandidater men inte grupper

Varför det händer: Det är lätt att fokusera på enskilda rutor.

Hur du undviker det: Kontrollera även rader, kolumner och boxar. Dolda singlar syns ofta bara på gruppnivå.

### Misstag 3: Att glömma gamla tekniker

Varför det händer: När du lär dig par och mönster kan du börja leta efter svåra saker för tidigt.

Hur du undviker det: Börja alltid med enkla singlar och dolda singlar innan du går vidare.

## Övningar

### Övning 1: Välj nästa felsökningssteg

Du har placerat en 4 i R7C3 och kör sedan fast. Vad bör du göra först?

1. Leta efter X-Wing.
2. Uppdatera alla kandidater i rad 7, kolumn 3 och samma box.
3. Gissa mellan två kandidater.
4. Börja om från början.

### Övning 2: Hitta den missade singeln

Efter en uppdatering har du följande kandidater:

| Ruta | Kandidater |
|---|---|
| R2C1 | 1, 6 |
| R2C4 | 6 |
| R2C7 | 3, 6, 9 |

Vilken ruta är en enkel singel?

### Övning 3: Byt perspektiv

I en box finns kandidaten 9 på följande platser:

| Rad/kolumn | C4 | C5 | C6 |
|---|---:|---:|---:|
| R4 | x | x | x |
| R5 | x | 9 | x |
| R6 | x | x | x |

Vad kan du dra för slutsats?

### Fördjupning

Välj ett sudoku du själv har kört fast i. Gör en felsökningsrunda:

1. Uppdatera kandidater efter senaste placeringen.
2. Leta efter enkla singlar.
3. Leta efter dolda singlar.
4. Leta efter par.
5. Leta efter låsta kandidater.

Skriv ner vilket steg som gav framsteg, även om framsteget bara var en kandidatrensning.

## Snabb sammanfattning

- Att köra fast är normalt.
- Nästa logiska steg kan vara en kandidatrensning, inte en ny siffra.
- Börja felsökning med uppdateringar och enkla tekniker.
- Byt perspektiv mellan ruta-för-ruta och siffra-för-siffra.
- Gissa inte om du inte kan motivera placeringen logiskt.

## Quiz/reflektionsfrågor

1. Varför kan en missad kandidatuppdatering göra att man kör fast?
2. Vad är skillnaden mellan att titta på en ruta och att följa en siffra?
3. Varför bör du leta efter enkla singlar innan du letar efter mer avancerade mönster?
4. Vad betyder regeln “kan jag inte förklara det, skriver jag inte in det”?

## Nästa steg

I nästa kapitel tittar vi närmare på vanliga misstag. Där får du lära dig hur fel uppstår, hur du upptäcker dem tidigt och hur du kan rädda en lösning innan den spårar ur.
