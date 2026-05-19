# Övningar till kapitel 10: Avancerade strategier på ett lugnt sätt

## Syfte

De här övningarna tränar dig på att känna igen avancerade mönster utan att behöva lösa ett helt sudoku. Målet är inte snabbhet. Målet är att du ska kunna säga:

“Jag vet vilken kandidat jag tittar på, vilket mönster jag ser och vilka kandidater som kan rensas.”

## Övning A: Hitta X-Wing-raderna

Kandidat 8 visas i tabellen.

| Rad | Kolumn 2 | Kolumn 6 | Kolumn 9 |
|---|---:|---:|---:|
| Rad 1 | 8 | 8 | . |
| Rad 3 | . | 8 | 8 |
| Rad 5 | 8 | 8 | . |
| Rad 7 | . | 8 | 8 |

Frågor:

1. Vilka två rader bildar ett X-Wing i kolumn 2 och kolumn 6?
2. Vilka två rader bildar ett X-Wing i kolumn 6 och kolumn 9?
3. Vad kan rensas i de berörda kolumnerna?

## Övning B: Rensa rätt kandidater

Rad 2 och rad 8 bildar ett X-Wing för kandidat 3 i kolumn 4 och kolumn 9.

| Plats | Kandidat 3? | Rensa eller behåll? |
|---|---|---|
| Rad 2, kolumn 4 | Ja |  |
| Rad 2, kolumn 9 | Ja |  |
| Rad 8, kolumn 4 | Ja |  |
| Rad 8, kolumn 9 | Ja |  |
| Rad 5, kolumn 4 | Ja |  |
| Rad 6, kolumn 9 | Ja |  |
| Rad 5, kolumn 2 | Ja |  |

Fyll i “rensa” eller “behåll”.

## Övning C: Är det verkligen X-Wing?

Undersök kandidat 6.

| Rad | Kolumn 1 | Kolumn 5 | Kolumn 8 |
|---|---:|---:|---:|
| Rad 2 | 6 | 6 | . |
| Rad 4 | 6 | . | 6 |
| Rad 7 | 6 | 6 | . |

Frågor:

1. Finns det ett tydligt X-Wing?
2. Vilka rader skulle i så fall vara inblandade?
3. Vad gör att mönstret blir säkert eller osäkert?

## Övning D: Swordfish på igenkänningsnivå

Titta på kandidat 2.

| Rad | Kolumn 1 | Kolumn 4 | Kolumn 7 |
|---|---:|---:|---:|
| Rad 1 | 2 | 2 | . |
| Rad 5 | . | 2 | 2 |
| Rad 9 | 2 | . | 2 |

Frågor:

1. Vilka tre rader ingår?
2. Vilka tre kolumner ingår?
3. Varför kan andra 2-kandidater i dessa kolumner vara möjliga att rensa?

## Övning E: Gissning eller logik?

| Formulering | Ditt svar |
|---|---|
| “Jag testar 4 här och ser om det går.” |  |
| “Om den här rutan är 4, kan nästa ruta inte vara 4 eftersom de ligger i samma rad.” |  |
| “Det känns som att 9 borde stå här.” |  |
| “Eftersom dessa två kandidater låser varandra kan den tredje rutan inte ha samma kandidat.” |  |
| “Jag kan inte förklara varför, men jag tror att det är rätt.” |  |

Skriv “gissning” eller “logiskt resonemang”.

## Facit och kommentarer

### Facit A

1. Rad 1 och rad 5 bildar ett X-Wing i kolumn 2 och kolumn 6.
2. Rad 3 och rad 7 bildar ett X-Wing i kolumn 6 och kolumn 9.
3. Kandidat 8 kan rensas från andra rutor i de kolumner som ingår i respektive X-Wing. Mönsterrutorna själva behålls.

### Facit B

| Plats | Rensa eller behåll? |
|---|---|
| Rad 2, kolumn 4 | Behåll |
| Rad 2, kolumn 9 | Behåll |
| Rad 8, kolumn 4 | Behåll |
| Rad 8, kolumn 9 | Behåll |
| Rad 5, kolumn 4 | Rensa |
| Rad 6, kolumn 9 | Rensa |
| Rad 5, kolumn 2 | Behåll |

Kandidat 3 rensas bara från andra rutor i kolumn 4 och kolumn 9. Kolumn 2 påverkas inte.

### Facit C

Rad 2 och rad 7 har kandidat 6 i samma två kolumner: kolumn 1 och kolumn 5. De kan därför bilda ett X-Wing. Rad 4 ingår inte i just det mönstret eftersom den har kandidater i kolumn 1 och kolumn 8.

Det viktiga är att du väljer två rader där kandidaten ligger i exakt samma två kolumner.

### Facit D

1. Raderna är rad 1, rad 5 och rad 9.
2. Kolumnerna är kolumn 1, kolumn 4 och kolumn 7.
3. De tre raderna låser kandidat 2 till dessa tre kolumner. Därför kan andra 2-kandidater i samma kolumner rensas, om hela rutnätet bekräftar att mönstret är komplett.

### Facit E

| Formulering | Svar |
|---|---|
| “Jag testar 4 här och ser om det går.” | Gissning |
| “Om den här rutan är 4, kan nästa ruta inte vara 4 eftersom de ligger i samma rad.” | Logiskt resonemang |
| “Det känns som att 9 borde stå här.” | Gissning |
| “Eftersom dessa två kandidater låser varandra kan den tredje rutan inte ha samma kandidat.” | Logiskt resonemang |
| “Jag kan inte förklara varför, men jag tror att det är rätt.” | Gissning |

## Egen kontroll

Innan du går vidare, kontrollera att du kan formulera detta med egna ord:

- X-Wing handlar om en kandidat i två rader och två kolumner.
- Swordfish är samma typ av tanke men med tre rader och tre kolumner.
- Kedjor är logiska följder, inte gissningar.
- Avancerade tekniker används bäst efter att enklare tekniker är kontrollerade.
