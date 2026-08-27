def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

print("Média:", calcular_media(n1, n2, n3))