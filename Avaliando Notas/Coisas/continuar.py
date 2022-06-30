# Definição

def continuar():
    """
    NOME: 
    continuar -> faz codagem para dar continuidade a um programa 
    """
    while True:
        c = str(input("Deseja continuar? [S/N] ")).upper().strip()
        if c == "S":
            c = True
            break
        elif c == "N":
            c = False
            break
        else:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            continue
    
    return c