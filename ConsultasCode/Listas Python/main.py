lista_compras = ["banana", "maçã", "laranja"]
print(lista_compras)
print(lista_compras[1])

# Add novo item ao fim da lista
lista_compras.append("mamão")
print(lista_compras)

# Add novo item em uma posiçãoda lista
lista_compras.insert(1, "chocolate")
print(lista_compras)

# Deletar um Item
del lista_compras[0]
print(lista_compras)

# Removendo um Item
lista_compras.remove("laranja")
print(lista_compras)

# Movendo para outra lista
lista_compras.append("carro")
print(lista_compras)

lista_sonhos = []
sonho = lista_compras.pop(-1)
lista_sonhos.append(sonho)
print(lista_compras)
print(lista_sonhos)

# Tarefas
"""tarefas = []
tarefa = input("Insira uma tarefa: ")
tarefas.append(tarefa)
while tarefa != "": 
    tarefa = input("Insira uma tarefa: ")
    tarefas.append(tarefa)
tarefas.remove("")
print(tarefas)
print(tarefas[:-1])
print(tarefas[2:])
print(tarefas[1:4])"""

# Lojas
lojas = ["Rio de Janeiro", "São Paulo", "Curitiba"]
faturamento = [10000, 20000, 50000]
faturamento.sort() # para inverter -> sort(reverse=True)
print(lojas)
print(faturamento)
resultados = list()
for i in range(3):
    tupla = (lojas[i-1], faturamento[i-1])
    resultados.append(tupla)
print(resultados)
print(resultados[1][1])