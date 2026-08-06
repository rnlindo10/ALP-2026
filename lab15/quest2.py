def celsius_para_fahrenheit(c):
    fahrenheit = (c * 1.8) + 32
    return fahrenheit


celsius = float(input("Digite a temperatura em Celsius: "))

f = celsius_para_fahrenheit(celsius)

print(f"{celsius:.1f}°C equivalem a {f:.1f}°F")