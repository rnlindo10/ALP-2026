import random
import time

inicio = time.time()

print("Preparando envio...")

time.sleep(random.randint(1, 3))

print("Mensagem enviada!")

fim = time.time()

print("Enviou demorou", int(fim - inicio), "segundos")