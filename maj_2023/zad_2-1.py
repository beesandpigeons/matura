n = int(input("Podaj liczbę: "))
binarna = bin(n).strip("0b")
b = 1
poprzednia = None
print(binarna)
for cyfra in str(binarna):
    if poprzednia is not None:
        if cyfra != poprzednia:
            b += 1
        else:
            pass
    poprzednia=cyfra
print(b)