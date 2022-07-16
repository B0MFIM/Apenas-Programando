import pygame
import math
pygame.init()

# DEFININDO A INTERFACE (JANELA) DE EXIBIÇÃO DA SIMULAÇÃO
largura, altura = 730, 730                                  # Tamanho da interface 
janela = pygame.display.set_mode((largura, altura))         # Interface do pygame
pygame.display.set_caption("Simulação do Sistema Solar")    # Título da interface

# DEFININDO CORES (RGB)
branco = (255, 255, 255)
amarelo = (255, 255, 0)
azul = (100, 149, 237)
vermelho = (255, 0, 0)
cinza_escuro = (80, 78, 81)

# DEFININDO FONTE DE TEXTO NA INTERFACE
fonte = pygame.font.SysFont("comicsans", 16)

# DEFININDO O OBJETO "PLANETA"
class Planeta:
    UA = 149.6e6 * 1000     # Unidade Astronomica (UA) convertida para Km
    G = 6.67428e-11         # Constante gravitacional (aceleração da gravidade)
    ESCALA = 200 / UA       # Escala apropriada pra interface (1UA = 100 pixels)
    TIMESTEP = 3600 * 24    # 1 dia - Representação de Tempo na simulação

    def __init__(self, x, y, raio, cor, massa):
        """
        NOME: __init__
        PARÂMETROS:
            self  -> referenciador de atributos/métodos
            x, y  -> posição do planeta na interface
            raio  -> raio do planeta (planetas redondos obviamente :P)
            cor   -> cor do planeta (detalhe do planeta)
            massa -> massa do planeta (para calcular a atração)
        """
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.massa = massa

        self.orbita = []            # Desenhar pontos percorrido pelo planeta
        self.sol = False            # Para não desenharmos a orbita do sol
        self.distancia_do_sol = 0   # Distância do planeta ao sol
         
        self.x_vel = 0  # Direção x da velocidade (horizontal)
        self.y_vel = 0  # Direção y da velocidade (vertical)

    def desenhar(self, janela):
        """
        NOME: desenhar
        PARÂMETROS:
            self   -> referenciador de atributos/métodos
            janela -> interface para desenhar o objeto (planeta)
        """
        x = self.x * self.ESCALA + largura / 2  # Posição da "horizontal central" na interface
        y = self.y * self.ESCALA + altura / 2   # Posição da "vertical central" na interface

        # "CALCULANDO" A ORBITA DOS PLANETAS
        if len(self.orbita) > 2:
            # SABER AS COORDENADAS x E y dos pontos
            atualizar_pontos = [] # Lista de pontos atualizados
            for ponto in self.orbita:
                x, y = ponto
                x = x * self.ESCALA + largura / 2   # Posição X do ponto na interface
                y = y * self.ESCALA + altura / 2    # Posição Y do ponto na interface
                atualizar_pontos.append((x, y))     # Adicionar cordenadas (x, y) na lista

            # "DESENHAR" A LINHA ORBITAL DO PLANETA
            pygame.draw.lines(janela, self.cor, False, atualizar_pontos, 2)

        # "DESENHAR" UM CIRCULO NA JANELA, EDITANDO COR, POSIÇÃO E O RAIO
        pygame.draw.circle(janela, self.cor, (x, y), self.raio)

        if not self.sol:
            distancia_texto = fonte.render(f"{round(self.distancia_do_sol/1000, 1)}Km", 1, branco)
            janela.blit(distancia_texto, (x - distancia_texto.get_width()/2, y - distancia_texto.get_width()/2))

    def atração(self, outro):
        """
        NOME: atração
        PARÂMETROS: 
            self  -> referenciador de atributos/métodos
            outro -> referenciador de atributos/métodos (os planetas)
        """
        # CALCULANDO A DISTÂNCIA ENTRE OS DOIS OBJETOS
        outro_x, outro_y = outro.x, outro.y
        distancia_x = outro_x - self.x
        distancia_y = outro_y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)

        # DETERMINANDO SE O OUTRO OBJETO É O SOL, ARMAZENANDO-O EM UMA PROPRIEDADE
        if outro.sol:
            self.distancia_do_sol = distancia

        # CALCULAR A FORÇA DE ATRAÇÃO, E DIVIDIR ESSA FORÇA EM 2 COMPONENTES (x, y)
        força = self.G * self.massa * outro.massa / distancia**2    # Força da linha reta
        theta = math.atan2(distancia_y, distancia_x)                # Calculando ângulo Theta
        força_x = math.cos(theta) * força                           # Força na linha x
        força_y = math.sin(theta) * força                           # Força na linha y
        return força_x, força_y                                     # Retornando valores

    def atualizar_posição(self, planetas):
        """
        NOME: atualizar_posição
        PARÂMETROS:
            self     -> referenciador de atributos/métodos
            planetas -> receber planetas para calcular força de atração e velocidade entre eles
        """
        # OBTENDO AS FORÇAS TOTAIS EXERCIDAS NO OBJETO "PLANETA"
        total_fx = total_fy = 0
        for planeta in planetas:
            if self == planeta:
                continue
            fx, fy = self.atração(planeta)
            total_fx += fx
            total_fy += fy
        
        # CALCULAR A VELOCIDADE x E y 
        self.x_vel += total_fx / self.massa * self.TIMESTEP
        self.y_vel += total_fy / self.massa * self.TIMESTEP

        # ATUALIZAR A POSIÇÃO x E y USANDO A VELOCIDADE E O TIMESTEP(TEMPO)
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbita.append((self.x, self.y))    # Dados anexados da posição 'x' e 'y' da orbita

