# Laços FOR
lojas = ["Rio", "Paulo", "Belo", "Santa"]
for loja in lojas:
    print(loja)
print("=================")

for i in range(4):
    print(lojas[i])
print("=================")

for x in "Daniel":
    print(f"{x}", end="")
print()
print("=================")

# Laços WHILE
name = input("Insira um nome: ")
while name:
    name = input("Insira um nome: ")
print("=================")

while True:
    nome = input("Insira um nome: ")
    if nome == "":
        break
    else:
        continue
print("=================")