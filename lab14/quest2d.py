import time
def contagem_regressiva(numero):
    while numero >= 0:
        print(numero)
        time.sleep(1)
        numero -= 1

contagem_regressiva(5)