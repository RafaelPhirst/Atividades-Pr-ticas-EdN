# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

from datetime import datetime

def calcular_dias_vividos(data_nascimento_obj):
 
    hoje = datetime.now().date()
    
    if data_nascimento_obj > hoje:
        return None
        
    diferenca = hoje - data_nascimento_obj
    
    return diferenca.days

if __name__ == "__main__":
    print("--- Calculadora de Dias Vividos ---")
    
    while True:
        nascimento_str = input("Digite sua data de nascimento no formato DD/MM/AAAA: ")
        
        try:
            data_nascimento = datetime.strptime(nascimento_str, '%d/%m/%Y').date()
            
            dias = calcular_dias_vividos(data_nascimento)
            
            if dias is not None:
                print("\n--- Resultado ---")
                print(f"Até hoje, você viveu aproximadamente {dias} dias.")
                break 
            else:
                print("\nErro: A data de nascimento não pode ser uma data no futuro. Tente novamente.")

        except ValueError:
            print("\nErro: Formato de data inválido ou a data não existe (ex: 30/02).")
            print("Por favor, use o formato DD/MM/AAAA e tente novamente.\n")