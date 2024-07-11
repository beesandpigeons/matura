# nie umiałem zrobić sam ale byłem padnięty nie jestem nawet pewien czy nie powinno dodać się zer wypuśćcie mnie

plik = open('bin.txt', 'r')
wiersze = plik.readlines()

for wiersz in wiersze:
    wiersz = wiersz.strip()
    dziesietna = int(wiersz, 2)
    wynik = dziesietna^(dziesietna//2)
    wynik = bin(wynik).strip('0b')
    print(wynik)