import codecs
plik = open('informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/slowa.txt', 'r')
wiersze = plik.readlines()

slowa = []
for wiersz in wiersze:
    wiersz.strip()
    nowe = codecs.encode(wiersz, 'rot13')
    nowere = nowe[::-1]
    if sorted(wiersz) == sorted(nowere):
        slowa.append(wiersz)
        

print(len(slowa), max(slowa, key=len))

#dobrze zrobiłem sam ale potrzebowałem DUŻO wyszukiwania
