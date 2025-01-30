import pygame
import sys

pygame.init()

largura, altura = 640, 480
tamanho = largura, altura
tela = pygame.display.set_mode((tamanho))

imagem_fundo = pygame.image.load("snake-jogo\snake\Fundo.png")
nome_do_jogo = pygame.display.set_caption("Snake")


cor_fundo = (255, 0, 0) 

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False


    
    
    tela.blit(imagem_fundo, (0, 0))
 
    pygame.display.flip()
        

