# 3- Calculadora de Volume
# * Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

# * Comprimento: 12 cm
# * Largura: 14 cm
# * Altura: 20 cm
# O programa deve calcular o volume e exibir o resultado em cm³.

comp = int(input("Comprimento: "))
larg = int(input("Largura: "))
alt = int(input("Altura: "))

vol  = comp * larg * alt

print("O volume do retângulo é de: ", vol, "cm³")