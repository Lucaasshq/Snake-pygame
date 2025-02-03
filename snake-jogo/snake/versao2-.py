
import pygame
import random


pygame.init()


largura, altura = 640, 480
tamanho = largura, altura
# Cria a tela do jogo com as dimensões especificadas
tela = pygame.display.set_mode((tamanho))


nome_do_jogo = pygame.display.set_caption("Snake")

cor_fundo = pygame.Color("blue") 


cobra_pos = [100, 50]

cobra_corpo = [[100, 50], [90, 50], [80, 50]]

# Gera a posição inicial da fruta de forma aleatória
fruta_pos = [random.randrange(1, (largura // 10)) * 10, random.randrange(1, (altura // 10)) * 10]
fruta_spawn = True

def exibir_texto_pontos(pontos):
    text_color = (255,255,255)
    font = pygame.font.Font(None, 30)
    text_surface = font.render(f"Pontos: {pontos}", True, text_color)
    text_position = text_surface.get_rect(center=(50,10))

    return text_surface, text_position

def carregar_imagem_fruta():
    imagem_fruta = pygame.image.load("snake-jogo\snake\Maçã.png")
    imagem_fruta = pygame.transform.scale(imagem_fruta, (10, 10))
    return imagem_fruta

imagem_fruta = carregar_imagem_fruta()


direcao = "DIREITA"
pontos = 0


mudar_direcao = direcao

fps = pygame.time.Clock()


rodando = True
while rodando:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
        
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
    
    if cobra_pos == fruta_pos:
        fruta_spawn = False
        pontos += 1
    else:
        # Remove o último segmento do corpo da cobra
        cobra_corpo.pop()
        
    # Gera uma nova fruta se a anterior foi comida
    if not fruta_spawn:
        fruta_pos = [random.randrange(1, (largura // 10)) * 10, random.randrange(1, (altura // 10)) * 10]
    fruta_spawn = True
    
    # Preenche a tela com a cor de fundo
    tela.fill(cor_fundo)
    text_surface, text_position = exibir_texto_pontos(pontos)
    tela.blit(text_surface, text_position)
    
    
    for corpo in cobra_corpo:
        pygame.draw.rect(tela, pygame.Color('white'), pygame.Rect(corpo[0], corpo[1], 10, 10))
        
    
    tela.blit(imagem_fruta, (fruta_pos[0], fruta_pos[1]))

    
    pygame.display.update()
    
    fps.tick(15)


pygame.quit()