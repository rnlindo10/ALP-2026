def ex1(vet, numero):
    for i in range(len(vet)):
        if vet[i] == numero:
            return i
    return -1


def ex2(vet, inicio, fim):
    soma = 0

    for i in range(inicio, fim + 1):
        soma += vet[i]

    return soma


def ex3(vet):
    maior = vet[0]
    menor = vet[0]

    for numero in vet:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    return maior, menor


def ex4(vet):
    soma = 0

    for i in range(len(vet)):
        if vet[i] % 2 == 0:
            soma += i
            
    return soma