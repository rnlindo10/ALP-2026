N = int(input("Quantos números quer digitar? "))
contador = 1
impares = 0

# O erro era que o contador nunca aumentava, causando loop infinito.

while contador <= N:
    num = int(input("Digite um número: "))

    if num % 2 != 0:
        impares += 1

    contador += 1  # incrementa o contador

print(f"Quantidade de ímpares: {impares}")