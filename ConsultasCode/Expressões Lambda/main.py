# Usando Lambda:
preço = 500

def calcular_imposto1(preço):
    return preço * 0.3
    
calcular_imposto2 = lambda x: x * 0.3

print(f"Usando def: {calcular_imposto1(preço)}")
print(f"Usando lambda: {calcular_imposto2(preço)}")

preços = [100, 500, 10, 25]
impostos = list(map(lambda x: x*0.3, preços))
print(f"Lambda na lista: {impostos}")