valor = input("Digite um valor: ")

# A função int() dará erro se o valor digitado for decimal (ex: 3.5) ou texto (ex: palavra).
print("Saída int():", int(valor))

# A função float() dará erro se o valor digitado for um texto não numérico (ex: palavra).
print("Saída float():", float(valor))

# A função bool() raramente dá erro. Qualquer string preenchida (mesmo a palavra "False") resulta em True.
print("Saída bool():", bool(valor))