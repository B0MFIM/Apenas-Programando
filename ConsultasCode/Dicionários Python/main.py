emails_gerentes = {
    "Iguatemi": "iguatemi@gmail.com",
    "Plaza": "plaza@gmail.com",
    "Barra": "barra@gmail.com"
}
print(emails_gerentes["Iguatemi"])

# ADICIONANDO UM ITEM
emails_gerentes["Leblon"] = "leblon@gmail.com"

# DECOBRI TODOS OS SHOPPINGS:
 # Forma 1: Fazer um FOR
for shopping in emails_gerentes:
    print(shopping)

 # Forma 2: dicionário.keys()
print(emails_gerentes.keys())

# DECOBRI TODOS OS EMAILS DOS SHOPPINGS:
 # Forma 1: Fazer um FOR
for shopping in emails_gerentes:
    email = emails_gerentes[shopping]
    print(email)

 # Forma 2: dicionário.values()
print(emails_gerentes.values())

# REMOVENDO UM ITEM
emails_gerentes.pop("Leblon")
print(emails_gerentes)

# VERIFICAR EXISTÊNCIA
if "Leblon" in emails_gerentes:
    print("existe")
else:
    print("Não existe")