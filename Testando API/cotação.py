import requests
import json

cotações = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotações = cotações.json()
print(cotações)