# Exportguide

## Grundprincip
Export ska alltid utgå från `docs/export-metadata.yaml` och kapitelordningen där.

## Före export
Kontrollera att:
- `chapters/00-inledning.md` finns.
- Alla kapitel i metadatafilen finns.
- Författare, titel, språk, datum, version och identifierare är ifyllda.
- Inga rubriker använder H4 eller lägre.
- Markdown renderas till riktig typografi i EPUB/PDF/DOCX.
- Bildlänkar pekar på existerande filer.

## EPUB
- Ingen innehållsförteckning som vanligt textkapitel.
- Luftig CSS med tydliga styckeavstånd.
- Rutnätstabeller ska vara läsbara.

## PDF
- Innehållsförteckning ska ligga före inledningen.
- Sidbrytning före varje kapitel.
- Tabeller, listor och kodblock ska renderas tydligt.
