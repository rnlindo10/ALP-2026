cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0: 
        continue
# se vc digita um número ímpar o code imprime a mensagem a seguir e se vc digita um numero par reinicia o code
    print(f'{num} é um número ímpar')


#  o continue interrompe o codigo e volta ao while
