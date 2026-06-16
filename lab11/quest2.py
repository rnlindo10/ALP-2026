import random
import time

while True:
    opcao = input("Deseja fazer uma pergunta? (sim/não): ").lower()

    if opcao == "não" or opcao == "nao" or opcao == "n":
        print("Até logo!")
        break

    pergunta = input("Faça sua pergunta: ")

    print("Deixe-me pensar...")
    time.sleep(2)

    print("Estou quase...")
    time.sleep(2)

    print("Já sei!")
    time.sleep(2)

    prob = random.randint(1, 10)

    if prob <= 5:
        print("SIM")
    else:
        print("NÃO")