def reajuste_salario(salario, percentual):
    aumento = salario * percentual / 100
    return salario + aumento

salario = float(input("digite o salario: "))
percentual = float(input("digite o percentual de aumento: "))

print("novo salário:", reajuste_salario (salario, percentual))