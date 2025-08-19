# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

def calcular_preco_final(preco_original, percentual_desconto):
 
    valor_desconto = (preco_original * percentual_desconto) / 100.0
    
    preco_final = preco_original - valor_desconto
    
    valor_desconto_arredondado = round(valor_desconto, 2)
    preco_final_arredondado = round(preco_final, 2)
    
    return valor_desconto_arredondado, preco_final_arredondado


if __name__ == "__main__":
    print("--- Calculadora de Preço com Desconto ---")
    
    try:
        preco_str = input("Digite o preço original do produto (ex: 99.90): R$ ")
        percentual_str = input("Digite o percentual de desconto (ex: 15): % ")
        
        preco = float(preco_str)
        percentual = float(percentual_str)
        
        if preco < 0 or percentual < 0:
            print("\nErro: Os valores de preço e desconto não podem ser negativos.")
        else:
            desconto, final = calcular_preco_final(preco, percentual)
            
            print("\n--- Resultado do Cálculo ---")
            print(f"Preço Original: R$ {preco:.2f}")
            print(f"Desconto de {percentual}%: R$ {desconto:.2f}")
            print("-----------------------------")
            print(f"Preço Final: R$ {final:.2f}")
            
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos para o preço e o desconto.")