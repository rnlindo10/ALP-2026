while True:
    resposta = input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N\n> ")

    if resposta == 's' or resposta == 'sim':
        continue
    elif resposta == 'n' or resposta == 'não' or resposta == 'nao':
        print("Obrigada. Tenha um bom dia!")
        break
    else:
        print(f'"{resposta}" não é uma resposta válida de sim/não.')