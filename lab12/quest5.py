import random
import time

print("Prepare-se! Pressione ENTER assim que ler 'AGORA!'...")

N = random.randint(2, 10)

time.sleep(N)

print("AGORA!")

tempo0 = time.time()

input()

tempo1 = time.time()

tempo_decorrido = tempo1 - tempo0

print(f"Você levou {round(tempo_decorrido, 3)} segundos para responder.")