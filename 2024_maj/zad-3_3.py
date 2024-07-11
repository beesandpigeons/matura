#ngl nie wiedziałem jak zrobić dzielnik :(
import math
plik = open('Dane-NF-2405/skrot2_przyklad.txt', 'r')
wiersze = plik.readlines()
wyniki = []

for liczba in wiersze:
    liczba = liczba.strip()
    skrot_lista = []
    for cyfra in liczba:
        x = int(cyfra) % 2
        if x != 0:
            skrot_lista.append(cyfra)
    skrot = ''.join(map(str, skrot_lista)).replace(" ","")
    if skrot:
        liczba = int(liczba)
        skrot = int(skrot)
        if math.gcd(liczba,skrot) == 7:
            print(liczba)

#w końcu zrobiłem ale na maturze na pewno bym się nie wyrobił
