plik = open('Dane-NF-2405/liczby_przyklad.txt', 'r')
wiersze = plik.readlines()
chwil = wiersze[0].split()
liczby = [int(x) for x in chwil]
liczby.sort(reverse=True)

print(liczby[100])
