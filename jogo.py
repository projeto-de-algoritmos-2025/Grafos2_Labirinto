import pygame
import random
import sys

# Inicialização do pygame 
pygame.init()


TAMANHO_CELULA = 35
LINHAS = 15
COLUNAS = 15
LARGURA = COLUNAS * TAMANHO_CELULA
ALTURA = LINHAS * TAMANHO_CELULA
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto: Prim e Kruskal")

# Configurações do nosso jogo 
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

DIRECOES = {
    "CIMA": (0, -1),
    "BAIXO": (0, 1),
    "ESQUERDA": (-1, 0),
    "DIREITA": (1, 0)
}
INVERSO = {
    "CIMA": "BAIXO",
    "BAIXO": "CIMA",
    "ESQUERDA": "DIREITA",
    "DIREITA": "ESQUERDA"
}

# Classe para a criação das celulas 
class Celula:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paredes = {"CIMA": True, "BAIXO": True, "ESQUERDA": True, "DIREITA": True}
        self.visitada = False
        self.pai = self

    def desenhar(self, tela):
        x = self.x * TAMANHO_CELULA
        y = self.y * TAMANHO_CELULA
        if self.paredes["CIMA"]:
            pygame.draw.line(tela, BRANCO, (x, y), (x + TAMANHO_CELULA, y))
        if self.paredes["BAIXO"]:
            pygame.draw.line(tela, BRANCO, (x, y + TAMANHO_CELULA), (x + TAMANHO_CELULA, y + TAMANHO_CELULA))
        if self.paredes["ESQUERDA"]:
            pygame.draw.line(tela, BRANCO, (x, y), (x, y + TAMANHO_CELULA))
        if self.paredes["DIREITA"]:
            pygame.draw.line(tela, BRANCO, (x + TAMANHO_CELULA, y), (x + TAMANHO_CELULA, y + TAMANHO_CELULA))