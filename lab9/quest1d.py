quantidade = int(input("Quantos valores deseja digitar? "))

soma = 0
cont = 1

while cont <= quantidade:
    valor = int(input("Digite um valor: "))

    if valor % 2 == 0:
        soma += valor

    cont += 1

print("A soma dos valores pares digitados é:", soma)