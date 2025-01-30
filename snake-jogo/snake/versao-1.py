import pygame
import sys

pygame.init()

largura, altura = 640, 480
tamanho = largura, altura
tela = pygame.display.set_mode((tamanho))

nome_do_jogo = pygame.display.set_caption("Snake")
cor_fundo = pygame.Color("blue") 

cobra_pos = [100, 50]
cobra_corpo = [[100, 50], [90, 50], [80, 50]]



direcao = "DIREITA"

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
                
    if mudar_direcao == 'CIMA' and direcao != 'BAIXO':
        direcao = 'CIMA'
    if mudar_direcao == 'BAIXO' and direcao != 'CIMA':
        direcao = 'BAIXO'
    if mudar_direcao == 'ESQUERDA' and direcao != 'DIREITA':
        direcao = 'ESQUERDA'
    if mudar_direcao == 'DIREITA' and direcao != 'ESQUERDA':
        direcao = 'DIREITA'
        
    if direcao == 'CIMA':
        cobra_pos[1] -= 10
    if direcao == 'BAIXO':
        cobra_pos[1] += 10
    if direcao == 'ESQUERDA':
        cobra_pos[0] -= 10
    if direcao == 'DIREITA':
        cobra_pos[0] += 10
        
    cobra_corpo.insert(0, list(cobra_pos))
    cobra_corpo.pop()
    
    tela.fill(cor_fundo)
    
    for corpo in cobra_corpo:
        pygame.draw.rect(tela, pygame.Color('white'), pygame.Rect(corpo[0], corpo[1], 10, 10))
        
    pygame.display.update()
    fps.tick(15)
pygame.quit()
        

