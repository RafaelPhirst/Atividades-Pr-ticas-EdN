# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

try:
    peso = float(input("Digite o seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

    if altura > 0:
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else: # Se o IMC for 30 ou maior
            classificacao = "Obeso"

        print("\n--- Resultado ---")
        print(f"O seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")

    else:
        print("Erro: A altura não pode ser zero. Por favor, insira um valor válido.")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos para o peso e a altura.")