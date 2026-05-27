import random

secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))

    # Ignora números fora do intervalo
    if palpite < 1 or palpite > 10:
        print("Número inválido! Digite um valor entre 1 e 10.")
        continue

    # Verifica se acertou
    if palpite == secreto:
        print("Parabéns! Você acertou!")
        break

    chances -= 1
    print(f"Errado! Você ainda tem {chances} chance(s).")

# Caso acabe as chances sem acertar
if chances == 0:
    print(f"Suas chances acabaram! O número era {secreto}.)