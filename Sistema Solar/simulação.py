import pygame
import math
pygame.init()

largura, altura = 730, 730
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Simulação do Sistema Solar")

branco = (255, 255, 255)
amarelo = (255, 255, 0)
azul = (100, 149, 237)
vermelho = (255, 0, 0)
cinza_escuro = (80, 78, 81)

class Planeta:
    UA = 149.6e6 * 1000
    G = 6.67428e-11
    ESCALA = 200 / UA       # 1UA = 100 pixels
    TIMESTEP = 3600 * 24    # 1 dia

    def __init__(self, x, y, raio, cor, massa):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.massa = massa

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
         
        self.x_vel = 0
        self.y_vel = 0

    def desenhar(self, janela):
        x = self.x * self.ESCALA + largura / 2
        y = self.y * self.ESCALA + altura / 2
        pygame.draw.circle(janela, self.cor, (x, y), self.raio)


def main():
    run = True
    relógio = pygame.time.Clock()

    sol = Planeta(0, 0, 30, amarelo, 1.98892 * 10**30)
    sol.sol = True

    mercurio = Planeta(0.387 * Planeta.UA, 0, 8, cinza_escuro, 3.30 * 10**23)

    venus = Planeta(0.723 * Planeta.UA, 0, 14, branco, 4.8685 * 10**24)

    terra = Planeta(-1 * Planeta.UA, 0, 16, azul, 5.9742 * 10**24)

    marte = Planeta(-1.524 * Planeta.UA, 0, 12, vermelho, 6.39 * 10**23)

    planetas = [sol, mercurio, venus, terra, marte]

    while run:
        relógio.tick(60)
        #janela.fill(branco)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planeta in planetas:
            planeta.desenhar(janela)
        
        pygame.display.update()

    pygame.quit(janela)

main()