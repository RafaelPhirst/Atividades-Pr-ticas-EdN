# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nomeProduto = input("Nome do produto: ")
precoOriginal = float(input("Preço origianal: R$ "))
porcentDesc = float(input("Porcentagem de desconto: "))

desconto = precoOriginal * (porcentDesc / 100)
precoFinal = precoOriginal - desconto
print("========================")
print(nomeProduto)
print("Valor do desconto: R$ ", desconto)
print("Preço final: R$ ", precoFinal)