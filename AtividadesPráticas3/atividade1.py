# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).

try:
    idade = int(input("Por favor, digite a sua idade: "))

    if idade < 0:
        print("Idade inválida. Por favor, insira um número positivo.")
    elif idade <= 12:
        categoria = "Criança"
        print(f"Com {idade} anos, você é classificado(a) como: {categoria}.")
    elif idade <= 17:
        categoria = "Adolescente"
        print(f"Com {idade} anos, você é classificado(a) como: {categoria}.")
    elif idade <= 59:
        categoria = "Adulto"
        print(f"Com {idade} anos, você é classificado(a) como: {categoria}.")
    else:
        categoria = "Idoso"
        print(f"Com {idade} anos, você é classificado(a) como: {categoria}.")
except ValueError:
    print("Erro: Por favor, digite um número válido para a idade.")