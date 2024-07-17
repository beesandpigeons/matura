plik = open('informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki/odbiorcy.txt', 'r')
liczby = plik.readlines()
odbiorcy = []
for cyfra in liczby:
    odbiorcy.append(int(cyfra))

#teraz = []
#for i in range (len(odbiorcy)):
#    index = odbiorcy[i]-1
    #teraz.append(odbiorcy[index])
licznik = 0
#print(teraz)
for i in range (len(odbiorcy)):
    index = i+1
    if index not in odbiorcy:
        licznik +=1

print(licznik)
#dooobrze
