# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

def celsius_para_fahrenheit(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """Converte uma temperatura de Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    """Converte uma temperatura de Celsius para Kelvin."""
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    """Converte uma temperatura de Kelvin para Celsius."""
    return kelvin - 273.15

try:
    valor_temp = float(input("Digite a temperatura: "))

    unidade_origem = input("Qual a unidade de origem? (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper().strip()

    unidade_destino = input("Para qual unidade deseja converter? (C, F, K): ").upper().strip()

    temp_em_celsius = 0
    if unidade_origem == 'C':
        temp_em_celsius = valor_temp
    elif unidade_origem == 'F':
        temp_em_celsius = fahrenheit_para_celsius(valor_temp)
    elif unidade_origem == 'K':
        temp_em_celsius = kelvin_para_celsius(valor_temp)
    else:
        print("Erro: Unidade de origem inválida. Use C, F ou K.")
        exit() 

    resultado_final = 0
    if unidade_destino == 'C':
        resultado_final = temp_em_celsius
    elif unidade_destino == 'F':
        resultado_final = celsius_para_fahrenheit(temp_em_celsius)
    elif unidade_destino == 'K':
        resultado_final = celsius_para_kelvin(temp_em_celsius)
    else:
        print("Erro: Unidade de destino inválida. Use C, F ou K.")
        exit() 
        
    print("\n--- Resultado da Conversão ---")
    print(f"{valor_temp:.2f}°{unidade_origem} é igual a {resultado_final:.2f}°{unidade_destino}")

except ValueError:
    print("Erro: O valor da temperatura deve ser um número.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")