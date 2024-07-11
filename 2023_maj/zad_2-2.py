plik = open('bin.txt', 'r')
wiersze = plik.readlines()
def bloki(binarna):
    liczba_bloków = 1
    for i in range(len(binarna)-1):
        if binarna[i] != binarna [i+1]:
            liczba_bloków += 1
    return liczba_bloków

ilosc_liczb = 0
for liczba in wiersze:
    liczba = liczba.strip()
    if bloki(liczba) <= 2:
        ilosc_liczb += 1

print(ilosc_liczb)