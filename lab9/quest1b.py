x = int(input("Digite um valor: "))

cont = 0
soma = 0

while cont <= x:
    soma += cont
    cont += 1

print(f"A soma dos valores de 0 a {x} é {soma}")