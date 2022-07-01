import pandas as pd

# Importar a base de dados
tabela_vendas = pd.read_excel("C:\\Users\\bomfi\\OneDrive\\Documentos\\MeusProjetos\\Apenas-Programando\\Sistema de Lojas\\Vendas.xlsx")


# Visualizar a base de dados
pd.set_option("display.max_columns", None)


# Calcular o faturamento por loja
faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento)


# Calcular o quantidade de produtos vendidos por loja
quantidade = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
print(quantidade)


# Calcular o ticket médio por produto em cada loja
ticket_media = faturamento["Valor Final"] / quantidade["Quantidade"]
print(ticket_media)


# Enviar um Email com um relatório