import pygame
import sys

pygame.init()

largura, altura = 640, 480
tamanho = largura, altura
tela = pygame.display.set_mode((tamanho))

nome_do_jogo = pygame.display.set_caption("Snake")


cor_fundo = (255, 0, 0) 

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False


    
    
    tela.fill(cor_fundo)
    # Atualiza a tela
    pygame.display.flip()
        

