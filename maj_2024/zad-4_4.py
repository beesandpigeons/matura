plik = open('Dane-NF-2405/liczby.txt', 'r')
wiersze = plik.readlines()
lista1 = wiersze[0].strip('/n').split(' ')
liczby1 = []
for liczba in lista1:
    liczby1.append(int(liczba))

maks = 0
#odtąd nie umiałem sam yippee
#i mean zrobiłem ig ale zły wynik wychozdił
maks_indeks = -1
maks_elementy = 50
for okno in range (50, len(liczby1)+1):
    suma = sum(liczby1[:okno])
    srednia = suma/okno
    if srednia > maks:
        maks = srednia
        maks_indeks = 0
        maks_elementy = okno
    for i in range (okno, len(liczby1)):
        suma = suma + liczby1[i] - liczby1[i-okno]
        srednia = suma/okno
        if srednia > maks:
            maks = srednia
            maks_indeks = i - okno +1
            maks_elementy = okno
print(maks, maks_indeks, maks_elementy)
