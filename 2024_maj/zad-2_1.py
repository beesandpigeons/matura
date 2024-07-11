n = 87654321012345678
c = 0
b = 1
licznikc=0

while n>0:
    a = n % 10
    n = n//10
    if a % 2 == 0:
        c = c+b*(a//2)
    else:
        c = c+b
        licznikc+=1
    b=b*10
print(c, licznikc)
#121101; 2 Dobrze jupiii
#41312111011121344; 7 X
    #Powinno być 41312111011121314;8, pousuwałem int i dobrze my wyszło więc nie wiem czy liczyć
    #No było źle obviously ale umiem zrobić ig? Nie wiem potem zdecyduję
