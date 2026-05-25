maior = float('-inf')
contador = 1

# O erro era usar variável soma que nem existia e o maior começava com +inf, impossibilitando comparação correta

while contador <= 10:
    num = int(input("Digite um número: "))

    if num > maior:
        maior = num

    contador += 1

print("O maior número é:", maior)