n = int(input("Quantos números você deseja digitar? "))
soma = 0

for i in range(n):
    valor = int(input(f"Digite o {i+1}º número: "))
    soma += valor

media = soma / n
print(f"Soma: {soma}")
print(f"Quantidade: {n}")
print(f"Média: {media}")