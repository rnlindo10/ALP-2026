chances = 5
palavra_secreta = 'batata'

while chances > 0:
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances: ")
    chances -= 1

    # Quando o usuário acerta a palavra, o break encerra o loop imediatamente.
    if palavra == 'batata':
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        break

    # Quando o usuário erra, o programa continua até acabar as chances.
