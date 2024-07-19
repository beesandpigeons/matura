plik = open('informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/odbiorcy.txt', 'r')
liczby = plik.readlines()
odbiorcy = []
for cyfra in liczby:
    odbiorcy.append(int(cyfra))
pierwsze = []
for i in range (len(liczby)):
    pierwsze.append(i+1)
powtorzenia = 0
wszystkie = []
wszystkie.append(odbiorcy)


while powtorzenia <=6:
    poprzednio = wszystkie[powtorzenia]
    teraz = []
    for i in range (len(odbiorcy)):
        index = odbiorcy[i]-1
        teraz.append(poprzednio[index])
    #print(teraz, len(teraz))
    wszystkie.append(teraz)
    powtorzenia +=1


for lista in wszystkie:
    for i in range (len(lista)):
        if lista[i] == pierwsze[i]:
            print(lista[i], wszystkie.index(lista)+1)
            break

#dobrze yaaaaaaaaaaaaaaaaay
