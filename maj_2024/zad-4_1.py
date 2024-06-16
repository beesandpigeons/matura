plik = open('Dane-NF-2405/liczby_przyklad.txt', 'r')
wiersze = plik.readlines()

licznik = 0

lista1 = wiersze[0].strip('/n').split(' ')
lista2 = wiersze[1].strip('/n').split(' ')
liczby1 = []
liczby2 = []

for liczba in lista1:
    liczby1.append(int(liczba))
for liczba in lista2:
    liczby2.append(int(liczba))

for liczba in liczby1:
    for liczba2 in liczby2:
        if liczba2%liczba == 0:
            licznik += 1
            break

print(licznik)
#nie wiem nie mogłem się skupić i zrobić sam może faktycznie jestem debilem i nie zdam
