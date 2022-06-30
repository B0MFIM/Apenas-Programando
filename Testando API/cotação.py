import requests

cotações = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotações = cotações.json()
cotação_dolar = cotações["USDBRL"]["bid"]
cotação_euro = cotações["EURBRL"]["bid"]
print(f"A cotação atual do Dolar é de: {cotação_dolar}")
print(f"A cotação atual do EURO é de: {cotação_euro}")