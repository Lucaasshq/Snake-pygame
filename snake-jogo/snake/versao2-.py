import pygame
import sys
import random

# Inicializa o módulo pygame
pygame.init()

# Define a largura e altura da tela
largura, altura = 640, 480
tamanho = largura, altura
# Cria a tela do jogo com as dimensões especificadas
tela = pygame.display.set_mode((tamanho))

# Define o título da janela do jogo
nome_do_jogo = pygame.display.set_caption("Snake")
# Define a cor de fundo da tela
cor_fundo = pygame.Color("blue") 

# Posição inicial da cabeça da cobra
cobra_pos = [100, 50]
# Corpo inicial da cobra (uma lista de segmentos)
cobra_corpo = [[100, 50], [90, 50], [80, 50]]

# Gera a posição inicial da fruta de forma aleatória
fruta_pos = [random.randrange(1, (largura // 10)) * 10, random.randrange(1, (altura // 10)) * 10]
fruta_spawn = True

# Direção inicial da cobra
direcao = "DIREITA"

# Variável para armazenar a nova direção da cobra
mudar_direcao = direcao
# Controla os frames por segundo (FPS) do jogo
fps = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    # Verifica os eventos (como pressionar teclas ou fechar a janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            # Muda a direção com base na tecla pressionada
            if event.key == pygame.K_UP:
                mudar_direcao = 'CIMA'
            elif event.key == pygame.K_DOWN:
                mudar_direcao = 'BAIXO'
            elif event.key == pygame.K_LEFT:
                mudar_direcao = 'ESQUERDA'
            elif event.key == pygame.K_RIGHT:
                mudar_direcao = 'DIREITA'
                
    # Atualiza a direção da cobra, evitando movimentos opostos
    if mudar_direcao == 'CIMA' and direcao != 'BAIXO':
        direcao = 'CIMA'
    if mudar_direcao == 'BAIXO' and direcao != 'CIMA':
        direcao = 'BAIXO'
    if mudar_direcao == 'ESQUERDA' and direcao != 'DIREITA':
        direcao = 'ESQUERDA'
    if mudar_direcao == 'DIREITA' and direcao != 'ESQUERDA':
        direcao = 'DIREITA'
        
    # Move a posição da cobra com base na direção atual
    if direcao == 'CIMA':
        cobra_pos[1] -= 10
    if direcao == 'BAIXO':
        cobra_pos[1] += 10
    if direcao == 'ESQUERDA':
        cobra_pos[0] -= 10
    if direcao == 'DIREITA':
        cobra_pos[0] += 10
        
    # Insere a nova posição da cabeça da cobra no início do corpo
    cobra_corpo.insert(0, list(cobra_pos))
    # Verifica se a cobra comeu a fruta
    if cobra_pos == fruta_pos:
        fruta_spawn = False
    else:
        # Remove o último segmento do corpo da cobra
        cobra_corpo.pop()
        
    # Gera uma nova fruta se a anterior foi comida
    if not fruta_spawn:
        fruta_pos = [random.randrange(1, (largura // 10)) * 10, random.randrange(1, (altura // 10)) * 10]
    fruta_spawn = True
    
    # Preenche a tela com a cor de fundo
    tela.fill(cor_fundo)
    
    # Desenha cada segmento do corpo da cobra na tela
    for corpo in cobra_corpo:
        pygame.draw.rect(tela, pygame.Color('white'), pygame.Rect(corpo[0], corpo[1], 10, 10))
        
    # Desenha a fruta na tela
    pygame.draw.rect(tela, pygame.Color("red"), pygame.Rect(fruta_pos[0], fruta_pos[1], 10, 10))

    # Atualiza a tela
    pygame.display.update()
    # Define a taxa de atualização do jogo (FPS)
    fps.tick(15)

# Encerra o módulo pygame
pygame.quit()