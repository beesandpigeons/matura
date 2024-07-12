plik = open('informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/slowa.txt', 'r')
wiersze = plik.readlines()
ile = 0
for wiersz in wiersze:
    for i in range (len(wiersz)-2):
        if wiersz[i] == 'k':
            if wiersz[i+2] == 't':
                ile += 1
print(ile)
#udało się samemu confetti emoji
