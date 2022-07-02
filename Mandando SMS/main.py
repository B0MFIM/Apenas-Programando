import pandas as pd
from twilio.rest import Client

# Conectando-se na conta twilio
account_sid = "XXXxxxXXXxxxXXX" # Your Account SID
auth_token  = "xxxXXXxxxXXX"    # Your Auth Token
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos exel
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"C:\\Users\\bomfi\\OneDrive\\Documentos\\MeusProjetos\\Apenas-Programando\\Mandando SMS\\{mes}.xlsx")

    # Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]

        # Enviar um SMS
        message = client.messages.create(
            to="+123456789000", 
            from_="+123456789000",
            body=f"No mês de {mes}, bateram a meta: Vendedor: {vendedor} - Vendas: {vendas}")
        print(message.sid)