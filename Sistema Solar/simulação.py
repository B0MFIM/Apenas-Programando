import pygame
import math
pygame.init()

largura, altura = 600, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Simulação do Sistema Solar")

branco = (255, 255, 255)

class Planeta:
    UA = 149.6e6 * 1000
    G = 6.67428e-11
    ESCALA = 250 / UA       # 1UA = 100 pixels
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


def main():
    run = True
    relógio = pygame.time.Clock()

    while run:
        relógio.tick(60)
        #janela.fill(branco)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

main()