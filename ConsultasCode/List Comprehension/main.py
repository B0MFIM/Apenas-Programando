lista_preços = [500, 1500, 2000, 100, 25]

# caso 1, normal
nova_lista_preços = []
for preço in lista_preços:
    nova_lista_preços.append(preço*2)
print(nova_lista_preços)

# caso 1, com list comprehesion
nova_lista_preços_2 = [preço * 2 for preço in lista_preços]
print(nova_lista_preços_2)


# caso 2, normal
imposto = []
for preço in lista_preços:
    if preço > 1000:
        imposto.append(preço * 0.5)
print(imposto)

# caso 2, com list comprehesion
imposto_2 = [preço * 0.5 for preço in lista_preços if preço > 1000]
print(imposto_2)