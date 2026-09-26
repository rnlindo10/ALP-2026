# Ryan & Sophia - INFO 1A

jogar_novamente = "SIM"

maior_nota = -999
campeao = ""

while jogar_novamente == "SIM":

    nome = input("\nDigite o nome do jogador: ")

    pontuacao = 0
    erros_seguidos = 0
    acertos_seguidos = 0
    pergunta = 0

    print("\nQUIZ: STRANGER THINGS")
    print("Responda com A, B, C ou D")

    while pergunta < 10:

        if pergunta == 0:
            print("\n1) Qual o nome da cidade onde se passa Stranger Things?")
            print("A) Hawkins")
            print("B) Hill Valley")
            print("C) Sunnydale")
            print("D) Riverdale")
            correta = "A"

        elif pergunta == 1:
            print("\n2) Qual o número da Eleven?")
            print("A) 007")
            print("B) 010")
            print("C) 011")
            print("D) 012")
            correta = "C"

        elif pergunta == 2:
            print("\n3) Quem desaparece na 1ª temporada?")
            print("A) Mike")
            print("B) Dustin")
            print("C) Will")
            print("D) Lucas")
            correta = "C"

        elif pergunta == 3:
            print("\n4) Qual o nome do mundo paralelo?")
            print("A) Mundo Sombrio")
            print("B) Mundo Invertido")
            print("C) Dimensão X")
            print("D) Outro Mundo")
            correta = "B"

        elif pergunta == 4:
            print("\n5) Quem é o chefe de polícia?")
            print("A) Hopper")
            print("B) Steve")
            print("C) Jonathan")
            print("D) Billy")
            correta = "A"

        elif pergunta == 5:
            print("\n6) Qual criatura aparece na 1ª temporada?")
            print("A) Vecna")
            print("B) Demogorgon")
            print("C) Mind Flayer")
            print("D) Dragão")
            correta = "B"

        elif pergunta == 6:
            print("\n7) Qual o jogo que eles gostam?")
            print("A) Xadrez")
            print("B) Futebol")
            print("C) Dungeons & Dragons")
            print("D) Cartas")
            correta = "C"

        elif pergunta == 7:
            print("\n8) Quem é amigo próximo de Dustin?")
            print("A) Steve")
            print("B) Hopper")
            print("C) Billy")
            print("D) Murray")
            correta = "A"

        elif pergunta == 8:
            print("\n9) Quem é o vilão da 4ª temporada?")
            print("A) Demogorgon")
            print("B) Vecna")
            print("C) Mind Flayer")
            print("D) Billy")
            correta = "B"

        elif pergunta == 9:
            print("\n10) Qual música ajuda Max?")
            print("A) Thriller")
            print("B) Running Up That Hill")
            print("C) Billie Jean")
            print("D) Stayin Alive")
            correta = "B"

        resp = input("Resposta: ").upper()

        while resp != "A" and resp != "B" and resp != "C" and resp != "D":
            print("Opção inválida! Digite apenas A, B, C ou D.")
            resp = input("Resposta: ").upper()

        if resp == correta:

            if acertos_seguidos >= 2:
                pontuacao += 15
            else:
                pontuacao += 10

            acertos_seguidos += 1
            erros_seguidos = 0

        else:
            pontuacao -= 5
            erros_seguidos += 1
            acertos_seguidos = 0

            if erros_seguidos >= 2:
                pontuacao -= 10
                print("Penalidade por 2 erros seguidos!")

        print("Pontuação:", pontuacao)

        pergunta += 1

    print("\nFim do Quiz!")
    print("Pontuação final:", pontuacao)

    if pontuacao > 80:
        print("Classificação: Excelente")

    elif pontuacao >= 50:
        print("Classificação: Bom")

    else:
        print("Classificação: Precisa melhorar")

    if pontuacao > maior_nota:
        maior_nota = pontuacao
        campeao = nome

    jogar_novamente = input("\nDeseja jogar novamente? ").upper()

print("\nPrograma encerrado!")
print("Maior nota:", maior_nota)
print("Campeão:", campeao)
