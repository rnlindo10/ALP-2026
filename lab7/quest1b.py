soma = 0
contador = 1

# O erro era usar a variável soma no while e precisamos usar um contador para repetir 10 vezes.

while contador <= 10:
    num = int(input("Digite um número para somar: "))
    soma += num
    contador += 1

print("Soma total:", soma)