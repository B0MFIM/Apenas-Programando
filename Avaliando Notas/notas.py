# Definições
def main():
    # Avaliação Normal
    for c in range(1, 2+1):
        nota = float(input(f"Digite a nota da {c}º avaliação: "))
        notas.append(nota)

    # Avaliação Optativa
    fezOpt = str(input(f"O Aluno fez a Optativa? [S/N] ")).upper().strip()
    if fezOpt == "S":
        nota = float(input(f"Digite a nota da Optativa: "))
    elif fezOpt == "N":
        nota = -1
    else:
        print("Valor Inválido")

    # Calcular Média do Semestre
    if notas[0] < nota and notas[0] < notas[1]:
        media = (nota + notas[1]) / 2
    elif notas[1] < nota and notas[1] < notas[0]:
        media = (notas[0] + nota) / 2
    else:
        media = (notas[0] + notas[1]) / 2
        
    # Exibir Situação
    if media >= 6:
        print("O Aluno foi APROVADO!!")
    elif media <= 3:
        print("O Aluno foi REPROVADO!!")
    elif 3 < media < 6:
        print("O Aluno está de EXAME FINAL!!")


# Principal
notas = list()
main()
