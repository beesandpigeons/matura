#ngl nie wiedziałem jak zrobić dzielnik :(
plik = open('Dane-NF-2405/skrot2_przyklad.txt', 'r')
wiersze = plik.readlines()
wyniki = []
for liczba in wiersze:
    for cyfra in str(liczba):
        skrot_lista=[]
        x = int(cyfra) %2
        if x != 0:
            skrot_lista.append(cyfra)
        if x == 0:
            pass
        zlaczony = (''.join(skrot_lista))
        skrot=int(zlaczony)
print(skrot)
