import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)

# Definindo as dimensões da janela
largura_janela = 800
altura_janela = 600

# Definindo as dimensões e a velocidade do Pac-Man
pacman_tamanho = 30
pacman_velocidade = 2

# Definindo as dimensões e a velocidade das bolas
bola_tamanho = 10
bola_velocidade = 1

# Criando a janela do jogo
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Pac-Man")

# Definindo a posição inicial do Pac-Man
pacman_posicao = [largura_janela // 2, altura_janela // 2]

# Definindo a direção inicial do Pac-Man
pacman_direcao = [0, 0]

# Criando as bolas
bolas = []
num_bolas = 30

for _ in range(num_bolas):
    x = random.randint(0, largura_janela - bola_tamanho)
    y = random.randint(0, altura_janela - bola_tamanho)
    bolas.append(pygame.Rect(x, y, bola_tamanho, bola_tamanho))

# Função para desenhar o Pac-Man
def desenhar_pacman():
    pygame.draw.circle(janela, AMARELO, pacman_posicao, pacman_tamanho)

# Função para desenhar as bolas
def desenhar_bolas():
    for bola in bolas:
        pygame.draw.circle(janela, BRANCO, bola.center, bola_tamanho)

# Função para verificar colisão com as bolas
def verificar_colisao():
    for bola in bolas:
        if pygame.Rect(pacman_posicao[0] - pacman_tamanho, pacman_posicao[1] - pacman_tamanho,
                       pacman_tamanho * 2, pacman_tamanho * 2).colliderect(bola):
            bolas.remove(bola)

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Lógica da IA
    direcao_ia = [random.randint(-1, 1), random.randint(-1, 1)]

    # Movendo o Pac-Man
    pacman_posicao[0] += pacman_direcao[0] * pacman_velocidade
    pacman_posicao[1] += pacman_direcao[1] * pacman_velocidade

    # Movendo a IA
    pacman_posicao[0] += direcao_ia[0] * pacman_velocidade
    pacman_posicao[1] += direcao_ia[1] * pacman_velocidade

    # Verificando colisão com as bolas
    verificar_colisao()

    # Desenhando o jogo na tela
    janela.fill(PRETO)
    desenhar_bolas()
    desenhar_pacman()
    pygame.display.update()

# Encerrando o Pygame
pygame.quit()
