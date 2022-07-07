lista_preços = [500, 1500, 2000, 100, 25]

# caso 1, normal
nova_lista_preços = []
for preço in lista_preços:
    nova_lista_preços.append(preço*2)
print(nova_lista_preços)

# caso 2, com list comprehesion
nova_lista_preços_2 = [preço * 2 for preço in lista_preços]
print(nova_lista_preços_2)