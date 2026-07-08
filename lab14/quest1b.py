def ola_genero(nome, genero):
    if genero.lower() == "feminino":
        return f"Olá {nome}, bem vinda!"
    elif genero.lower() == "masculino":
        return f"Olá {nome}, bem vindo!"
    else:
        return f"Olá {nome}, boas vindas!"
    

print(ola_genero("Leo", "Neutro"))
print(ola_genero("Mila", "feminino"))
print(ola_genero("Alan", "masculino"))