import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 940, 880
tamanho = largura, altura
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Snake")

# Cores
branco = (255, 255, 255)

# Posições e corpos da cobra e da fruta
cobra_pos = [100, 50]
cobra_corpo = [[100, 50], [90, 50], [80, 50]]
fruta_pos = [random.randrange(1, (largura // 10)) * 10, random.randrange(1, (altura // 10)) * 10]
fruta_spawn = True

# Direção inicial da cobra
direcao = "DIREITA"
mudar_direcao = direcao

# Função para exibir a tela inicial
def tela_inicial():
    tela.blit(imagem_fundo, (0, 0))
    fonte = pygame.font.Font(None, 74)
    texto = fonte.render("Pressione ESPAÇO para iniciar", True, branco)
    texto_rect = texto.get_rect(center=(largura // 2, altura // 2))
    tela.blit(texto, texto_rect)
    pygame.display.flip()

# Função para exibir a tela de Game Over
def tela_game_over():
    tela.blit(imagem_fundo, (0, 0))
    fonte = pygame.font.Font(None, 74)
    texto = fonte.render("Game Over", True, branco)
    texto_rect = texto.get_rect(center=(largura // 2, altura // 2))
    tela.blit(texto, texto_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Espera 2 segundos antes de voltar para a tela inicial

# Função para exibir os pontos
def exibir_texto_pontos(pontos):
    font = pygame.font.Font(None, 30)
    text_surface = font.render(f"Pontos: {pontos}", True, branco)
    text_position = text_surface.get_rect(center=(50, 10))
    return text_surface, text_position

# Funções para carregar imagens
def carregar_imagem_fruta():
    imagem_fruta = pygame.image.load("snake/Maçã.png")
    imagem_fruta = pygame.transform.scale(imagem_fruta, (10, 10))
    return imagem_fruta

def carregar_imagem_corpo():
    imagem_corpo = pygame.image.load("snake/2.png")
    imagem_corpo = pygame.transform.scale(imagem_corpo, (10, 10))
    return imagem_corpo

def carregar_imagem_de_fundo():
    imagem_fundo = pygame.image.load("snake/fundo-verde.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
    return imagem_fundo

# Função para reiniciar o jogo
def reiniciar_jogo():
    global cobra_pos, cobra_corpo, direcao, mudar_direcao, fruta_pos, fruta_spawn, pontos
    cobra_pos = [100, 50]
    cobra_corpo = [[100, 50], [90, 50], [80, 50]]
    direcao = "DIREITA"
    mudar_direcao = direcao
    fruta_pos = [random.randrange(1, (largura // 10)) * 10, random.randrange(1, (altura // 10)) * 10]
    fruta_spawn = True
    pontos = 0

# Carrega as imagens
imagem_fruta = carregar_imagem_fruta()
imagem_corpo = carregar_imagem_corpo()
imagem_fundo = carregar_imagem_de_fundo()

# Variáveis de controle
pontos = 0
fps = pygame.time.Clock()

# Loop principal
mostrando_tela_inicial = True
rodando = True
while rodando:
    if mostrando_tela_inicial:
        tela_inicial()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    mostrando_tela_inicial = False
                    reiniciar_jogo()
    else:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != 'BAIXO':
                    mudar_direcao = 'CIMA'
                elif evento.key == pygame.K_DOWN and direcao != 'CIMA':
                    mudar_direcao = 'BAIXO'
                elif evento.key == pygame.K_LEFT and direcao != 'DIREITA':
                    mudar_direcao = 'ESQUERDA'
                elif evento.key == pygame.K_RIGHT and direcao != 'ESQUERDA':
                    mudar_direcao = 'DIREITA'

        # Atualiza a direção da cobra
        if mudar_direcao == 'CIMA' and direcao != 'BAIXO':
            direcao = 'CIMA'
        if mudar_direcao == 'BAIXO' and direcao != 'CIMA':
            direcao = 'BAIXO'
        if mudar_direcao == 'ESQUERDA' and direcao != 'DIREITA':
            direcao = 'ESQUERDA'
        if mudar_direcao == 'DIREITA' and direcao != 'ESQUERDA':
            direcao = 'DIREITA'

        # Move a posição da cobra
        if direcao == 'CIMA':
            cobra_pos[1] -= 10
        if direcao == 'BAIXO':
            cobra_pos[1] += 10
        if direcao == 'ESQUERDA':
            cobra_pos[0] -= 10
        if direcao == 'DIREITA':
            cobra_pos[0] += 10

        # Atualiza o corpo da cobra
        cobra_corpo.insert(0, list(cobra_pos))
        if cobra_pos == fruta_pos:
            fruta_spawn = False
            pontos += 1
        else:
            cobra_corpo.pop()

        # Gera uma nova fruta se necessário
        if not fruta_spawn:
            fruta_pos = [random.randrange(1, (largura // 10)) * 10, random.randrange(1, (altura // 10)) * 10]
        fruta_spawn = True

        # Desenha a tela do jogo
        tela.blit(imagem_fundo, (0, 0))
        text_surface, text_position = exibir_texto_pontos(pontos)
        tela.blit(text_surface, text_position)
        tela.blit(imagem_fruta, (fruta_pos[0], fruta_pos[1]))
        for corpo in cobra_corpo:
            tela.blit(imagem_corpo, (corpo[0], corpo[1]))

        # Verifica colisões
        if cobra_pos[0] < 0 or cobra_pos[0] >= largura or cobra_pos[1] < 0 or cobra_pos[1] >= altura:
            tela_game_over()
            mostrando_tela_inicial = True
        for bloco in cobra_corpo[1:]:
            if cobra_pos == bloco:
                tela_game_over()
                mostrando_tela_inicial = True

        # Atualiza a tela
        pygame.display.update()
        fps.tick(15)

pygame.quit()