primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

# Calcula o valor absoluto da diferença
valor_absoluto = abs(primeiro_numero - segundo_numero)

# Arredonda o resultado para duas casas decimais
valor_arredondado = round(valor_absoluto, 2)

print(f"A diferença absoluta entre os números é: {valor_arredondado}")