# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
# gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        return 0.0
    valor_calculado_gorjeta = (valor_conta * porcentagem_gorjeta) / 100.0
    return valor_calculado_gorjeta

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        return 0.0
    valor_calculado_gorjeta = (valor_conta * porcentagem_gorjeta) / 100.0
    return valor_calculado_gorjeta

conta_do_jantar = 250.75
percentual_servico = 10.0

gorjeta_a_pagar = calcular_gorjeta(conta_do_jantar, percentual_servico)

valor_total_com_gorjeta = conta_do_jantar + gorjeta_a_pagar


print(f"Valor da conta: R$ {conta_do_jantar:.2f}")
print(f"Porcentagem da gorjeta: {percentual_servico}%")
print("---------------------------------")

print(f"Valor da gorjeta: R$ {gorjeta_a_pagar:.2f}")
print(f"Valor total a pagar: R$ {valor_total_com_gorjeta:.2f}")

print("\n--- Outro Teste ---")
gorjeta_almoco = calcular_gorjeta(80.0, 12.0)
print(f"Gorjeta para uma conta de R$ 80.00 com 12% de serviço: R$ {gorjeta_almoco:.2f}")