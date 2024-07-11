#algorytm podaje ostatnią
n = 19
binarna = bin(n)
n_bin = binarna[2:]
w = 5
k = 3
maks = k*w
n_lista = []

while len(n_lista)<maks:
    for i in range (len(n_bin)):
        n_lista.append(n_bin[i])
x = n_lista[-1]
print(x)