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
    


# Principal
notas = list()
main()
