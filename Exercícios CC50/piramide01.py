# Recebendo um número inteiro do usuário
while True:
    try:
        largura = int(input("Tamanho da Pirâmide [1 - 8]: "))
    except:
        print("< ERRO > Valor Inválido < ERRO >")
        continue
    else:
        if largura < 1:
            print("< ALERTA > Insira um valor acima de Zero < ALERTA >")
            continue
        elif largura > 8:
            print("< ALERTA > Insira um valor abaixo de nove < ALERTA >")
            continue
        else:
            break

# Exibir piramide
for coluna in range(0, largura):
    for linha in range(0, largura):
        if (coluna + linha < largura - 1):
            print(" ", end="")
        else:
            print("#", end="")
    print()