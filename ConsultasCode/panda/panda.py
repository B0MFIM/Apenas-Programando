# Praticando com Biblioteca Pandas:
import pandas as pd    

vendas_df = pd.read_excel("C:\\Users\\bomfi\\OneDrive\\Documentos\\MeusProjetos\\Apenas-Programando\\ConsultasCode\\panda\\Vendas.xlsx")
#print(vendas_df)                       # Execução da tabela
#print(vendas_df.head(10))              # Execução das 10 primeiras linhas da tabéla
#print(vendas_df.shape)                 # Execução rápida de uma grande tabela de dados
#print(vendas_df.describe())            # Execução de um "resumo geral" da tabéla
#print(vendas_df.loc[1:5])              # Pegar Linhas da Tabela
#print(vendas_df.loc[1, "Produto"])     # Pegar um valor específico

vendas_ns_df = vendas_df.loc[vendas_df["ID Loja"] == "Norte Shopping"]                                          # Pegar Linhas que correspondem a uma condição
vendas_ns_df = vendas_df.loc[vendas_df["ID Loja"] == "Norte Shopping", ["ID Loja", "Produto", "Quantidade"]]    # Pegar varias Linhas e Colunas usando o loc

produtos = vendas_df[["Produto", "ID Loja"]]            # Acessando algumas colunas da tabela

vendas_df["Comissão"] = vendas_df["Valor Final"]        # Criar coluna a partir de uma que existe
vendas_df.loc[:, "Imposto"] = 0                         # Criar coluna com valor padrão

vendas_dez_df = pd.read_excel("C:\\Users\\bomfi\\OneDrive\\Documentos\\MeusProjetos\\Apenas-Programando\\ConsultasCode\\panda\\Vendas - Dez.xlsx")
vendas_df = vendas_df.append(vendas_dez_df)             # Inserindo tabela de vendas de dezembro na tabela vendas < ALERTA - ".append from pandas" será removido futuramente - ALERTA >

vendas_df = vendas_df.drop("Imposto", axis=1)           # Deletando uma coluna da tabela
#vendas_df = vendas_df.dropna(how="all", axis=1)        # Deletar linhas e colunas completamentes vazias
#vendas_df = vendas_df.dropna()                         # Deletar linhas que possuem pelo menos 1 valor vazio

vendas_df["Comissão"] = vendas_df["Comissão"].fillna(vendas_df["Comissão"].mean())      # Preencher valores vazios (com média da coluna)
vendas_df = vendas_df.ffill()                                                           # Preencher valores vazio (com o último valor)

transações_loja = vendas_df["ID Loja"].value_counts()   # Contando valores da tabela

faturamento_produto = vendas_df[["Produto", "Valor Final"]].groupby("Produto").sum()    # Agrupando a coluna produtos e somando o valor final

gerentes_df = pd.read_excel("C:\\Users\\bomfi\\OneDrive\\Documentos\\MeusProjetos\\Apenas-Programando\\ConsultasCode\\panda\\Gerentes.xlsx")
vendas_df = vendas_df.merge(gerentes_df)                # Mesclando duas tabelas




print(vendas_df)