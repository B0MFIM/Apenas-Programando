anos = 0

while True:
    tam_inicial = int(input("População Inicial: "))
    if tam_inicial < 9:
        continue
    else:
        break

while True:
    tam_final = int(input("População Final: "))
    if tam_final < tam_inicial:
        continue
    else:
        break

while tam_inicial < tam_final:
    tam_inicial = tam_inicial + (tam_inicial / 3) - (tam_inicial / 4)
    anos += 1

    if tam_inicial >= tam_final:
        break

print(f"Anos: {anos}")