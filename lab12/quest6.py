import datetime

nome1 = input("Nome da primeira pessoa: ")
data1_str = input("Data de nascimento (dd/mm/aaaa): ")

nome2 = input("Nome da segunda pessoa: ")
data2_str = input("Data de nascimento (dd/mm/aaaa): ")

data1 = datetime.datetime.strptime(data1_str, "%d/%m/%Y")
data2 = datetime.datetime.strptime(data2_str, "%d/%m/%Y")

if data1 < data2:
    print(nome1, "é a pessoa mais velha.")
elif data2 < data1:
    print(nome2, "é a pessoa mais velha.")
else:
    print("As duas pessoas têm a mesma idade.")