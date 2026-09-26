import func
vet = [14, 2, 63, 27, 3, 49, 52, 10, 77,1]

numero = int(input("digite um numero: "))
posicao = func.ex1(vet,numero)
if posicao != -1:
    print("encontrado na posição:", posicao)
else:
    print("numero não encontrado")

inicio = int(input("digite a posição: "))
fim = int(input("digite a posição final: "))
soma= func.ex2(vet,inicio,fim)
print("Soma do intervalo:", soma)


maior, menor = func.ex3(vet)

print("Maior elemento:", maior)
print("Menor elemento:", menor)


soma_posicoes = func.ex4(vet)

print("Soma das posições dos elementos pares:", soma_posicoes)