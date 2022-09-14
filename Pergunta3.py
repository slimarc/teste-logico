from itertools import combinations

def encontrar_combinacao(soma):
    a = True
    b = False
    for i in (2, len(vet)):
        for comb in combinations(vet, i):
            if (sum(comb) == x):
                print("Existe a soma no vetor: ")
                print (comb,'= ', x)
                return a
        if(sum(comb) != x):
            print("Nao existe a soma no vetor")
            return b
    return soma
    
    
vet = [1, 15, 2, 7, 2, 5, 7, 1, 4]
x = int(input("Insira o valor de x para verificar se a soma existe dentro do arrey"))

encontrar_combinacao(x)