import pandas
from flask import Flask, jsonify

app = Flask(__name__)

# Construir Funcionalidades
@app.route("/")
def homepage():
    return "A API está no ar"

@app.route("/pegar_vendas")
def pegar_vendas():
    tabela = pandas.read_csv("C:\\Users\\bomfi\\OneDrive\\Documentos\\MeusProjetos\\Apenas-Programando\\Testando-API\\advertising.csv")
    total_vendas = tabela["Vendas"].sum()
    resposta = {"total vendas": total_vendas}
    return jsonify(resposta)


# Rodar a nossa API
app.run()