# Criando a Classe Pai
class Caneca:
    formato = "Cilindrico com Alça lateral"

    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = "Cheia"
        self.preço = 24.90
        self.__preço_fabrica = 15
    
    def beber(self):
        self.status = "Vazia"
        return f"É da {self.nome} que eu estou bebendo "

    def encher(self):
        self.status = "Cheia"
        return f"Estou enchendo a {self.nome}"