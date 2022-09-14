def faltante(vet_preenchido):
    maior = max(vet_preenchido)
    for i in range(1, maior + 1):
        if i not in vet_preenchido:
            vet.append(i)
    return vet

n = int(input("Insira o valor de n"))
vet = [9, 2, 3, 1, 4]

for i in vet:
    if(i==4):
        vet.append(n)
        vet.append(0)
        
print(f'O vetor preenchido com os numeros faltantes é:\n{faltante(vet)}')
