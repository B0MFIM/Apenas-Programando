from Canecas.caneca_londres import Caneca_Londrina
from Canecas.caneca_bylearn import Caneca_ByLearn

# Criando os Objetos
caneca_londres = Caneca_Londrina()
caneca_bylearn = Caneca_ByLearn()

# Executando
print(caneca_bylearn.beber())
print(caneca_londres.beber())

print("VALORES EM REAIS:")
print(f"A {caneca_londres.nome} é R${caneca_londres.preço:.2f}")
print(f"A {caneca_bylearn.nome} é R${caneca_bylearn.preço:.2f}")