import random

p1 = 0
p2 = 0
rodada = 1

while p1 < 50 and p2 < 50:
    print(f"\n========== RODADA {rodada} ==========")

    palpite1 = int(input(f"Jogador 1 ({p1} pontos): "))
    palpite2 = int(input(f"Jogador 2 ({p2} pontos): "))

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    soma = dado1 + dado2

    print("Rolando os dados...")
    print("Dado 1:", dado1)
    print("Dado 2:", dado2)
    print("Soma:", soma)

    diferenca1 = abs(soma - palpite1)
    diferenca2 = abs(soma - palpite2)

    if diferenca1 < diferenca2:
        p1 += 5
        print("Jogador 1 ganhou a rodada!")
    elif diferenca2 < diferenca1:
        p2 += 5
        print("Jogador 2 ganhou a rodada!")
    else:
        p1 += 2
        p2 += 2
        print("Empate! Cada jogador ganha 2 pontos!")

    rodada += 1

print("\nFim de jogo!")

if p1 >= 50:
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")