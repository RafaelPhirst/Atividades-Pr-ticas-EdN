# 1 - Crie um programa que gera uma senha aleatória com o módulo
# random, utilizando caracteres especiais, possibilitando o
# usuário a informar a quantidade de caracteres dessa senha
# aleatória.

import random
import string

def gerar_senha(tamanho):

  caracteres = string.ascii_letters + string.digits + string.punctuation

  senha_temporaria = random.choices(caracteres, k=tamanho)

  return ''.join(senha_temporaria)


print("--- Gerador de Senhas Aleatórias ---")

try:
  tamanho_da_senha = int(input("Digite a quantidade de caracteres para a sua senha: "))

  if tamanho_da_senha > 0:
    senha_final = gerar_senha(tamanho_da_senha)

    print(f"\n✅ Sua senha aleatória é: {senha_final}")
  else:
    print("❌ Erro: Por favor, digite um número maior que zero.")

except ValueError:
  print("❌ Erro: Entrada inválida. Por favor, digite apenas um número.")