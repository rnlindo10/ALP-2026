import random

numero_secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Digite um número de 1 a 10: "))

    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break

print("O número era:", numero_secreto)