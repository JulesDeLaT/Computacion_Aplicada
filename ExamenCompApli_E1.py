import math


sumaDiagonal = 0
matriz = []
matrizFinal = []
numPrimo = 0
num = 0

def pruebaMillerRabin(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


m = int(input("Dimension M: "))

while numPrimo < m*m:
    if pruebaMillerRabin(num):
        matriz.append(num)
        numPrimo += 1
    num += 1

for i in range(0, len(matriz), m):
    matrizFinal.append(matriz[i:i+m])

for fila in matrizFinal:
    numerosSeparados = [("{:2d}".format(num)) for num in fila]
    conFormato = ""
    for i, num_str in enumerate(numerosSeparados):
        conFormato += num_str
        if i < len(numerosSeparados) - 1:
            conFormato += "  "
    print(conFormato)

for i in range(m):
    for j in range(i, m):
        sumaDiagonal += matrizFinal[i][j] 

print("Suma = ", sumaDiagonal)




