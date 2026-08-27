def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado


def reajuste_salario(salario, percentual):
    aumento = salario * percentual / 100
    return salario + aumento


def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def area_circulo(raio):
    area = 3.14 * raio ** 2
    return area