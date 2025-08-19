# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

def verificar_palindromo(frase):
    
    texto_limpo = ''.join(char for char in frase.lower() if char.isalnum())

    if not texto_limpo:
        return "Não"

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"
    
palavra1 = "ovo"
print(f"A palavra '{palavra1}' é um palíndromo? {verificar_palindromo(palavra1)}")

frase1 = "Anotaram a data da maratona"
print(f"A frase '{frase1}' é um palíndromo? {verificar_palindromo(frase1)}")

frase2 = "Socorram-me, subi no onibus em Marrocos!"
print(f"A frase '{frase2}' é um palíndromo? {verificar_palindromo(frase2)}")

palavra2 = "python"
print(f"A palavra '{palavra2}' é um palíndromo? {verificar_palindromo(palavra2)}")

frase3 = "ola, mundo"
print(f"A frase '{frase3}' é um palíndromo? {verificar_palindromo(frase3)}")