# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

def calcular():
    operacao = input("Digite a operação (+, -, *, /): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = 0

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Operação inválida. Por favor, escolha entre +, -, *, /."
    return f"O resultado de {num1} {operacao} {num2} é: {resultado}"
