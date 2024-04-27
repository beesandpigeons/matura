plik = open('Dane_2305/pi.txt', 'r')
wiersze = plik.readlines()
n=0
for i in range(0, len(wiersze)-1):
    pary = wiersze[i][0]+wiersze[i+1][0]
    pary = int(pary)
    if pary > 90:
        n+=1

print(n)