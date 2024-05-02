#nie umiałem sam zrobić ale idk może nie myślę
plik = open('Dane_2305/pi.txt', 'r')
wiersze = plik.readlines()

max_dlug = 0
max_pozycja = 0
dlug_teraz = 0
pozycja_teraz = 0

for i in range (0, len(wiersze)-5):
    czy_ros = True
    czy_mal = True
    poprzednia = int(wiersze[i])
    j = i+1
    while j < len(wiersze) and (czy_ros == True or czy_mal == True):
        dlug_teraz += 1
        obecna = int(wiersze[j])
        if czy_ros and obecna <= poprzednia:
            if dlug_teraz == 1:
                dlug_teraz == 0
                break
            czy_ros = False
        elif not czy_ros and czy_mal and obecna >= poprzednia:
            czy_mal = False
            if dlug_teraz > max_dlug:
                max_dlug = dlug_teraz
                max_pozycja = i
            dlug_teraz = 0
        
        poprzednia = obecna
        j = j+1

print(max_pozycja+1, wiersze[max_pozycja:max_pozycja+max_dlug])
