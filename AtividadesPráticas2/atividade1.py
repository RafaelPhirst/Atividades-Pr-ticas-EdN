# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valorReais = float(input("Valor em reais: R$ "))
taxaDolar = float(input("Taxa do dólar: R$ "))
taxaEuro = float(input("Taxa do euto: R$ "))

valorDolar = valorReais / taxaDolar
valorEuro = valorReais / taxaEuro
print("========================")
print(f"Valor em dólares: ${valorDolar:.2f}")
print(f"Valor em euros: €{valorEuro:.2f}")