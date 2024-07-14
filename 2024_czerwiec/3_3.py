plik = open('informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/slowa.txt', 'r')
wiersze = plik.readlines()

wynik = []
for slowo in wiersze:
    for litera in slowo:
        ile = slowo.count(litera)
        if ile >= len(slowo)//2:
            wynik.append(slowo)
            break
print(wynik)
#dobrze yupppppi
