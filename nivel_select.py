import pygame
import assets
import random

#Define a sequência máxima de cores
def nivel(window):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if botao_10.collidepoint(pos):
                        window.fill((0, 0, 0))
                        assets.assets["SOMMENU"].play()
                        return int(10)
                    elif botao_20.collidepoint(pos):
                        assets.assets["SOMMENU"].play()
                        return int(20)
                    elif botao_40.collidepoint(pos):
                        assets.assets["SOMMENU"].play()
                        return int(40)
            #Texto escrito "selecione"
            window.fill((0, 0, 0))
            text_surface = assets.assets['score_font'].render("Selecione:", True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (250,  30)
            window.blit(text_surface, text_rect)
            #Botão 10 níveis
            botao_10 = pygame.draw.rect(window, (255, 140, 0), (100, 75, 300, 50))
            text_surface = assets.assets['play_again_font'].render("10 níveis", True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (250,  90)
            window.blit(text_surface, text_rect)
            #Botão 20 níveis
            botao_20 = pygame.draw.rect(window, (255, 140, 0), (100, 175, 300, 50))
            text_surface = assets.assets['play_again_font'].render("20 níveis", True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (250,  190)
            window.blit(text_surface, text_rect)
            #Botão 40 níveis
            botao_40 = pygame.draw.rect(window, (255, 140, 0), (100, 275, 300, 50))
            text_surface = assets.assets['play_again_font'].render("40 níveis", True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (250,  290)
            window.blit(text_surface, text_rect)

            pygame.display.update()

#Cria a lista
def aleatorio(j,lista):
    i=0
    while i < j:
        lista.append(random.randint(0, 3))
        i += 1
    print(lista)
    return lista