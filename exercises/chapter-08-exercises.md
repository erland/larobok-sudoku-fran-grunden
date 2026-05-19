# Övningar till kapitel 8: När man kör fast

## Syfte

De här övningarna tränar dig i att felsöka när ett sudoku känns stillastående. Målet är att hitta nästa logiska steg utan att gissa.

## Övning A: Vad gör du först?

Du har precis placerat siffran 3 i R5C8. Sedan hittar du inget mer.

Vilket steg bör komma först?

1. Leta efter avancerade mönster.
2. Uppdatera kandidater i rad 5, kolumn 8 och samma box.
3. Gissa i en ruta med två kandidater.
4. Radera alla anteckningar.

Skriv också varför ditt val är bäst.

## Övning B: Enkel singel efter uppdatering

Efter att en kandidat har rensats ser kandidatlistorna ut så här:

| Ruta | Kandidater |
|---|---|
| R1C4 | 2, 7 |
| R1C6 | 7 |
| R1C9 | 2, 5, 7 |

Svara:

1. Vilken ruta är en enkel singel?
2. Vilken siffra ska placeras där?
3. Vad ska uppdateras efter placeringen?

## Övning C: Dold singel i en box

Titta bara på kandidaten 4 i den här boxen.

| Rad/kolumn | C1 | C2 | C3 |
|---|---:|---:|---:|
| R4 | x | x | x |
| R5 | x | 4 | x |
| R6 | x | x | x |

Svara:

1. Finns en dold singel?
2. Vilken ruta gäller det?
3. Varför är placeringen säker?

## Övning D: Rensning före placering

Titta på raden:

| Ruta | R8C1 | R8C2 | R8C3 | R8C4 |
|---|---:|---:|---:|---:|
| Kandidater | 1, 6 | 1, 6 | 1, 6, 9 | 4, 6, 9 |

Svara:

1. Finns ett naket par?
2. Vilka två rutor bildar paret?
3. Vilka kandidater kan rensas från andra rutor i raden?
4. Blir någon ruta en enkel singel efter rensningen?

## Övning E: Skriv en motivering

Välj ett av påståendena och skriv en kort logisk motivering.

1. “R1C6 måste vara 7.”
2. “Kandidaten 6 kan tas bort från R8C3.”
3. “Jag ska inte skriva in en siffra här ännu.”

Målet är att träna på att skilja mellan en känsla och en bevisad slutsats.

## Facit

### Facit A

Rätt svar är 2.

Efter en placering ska du först uppdatera kandidater i samma rad, kolumn och box. Annars kan du missa enkla singlar eller rensningar som placeringen skapade.

### Facit B

1. R1C6 är en enkel singel.
2. Siffran 7 ska placeras där.
3. Efter placeringen ska 7 tas bort som kandidat från samma rad, kolumn och box.

### Facit C

1. Ja.
2. R5C2.
3. Kandidaten 4 finns bara på en möjlig plats i boxen. Därför är R5C2 en säker placering för 4.

### Facit D

1. Ja.
2. R8C1 och R8C2 bildar ett naket par.
3. Kandidaterna 1 och 6 kan tas bort från andra rutor i samma rad.
4. R8C3 blir 9 efter att 1 och 6 rensas bort. R8C4 blir 4, 9 eftersom 6 tas bort.

### Facit E

Exempel på godkända motiveringar:

1. “R1C6 måste vara 7 eftersom rutan bara har kandidaten 7 kvar.”
2. “Kandidaten 6 kan tas bort från R8C3 eftersom 1 och 6 är låsta som ett naket par i R8C1 och R8C2.”
3. “Jag ska inte skriva in en siffra här ännu eftersom det finns flera kandidater kvar och jag inte kan visa vilken som är säker.”
