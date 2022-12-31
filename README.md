## Luhnov algoritam
Luhnov algoritam se općenito koristi za provjere validnosti različitih identifikacijskih
brojeva poput brojeva kreditnih kartica, brojeva socijalnog osiguranja, IMEI brojeva i mnogih drugih. Također je poznat i kao "modul 10" ili "mod 10" algoritam.
Ovaj algoritam verifikuje ispravnost identifikacijskog broja pomoću kontrolne cifre koja je uključena u sam broj.

Algoritam je sljedeći:

1. Počevši od krajnje desne cifre, koja je obično kontrolna cifra, krećući se nalijevo, udvostručiti vrijednost svake druge cifre

2. Ako je taj proizvod veći od 9 (npr. 8 × 2 = 16), tada sabrati cifre proizvoda (npr. 16: 1 + 6 = 7, 18: 1 + 8 = 9).Izračunati sumu svih cifara

3. Ako je suma kongruentna sa nulom po modulu 10 (ako se suma završava nulom) tada je broj ispravan sudeći po Luhnovom algoritmu, inače je neispravan.
