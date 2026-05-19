# Övningar till kapitel 6: Par och låsta möjligheter

## Övning 1: Naket par i en rad

| Ruta | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|
| Kandidater | 2, 8 | 1, 5, 8 | 3, 6 | 2, 8 | 1, 5 | 4, 8 |

### Uppgift

1. Vilka två rutor bildar ett naket par?
2. Vilka kandidater är reserverade av paret?
3. Vilka kandidater kan tas bort från andra rutor i raden?

### Facit

1. C1 och C4.
2. Kandidaterna 2 och 8.
3. Kandidaten 8 kan tas bort från C2 och C6. Kandidaten 2 finns inte i någon annan ruta i raden.

Efter rensning:

| Ruta | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|
| Kandidater | 2, 8 | 1, 5 | 3, 6 | 2, 8 | 1, 5 | 4 |

C6 blir då en enkel singel: 4.

## Övning 2: Dolt par i en box

| Ruta | A | B | C |
|---|---|---|---|
| Kandidater | 1, 3, 7 | 2, 5 | 3, 7, 9 |

| Ruta | D | E | F |
|---|---|---|---|
| Kandidater | 1, 4 | 2, 6 | 5, 8 |

### Uppgift

Siffrorna 3 och 7 förekommer bara i rutorna A och C. Rensa kandidatlistorna.

### Facit

Eftersom 3 och 7 bara kan stå i A och C måste A och C reserveras för dessa två siffror. Därför kan andra kandidater tas bort från A och C.

Före:

| Ruta | A | C |
|---|---|---|
| Kandidater | 1, 3, 7 | 3, 7, 9 |

Efter:

| Ruta | A | C |
|---|---|---|
| Kandidater | 3, 7 | 3, 7 |

## Övning 3: Låsta kandidater från box till rad

| Boxruta | Vänster | Mitten | Höger |
|---|---|---|---|
| Övre rad | 6? | . | 6? |
| Mittenrad | . | . | . |
| Nedre rad | . | . | . |

| Plats på raden | I boxen | I boxen | I boxen | Utanför boxen | Utanför boxen |
|---|---|---|---|---|---|
| Kandidat 6 | 6? | . | 6? | 6? | 6? |

### Uppgift

Vilka kandidater för 6 kan tas bort?

### Facit

Eftersom 6 bara kan stå i den övre raden inom boxen måste boxens 6 hamna i någon av dessa rutor. Därför kan 6 tas bort från övriga rutor på samma rad utanför boxen.

Efter rensning:

| Plats på raden | I boxen | I boxen | I boxen | Utanför boxen | Utanför boxen |
|---|---|---|---|---|---|
| Kandidat 6 | 6? | . | 6? | x | x |

## Övning 4: Är det ett naket par?

Avgör om varje rad innehåller ett naket par.

### A

| Ruta | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| Kandidater | 4, 9 | 1, 2 | 4, 9 | 2, 8 |

### B

| Ruta | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| Kandidater | 4, 9 | 1, 2 | 4, 8, 9 | 2, 8 |

### Facit

A innehåller ett naket par: C1 och C3 med kandidaterna 4 och 9.

B innehåller inte ett naket par mellan C1 och C3, eftersom C3 har tre kandidater: 4, 8 och 9.

## Övning 5: Kort reflektionsfråga

Skriv med egna ord:

- När tar ett naket par bort kandidater från andra rutor?
- När tar ett dolt par bort kandidater från parets egna rutor?

### Exempelsvar

Ett naket par tar bort sina två kandidater från andra rutor i samma grupp. Ett dolt par tar bort andra kandidater från de två rutor där parets två siffror är låsta.
