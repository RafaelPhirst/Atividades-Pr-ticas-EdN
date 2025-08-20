# 4 - Crie um programa que consulte a cotação atual de uma moeda
# estrangeira em relação ao Real Brasileiro (BRL). O usuário
# deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo
# da cotação, além da data e hora da última atualização. Utilize
# a API da AwesomeAPI para obter os dados de cotação.

import requests
from datetime import datetime

def formatar_valor(valor_str):

  try:
    valor_float = float(valor_str)
    return f"R$ {valor_float:.4f}"
  except (ValueError, TypeError):
    return "Valor inválido"

def consultar_cotacao(codigo_moeda):

  codigo_moeda_limpo = codigo_moeda.strip().upper()

  if not codigo_moeda_limpo:
    print("❌ Erro: O código da moeda não pode ser vazio.")
    return

  url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda_limpo}-BRL"
  print(f"\nBuscando cotação para {codigo_moeda_limpo}-BRL...")

  try:
    response = requests.get(url)

    response.raise_for_status()

    dados = response.json()

    chave_api = f"{codigo_moeda_limpo}BRL"

    if chave_api in dados:
      cotacao = dados[chave_api]

      nome_moeda = cotacao.get('name', 'Nome não disponível')
      valor_atual = cotacao.get('bid', 'N/A')
      valor_maximo = cotacao.get('high', 'N/A')
      valor_minimo = cotacao.get('low', 'N/A')
      data_atualizacao = cotacao.get('create_date', 'N/A')

      print("\n--- ✅ Cotação Encontrada ---")
      print(f"Moeda: {nome_moeda}")
      print(f"Valor Atual (Compra): {formatar_valor(valor_atual)}")
      print(f"Máxima do Dia:        {formatar_valor(valor_maximo)}")
      print(f"Mínima do Dia:        {formatar_valor(valor_minimo)}")
      print(f"Última Atualização:   {data_atualizacao}")

    else:
      print("❌ Erro: A resposta da API não continha os dados da cotação.")

  except requests.exceptions.HTTPError as http_err:
    if http_err.response.status_code == 404:
      print(f"❌ Erro: A moeda '{codigo_moeda_limpo}' não foi encontrada ou é inválida.")
    else:
      print(f"❌ Erro HTTP: {http_err}")
  except requests.exceptions.RequestException as req_err:
    print(f"❌ Erro de conexão com a API: {req_err}")

if __name__ == "__main__":
  print("--- Consulta de Cotação de Moedas ---")
  codigo = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ")
  consultar_cotacao(codigo)