plik = open('matura/bin.txt', 'r')
wiersze = plik.readlines()

największa = 0
for wiersz in wiersze:
    dziesiętna = int(wiersz, 2)
    if dziesiętna > największa:
        największa = dziesiętna

wynik = bin(największa).strip('0b')
print(wynik)