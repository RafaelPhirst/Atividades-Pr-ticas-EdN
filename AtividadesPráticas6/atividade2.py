# 2 - Crie um programa que gera um perfil de usuário aleatório usando a
# API 'Random User Generator'. O programa deve exibir o nome, email e
# país do usuário gerado."

import requests

def gerar_usuario_aleatorio():
  """
  Busca um usuário aleatório na API Random User Generator e exibe seus dados.
  """
  url = "https://randomuser.me/api/"

  print("Gerando um novo perfil de usuário, aguarde...")

  try:
    response = requests.get(url)

    response.raise_for_status()

    dados = response.json()

    usuario = dados['results'][0]

    primeiro_nome = usuario['name']['first']
    ultimo_nome = usuario['name']['last']
    nome_completo = f"{primeiro_nome} {ultimo_nome}"

    email = usuario['email']
    pais = usuario['location']['country']

    print("\n--- ✅ Perfil de Usuário Gerado ---")
    print(f"👤 Nome: {nome_completo}")
    print(f"📧 Email: {email}")
    print(f"🌍 País: {pais}")

  except requests.exceptions.RequestException as e:
    print(f"❌ Erro ao se conectar com a API: {e}")
  except (KeyError, IndexError):
    print("❌ Erro: Não foi possível extrair os dados do usuário. O formato da resposta da API pode ter mudado.")

if __name__ == "__main__":
  gerar_usuario_aleatorio()