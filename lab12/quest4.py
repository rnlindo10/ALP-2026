import random
import time

# Sorteia um número N entre 0 e 10
N = random.randint(0, 10)

# (Opcional) Imprime o número sorteado apenas para você saber quantas vezes o loop vai rodar
print(f"Número sorteado: {N}")

# Laço for para repetir a frase N vezes
for i in range(N):
    # i começa em 0, então usamos i+1 para a contagem começar na "Volta 1"
    print(f"Volta {i+1}: Mais uma volta!")
    
    # Pausa a execução por 1 segundo
    time.sleep(1)