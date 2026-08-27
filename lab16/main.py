from funçoes import fatorial, reajuste_salario, celsius_para_fahrenheit, calcular_media, area_circulo
# 1 - Fatorial
num = int(input("Digite um número: "))
print("Fatorial:", fatorial(num))

# 2 - Reajuste salarial
salario = float(input("\nDigite o salário: "))
percentual = float(input("Digite o percentual de aumento: "))
print("Novo salário:", reajuste_salario(salario, percentual))

# 3 - Celsius para Fahrenheit
temperatura = float(input("\nDigite a temperatura em Celsius: "))
print("Temperatura em Fahrenheit:", celsius_para_fahrenheit(temperatura))

# 4 - Média de três notas
n1 = float(input("\nDigite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
print("Média:", calcular_media(n1, n2, n3))

# 5 - Área do círculo
raio = float(input("\nDigite o raio do círculo: "))
print("Área do círculo:", area_circulo(raio))