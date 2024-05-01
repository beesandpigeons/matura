#zrobiłem sam do połowy, potem przepisałem z filmiku bo gówno rozumiałem
#napisałem tak samo jak on wyszło mi 176 zamiast 3, próbowałem naprawić wyszło 1
plik = open('Dane_2305/pi_przyklad.txt', 'r')
wiersze = plik.readlines()
ciągi = []
chwilowe = []
licznik = 0

for i in range (0, len(wiersze)-5):
    czy_ros = True
    czy_mal = True
    poprzednia = int(wiersze[i])
    for j in range (1,6):
        obecna = int(wiersze[i+j])
        if czy_ros and obecna <= poprzednia:
            czy_ros = False
        elif not czy_ros and czy_mal and obecna >= poprzednia:
            czy_mal = False
            break
        poprzednia = obecna
        if czy_ros == False and czy_mal==True:
            chwilowe.append(obecna)
            if len(chwilowe) == 6:
                licznik = licznik + 1
                ciągi.append(wiersze[i:i+j+1])

print(licznik, ciągi,chwilowe)
