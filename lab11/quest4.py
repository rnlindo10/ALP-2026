import random

segredo = [
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)
]

for chance in range(1, 11):
    print(f"\n==== Chance {chance} ====")

    palpite = input("Digite 3 dígitos separados por espaço: ").split()

    saida = ""

    for i in range(3):
        digito = int(palpite[i])

        if digito == segredo[i]:
            saida += "+"
        elif digito in segredo:
            saida += "!"
        else:
            saida += "_"

    print("Saída:", saida)

    if saida == "+++":
        print("Parabéns! Você acertou!")
        break
else:
    print("Você perdeu!")
    print("Número secreto:", *segredo)