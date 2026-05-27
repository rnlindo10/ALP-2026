while True:
    valor = int(input("Digite o valor do saque: R$ "))

    restante = valor

    n100 = restante // 100
    restante = restante % 100

    n50 = restante // 50
    restante = restante % 50

    n20 = restante // 20
    restante = restante % 20

    if restante != 0:
        print("Não é possível sacar esse valor com as notas disponíveis.")
        continue

    print("Saque realizado com sucesso!")
    print(f"Notas de R$100: {n100}")
    print(f"Notas de R$50: {n50}")
    print(f"Notas de R$20: {n20}")
    break