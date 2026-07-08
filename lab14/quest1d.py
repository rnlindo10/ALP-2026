def calculadora(a, b, sinal):
    if sinal == "+":
        return a + b
    elif sinal == "-":
        return a - b
    elif sinal == "*":
        return a * b
    elif sinal == "/":
        return a / b
    else:
        return "sinal inválido."

print(calculadora(2, 3, "+"))
print(calculadora(10, 20, "-"))
print(calculadora(5, 2, "*"))
print(calculadora(100, 5, "/"))