import random # O import traz bibliotecas externas para o código, como a random para sorteios

# 1. função input(): recebe uma string para imprimir na tela, lê o que o usuário digita e retorna o valor sempre como texto (string).
entrada_usuario = input('Digite o seu ano de nascimento: ')

# 2. função int(): converte um valor compatível (como um texto contendo apenas números) para um número inteiro.
ano_nascimento = int(entrada_usuario)

# 3. função type(): recebe um objeto e retorna qual é o seu tipo na programação (int, str, float, bool, etc).
tipo_da_variavel = type(ano_nascimento)

# 4. função str(): faz o caminho inverso do int(), convertendo um valor qualquer para o formato de texto (string).
ano_em_texto = str(ano_nascimento)

# 5. função random.randint(): nativa da biblioteca random, sorteia um número inteiro aleatório dentro do intervalo passado.
numero_da_sorte = random.randint(1, 100)

# 6. função print(): recebe um ou mais argumentos e os imprime na tela do terminal.
print("Você nasceu no ano de", ano_nascimento)
print("O tipo da variável ano_nascimento é:", tipo_da_variavel)
print("Seu número da sorte para hoje é:", numero_da_sorte)