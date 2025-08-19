# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

try:
    ano = int(input("Por favor, digite um ano para verificar (ex: 2024): "))

    if ano > 0:
        if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
            print(f"Sim, o ano {ano} é um ano bissexto.")
        else:
            print(f"Não, o ano {ano} não é um ano bissexto.")
    else:
        print("Por favor, insira um ano válido (número positivo).")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro para o ano.")