#Nie wiem czy powinienem napisać że n = jakaś liczba czy w ogóle tego nie pisać ?? ale wyszło dobrze so :3:3:3
#Chyba ogólnie muszę się nauczyć jak ładnie napisać taką odpowiedź yk
n =  294762
m_lista=[]
for cyfra in str(n):
    x = int(cyfra) %2
    if x != 0:
        m_lista.append(cyfra)
    if x == 0:
        pass
    #print(m_lista)

m = int(''.join(map(str, m_lista)))
print(m)
