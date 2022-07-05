from Canecas.caneca import Caneca

# Criando a Classe Filha
class Caneca_Londrina(Caneca):
    def __init__(self):
        super().__init__("Caneca Londrina", "Cidade de Londres", "Branca")
        self.bebida = "Chá"
        self.preço = 29.90

    def extras(self):
        print("Como bônus você ganha uma colher de chá")

    def beber(self):
        self.status = "Vazia"
        return f"Tá na hora do chá das 5"