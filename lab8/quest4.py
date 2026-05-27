total = 0

while True:
    print("\n=== CANTINA ===")
    print("1 - Coxinha ........ R$ 5,00")
    print("2 - Pastel ......... R$ 7,00")
    print("3 - Refrigerante ... R$ 4,00")
    print("4 - Fechar conta")

    opcao = int(input("Escolha uma opção: "))

    if opcao < 1 or opcao > 4:
        print("Opção inválida!")
        continue

    if opcao == 1:
        total += 5
        print("Coxinha adicionada!")

    elif opcao == 2:
        total += 7
        print("Pastel adicionado!")

    elif opcao == 3:
        total += 4
        print("Refrigerante adicionado!")

    elif opcao == 4:
        print(f"Total da conta: R$ {total:.2f}")
        break