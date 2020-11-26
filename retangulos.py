# PROJETO FINAL DESIGN DE SOFTWARE
# JOGO GENIUS
# INSPER 2020
# Jonas Bonfá Pelegrina,Layne Pereira Silva,Giancarlo Vanoni Ruggiero

# CONVERSÃO DE NÚMERO PARA COR
# 0 - Verde
# 1 - Vermelho
# 2 - Amarelo
# 3 - Azul
import pygame
import assets

#CORES
VERDE = (0,155,0)
VERDE_CLARO = (0,255,0)

AZUL = (0,0,155)
AZUL_CLARO = (0,0,255)

VERMELHO = (155,0,0)
VERMELHO_CLARO = (255,0,0)

AMARELO = (155,155,0)
AMARELO_CLARO = (225,225,0)

# Propriedade dos retângulos
verde_rect = pygame.Rect(90,40,150,150)
amarelo_rect = pygame.Rect(90,210,150,150)
vermelho_rect = pygame.Rect(260,40,150,150)
azul_rect = pygame.Rect(260,210,150,150)

def placar(score,window):
    #Exibe a pontuação   
    text_surface = assets.assets['score_font'].render("{:08d}".format(score), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (125,  10)
    window.blit(text_surface,text_rect)


#POSSIBILIDADES DE RETÂNGULOS
def r_base(window,score):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    placar(score,window)
    pygame.display.update()
def r_verde_claro(window,score):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE_CLARO), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    placar(score,window)
    pygame.display.update()
def r_vermelho_claro(window,score):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO_CLARO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    placar(score,window)
    pygame.display.update()
def r_amarelo_claro(window,score):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO_CLARO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    placar(score,window)
    pygame.display.update()
def r_azul_claro(window,score):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL_CLARO), (azul_rect))
    placar(score,window)
    pygame.display.update()