# 4- Calculadora de Preço Total
# * Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

# * Nome do produto: "Cadeira Infantil"
# * Preço unitário: R$ 12.40
# * Quantidade: 3
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

nome = str(input("Nome do produto: "))
preco = float(input("Preço Unitário: R$ "))
qtd = int(input("Quantidade: "))

preco_total = float(preco * qtd)

print("===============================Bo")

print("Nome do Produto: ", nome)
print("Preço Unitário: ", preco)
print("Quantidade: ", qtd)
print("Valor Total: ", preco_total)