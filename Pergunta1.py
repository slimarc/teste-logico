vet = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
aux = 0

for i in range(0, len(vet)):
    for j in range(0, len(vet)):
        if(vet[i] == 1):
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux

aux2 = 0
aux2 = vet[5]
vet[5]= vet[4]
vet[4] = aux2

print(vet)