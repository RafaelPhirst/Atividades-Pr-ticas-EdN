# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

def registrar_notas():
    notas = []
    while True:
        nota = input("Digite a nota do aluno (ou 'sair' para finalizar): ")
        if nota.lower() == 'sair':
            break
        try:
            nota_float = float(nota)
            if 0 <= nota_float <= 10:
                notas.append(nota_float)
            else:
                print("Nota inválida. Deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    if notas:
        media = sum(notas) / len(notas)
        return f"A média da turma é: {media:.2f}"
    else:
        return "Nenhuma nota registrada."