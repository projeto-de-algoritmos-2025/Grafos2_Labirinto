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

# Funções de união (Kruskal)
def encontrar(celula):
    if celula.pai != celula:
        celula.pai = encontrar(celula.pai)
    return celula.pai

def unir(c1, c2):
    raiz1 = encontrar(c1)
    raiz2 = encontrar(c2)
    if raiz1 != raiz2:
        raiz2.pai = raiz1
        return True
    return False

# Geração com Prim
def criar_labirinto_prim():
    grade = [[Celula(x, y) for y in range(LINHAS)] for x in range(COLUNAS)]
    celula_inicial = grade[0][0]
    celula_inicial.visitada = True
    paredes = []

    def adicionar_paredes(c):
        for dir, (dx, dy) in DIRECOES.items():
            nx, ny = c.x + dx, c.y + dy
            if 0 <= nx < COLUNAS and 0 <= ny < LINHAS:
                paredes.append((c.x, c.y, dir))

    adicionar_paredes(celula_inicial)

    while paredes:
        x, y, direcao = random.choice(paredes)
        paredes.remove((x, y, direcao))
        dx, dy = DIRECOES[direcao]
        nx, ny = x + dx, y + dy

        if 0 <= nx < COLUNAS and 0 <= ny < LINHAS and not grade[nx][ny].visitada:
            grade[x][y].paredes[direcao] = False
            grade[nx][ny].paredes[INVERSO[direcao]] = False
            grade[nx][ny].visitada = True
            adicionar_paredes(grade[nx][ny])
    return grade

# Geração com Kruskal
def criar_labirinto_kruskal():
    grade = [[Celula(x, y) for y in range(LINHAS)] for x in range(COLUNAS)]
    paredes = []

    for x in range(COLUNAS):
        for y in range(LINHAS):
            for dir, (dx, dy) in DIRECOES.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < COLUNAS and 0 <= ny < LINHAS:
                    if (x, y, dir) not in paredes:
                        paredes.append((x, y, dir))

    random.shuffle(paredes)

    for x, y, direcao in paredes:
        dx, dy = DIRECOES[direcao]
        nx, ny = x + dx, y + dy
        if unir(grade[x][y], grade[nx][ny]):
            grade[x][y].paredes[direcao] = False
            grade[nx][ny].paredes[INVERSO[direcao]] = False
    return grade


