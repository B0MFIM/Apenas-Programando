# Definição Principal
def main():
    # Recebendo um número inteiro do usuário
    while True:
        try:
            largura = int(input("Tamanho da Piramide [1 - 8]: "))
        except:
            print("< ERRO > Valor Inválido < ERRO >")
            continue
        else:
            if largura < 1:
                print("< ALERTA > Insira um valor entre 1 - 8 < ALERTA >")
                continue
            elif largura > 8:
                print("< ALERTA > Insira um valor entre 1 - 8 < ALERTA >")
                continue
            else:
                break
    
    # Exibir Piramide
    for contador in range(0, largura):
        if contador < largura:
            imprimir_piramide(largura, contador+1)

# Definição para a Piramide
def imprimir_piramide(largura, numero):
    # Imprimir os Espaços quando necessário
    for espaço in range(0, largura):
        if espaço < largura - numero:
            print(" ", end="")

    # Imprimir blocos à esquerda
    for blocos_1 in range(0, largura):
        if blocos_1 < numero:
            print("#", end="")

    # Separar Colunas
    print(" ", end="")

    # Imprimir blocos à direita
    for blocos_2 in range(0, largura):
        if blocos_2 < numero:
            print("#", end="")

    # Quebra de linha
    print()


# Inicializando
main()