def main():
    run = True  # loop infinito
    relógio = pygame.time.Clock() # Estabelecer taxa de frames pra simulação

    sol = Planeta(0, 0, 30, amarelo, 1.98892 * 10**30) # "Desenhando" o Sol
    sol.sol = True # Para não traçarmos a orbita do sol e nem sua distância 

    mercurio = Planeta(0.387 * Planeta.UA, 0, 8, cinza_escuro, 3.30 * 10**23) # "Desenhando" Mercúrio
    mercurio.y_vel = -47.4 * 1000 # Velocidade (direção Y "negativo") de mercúrio

    venus = Planeta(0.723 * Planeta.UA, 0, 14, branco, 4.8685 * 10**24) # "Desenhando" Venus
    venus.y_vel = -35.02 * 1000 # Velocidade (direção Y "negativo") de venus

    terra = Planeta(-1 * Planeta.UA, 0, 16, azul, 5.9742 * 10**24) # "Desenhando" a Terra
    terra.y_vel = 29.783 * 1000 # Velocidade (direção Y) da terra

    marte = Planeta(-1.524 * Planeta.UA, 0, 12, vermelho, 6.39 * 10**23) # "Desenhando" Marte
    marte.y_vel = 24.077 * 1000 # Velocidade (direção Y) de marte

    planetas = [sol, mercurio, venus, terra, marte] # Lista dos Planetas

    while run:
        relógio.tick(60) # Frames atualizados (60 frames/segundo)
        janela.fill((0, 0, 0)) # Atualizando background da interface

        # PROCESSANDO TODOS OS EVENTOS PYGAME
        for event in pygame.event.get():
            # PROCESSANDO EVENTO quit DO PYGAME, PARA FECHARMOS A INTERFACE (NOSSA JANELA)
            if event.type == pygame.QUIT:
                run = False # Quebrar o loop

        # "DESENHAR" OBJETOS DENTRO DA LISTA planetas NA JANELA
        for planeta in planetas:
            planeta.atualizar_posição(planetas) # Atualizando posição dos planetas na interface
            planeta.desenhar(janela)            # Desenhando o planeta na interface
        
        # ATUALIZAR A INTERFACE
        pygame.display.update()

    # SAINDO DA INTERFACE (NOSSA JANELA)
    pygame.quit(janela)

# CHAMANDO A FUNÇÃO MAIN
main()