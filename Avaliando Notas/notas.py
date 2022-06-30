from Coisas import continuar

# Definições
def main():

    # Definindo uma lista para as notas
    notas = list()

    # Avaliação Normal
    while True:
        try:
            for c in range(1, 2+1):
                nota = float(input(f"Digite a nota da {c}º avaliação: "))
                notas.append(nota)
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            notas.clear()
            continue
        else:
            break

    # Avaliação Optativa
    while True:
        fezOpt = str(input(f"O Aluno fez a Optativa? [S/N] ")).upper().strip()
        if fezOpt == "S":
            nota = float(input(f"Digite a nota da Optativa: "))
            break
        elif fezOpt == "N":
            nota = -1
            break
        else:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            continue

    # Calcular Média do Semestre
    if notas[0] < nota and notas[0] <= notas[1]:
        media = (nota + notas[1]) / 2
    elif notas[1] < nota and notas[1] < notas[0]:
        media = (notas[0] + nota) / 2
    else:
        media = (notas[0] + notas[1]) / 2
        
    # Exibir Situação
    if media >= 6:
        print("O Aluno foi \033[0;35mAPROVADO!!\033[m")
    elif media <= 3:
        print("O Aluno foi \033[0;31mREPROVADO!!\033[m")
    elif 3 < media < 6:
        print("O Aluno está de \033[0;33mRECUPERAÇÃO!!\033[m")


# Principal
while True:
    main()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        break