pontuacao = 0
erros_seguidos = 0
acertos_seguidos = 0

print("QUIZ: STRANGER THINGS")
print("Responda com A, B, C ou D")

print("1) Qual o nome da cidade onde se passa Stranger Things?")
print("A) Hawkins")
print("B) Hill Valley")
print("C) Sunnydale")
print("D) Riverdale")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "A":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
    print("Penalidade por 2 erros seguidos!")

print("Pontuação:", pontuacao)

print("2) Qual o número da Eleven?")
print("A) 007")
print("B) 010")
print("C) 011")
print("D) 012")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "C":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
    print("Penalidade por 2 erros seguidos!")

print("Pontuação:", pontuacao)

print("3) Quem desaparece na 1ª temporada?")
print("A) Mike")
print("B) Dustin")
print("C) Will")
print("D) Lucas")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "C":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
    print("Você errou duas seguidas!")

print("Pontuação:", pontuacao)

print("4) Qual o nome do mundo paralelo?")
print("A) Mundo Sombrio")
print("B) Mundo Invertido")
print("C) Dimensão X")
print("D) Outro Mundo")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "B":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
    print("Penalidade por 2 erros seguidos!")

print("Pontuação:", pontuacao)

print("5) Quem é o chefe de polícia?")
print("A) Hopper")
print("B) Steve")
print("C) Jonathan")
print("D) Billy")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "A":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
    print("Penalidade por 2 erros seguidos!")

print("Pontuação:", pontuacao)

print("6) Qual criatura aparece na 1ª temporada?")
print("A) Vecna")
print("B) Demogorgon")
print("C) Mind Flayer")
print("D) Dragão")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "B":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
print("Penalidade por 2 erros seguidos!")

print("Pontuação:", pontuacao)

print("7) Qual o jogo que eles gostam?")
print("A) Xadrez")
print("B) Futebol")
print("C) Dungeons & Dragons")
print("D) Cartas")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "C":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
    print("Penalidade por 2 erros seguidos!")

print("Pontuação:", pontuacao)

print("8) Quem é amigo próximo de Dustin?")
print("A) Steve")
print("B) Hopper")
print("C) Billy")
print("D) Murray")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "A":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
    print("Penalidade por 2 erros seguidos!")

print("Pontuação:", pontuacao, "\n")

print("9) Quem é o vilão da 4ª temporada?")
print("A) Demogorgon")
print("B) Vecna")
print("C) Mind Flayer")
print("D) Billy")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "B":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
print("Penalidade por 2 erros seguidos!")

print("Pontuação:", pontuacao)

print("10) Qual música ajuda Max?")
print("A) Thriller")
print("B) Running Up That Hill")
print("C) Billie Jean")
print("D) Stayin Alive")
resp = input("Resposta: ").upper()

if acertos_seguidos >= 2:
    pontuacao += 15
else:
    pontuacao += 10

if resp == "B":
    acertos_seguidos += 1
    erros_seguidos = 0
else:
    erros_seguidos += 1
    acertos_seguidos = 0
    pontuacao -= 5

if erros_seguidos >= 2:
    pontuacao -= 10
    print("Penalidade por 2 erros seguidos!")

print()
print(" Fim do Quiz!")
print("Pontuação final:", pontuacao)

if pontuacao > 80:
    print("Classificação: Excelente")
elif pontuacao >= 50:
    print("Classificação: Bom")
else:
    print("Classificação: Precisa melhorar")