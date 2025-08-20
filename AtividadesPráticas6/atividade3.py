# 3 - Desenvolva um programa que consulte informações de
# endereço a partir de um CEP fornecido pelo usuário, utilizando
# a API ViaCEP. O programa deve exibir o logradouro, bairro,
# cidade e estado correspondentes ao CEP consultado.

import requests

def consultar_cep(cep):
  
  cep_limpo = "".join(filter(str.isdigit, cep))

  if len(cep_limpo) != 8:
    print("❌ Erro: O CEP deve conter exatamente 8 dígitos.")
    return

  url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

  try:
    print(f"\nConsultando o CEP {cep_limpo}...")
    response = requests.get(url)
    response.raise_for_status() 
    dados_endereco = response.json()

    if dados_endereco.get('erro'):
      print(f"❌ CEP {cep} não foi encontrado.")
    else:
      print("\n--- ✅ Endereço Encontrado ---")
      print(f"CEP: {dados_endereco.get('cep', 'Não informado')}")
      print(f"Logradouro: {dados_endereco.get('logradouro', 'Não informado')}")
      print(f"Bairro: {dados_endereco.get('bairro', 'Não informado')}")
      print(f"Cidade: {dados_endereco.get('localidade', 'Não informado')}")
      print(f"Estado: {dados_endereco.get('uf', 'Não informado')}")

  except requests.exceptions.RequestException as e:
    print(f"❌ Ocorreu um erro de conexão: {e}")

if __name__ == "__main__":
  print("--- Consulta de Endereço por CEP ---")
  cep_usuario = input("Digite o CEP que deseja consultar: ")
  consultar_cep(cep_usuario)