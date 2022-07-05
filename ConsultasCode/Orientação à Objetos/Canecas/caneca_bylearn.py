from Canecas.caneca import Caneca

# Criando a Classe Filha
class Caneca_ByLearn(Caneca):
    def __init__(self):
        super().__init__("Caneca ByLearn", "Foguete ByLearn", "Branca")
        self.bebida = "Café"
    
    def beber(self):
        return super().beber() + f"{self.bebida}"