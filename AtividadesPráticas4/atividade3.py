# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança, a - deve ter pelo menos 8 caracteres, b - deve conter pelo menos um número.

def verificar_senha():
    senha = input("Digite a senha: ")

    if len(senha) < 8:
        return "Senha inválida. Deve ter pelo menos 8 caracteres."
    
    if not any(char.isdigit() for char in senha):
        return "Senha inválida. Deve conter pelo menos um número."

    return "Senha válida."