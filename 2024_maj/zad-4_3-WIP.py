plik = open('Dane-NF-2405/liczby_przyklad.txt', 'r')
wiersze = plik.readlines()
wyniki = []

lista1 = wiersze[0].strip('/n').split(' ')
lista2 = wiersze[1].strip('/n').split(' ')
liczby1 = []
liczby2 = []
for liczba in lista1:
    liczby1.append(int(liczba))
for liczba in lista2:
    liczby2.append(int(liczba))

#skopiowałem od kogoś i wyszło mi źle am i cooked
def znajdzlicz(n):
    lista = []
    i = 2
    while i*i <= n:
        while n % i == 0:
            lista.append(i)
            n = n//i
        i+=1
        return lista

for liczby in liczby2:
    liczniki = znajdzlicz(liczby)
    liczby1kop = liczby1.copy()
    czy = True
    for czynnik in liczniki:
        if czynnik not in liczby1kop:
            czy = False
        else:
            liczby1kop.remove(czynnik)
        if czy:
            wyniki.append(liczby)
print(wyniki)
