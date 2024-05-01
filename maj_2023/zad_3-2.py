#nie umiałem zorbić sam
plik = open('Dane_2305/pi.txt', 'r')
wiersze = plik.readlines()
ilosc_frag = {}
for i in range (0, 10):
    for j in range (0, 10):
        ilosc_frag[str(i)+str(j)] = 0

for i in range(0, len(wiersze)-1):
    fragment = wiersze[i][0] + wiersze[i+1][0]
    ilosc_frag[fragment] = ilosc_frag[fragment] + 1
    print(ilosc_frag)
    break

min_liczba = 0
min_wartosc = 99999
max_liczba = 0
max_wartosc = 0

for klucz in ilosc_frag:
    liczba_wystapien = ilosc_frag[klucz]
    if liczba_wystapien <= min_wartosc:
        if int(klucz) < min_liczba:
            min_wartosc = liczba_wystapien
            min_liczba = int(klucz)
    if liczba_wystapien >= max_wartosc:
        if int(klucz) < max_liczba:
            max_wartosc = liczba_wystapien
            max_liczba = int(klucz)

print(min_liczba, min_wartosc, max_liczba, max_wartosc)