#Zrobiłem sam, nic mi nie wychodziło, zobaczyłem rozwiązanie na internecie i jakimś cudem było praktycznie tak samo,
#oprócz tego że miałęm == zamiast = w 16. Idk czy liczyć czy nie.

plik = open('Dane-NF-2405/skrot_przyklad.txt', 'r')
wiersze = plik.read()
wiersze = wiersze.split()

licznik = 0
najw = -1
skrot = []

for liczba in wiersze:
    ma = False
    for cyfra in liczba:
        cyfra = int(cyfra)
        if cyfra % 2 == 1:
            ma = True
    if not ma:
        licznik += 1
        liczba = int(liczba)
        if liczba > int(najw):
            najw = liczba

print(licznik,najw)
