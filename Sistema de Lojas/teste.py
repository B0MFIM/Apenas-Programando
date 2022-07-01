import pandas as pd
import win32com.client as win32

# Importar a base de dados
tabela_vendas = pd.read_excel("C:\\Users\\bomfi\\OneDrive\\Documentos\\MeusProjetos\\Apenas-Programando\\Sistema de Lojas\\Vendas.xlsx")


# Visualizar a base de dados
pd.set_option("display.max_columns", None)


# Calcular o faturamento por loja
faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()


# Calcular o quantidade de produtos vendidos por loja
quantidade = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()


# Calcular o ticket médio por produto em cada loja
ticket_media = (faturamento["Valor Final"] / quantidade["Quantidade"]).to_frame()


# Enviar um Email com um relatório
outlook = win32.Dispatch("outlook.application")
mail = outlook.CreateItem(0)
mail.To = "email@gmail.com"
mail.Subject = "Relatório de Vendas por Loja"
mail.HTMLBody = f"""
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja</p>

<p>Faturamento:</p>
{faturamento.to_html()}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_media.to_html()}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>

<p>Bomfim</p>
"""

mail.Send()
print("Email Enviado...")