import pygame
pygame.init()

assets = {}
assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
assets["play_again_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 14)
assets["SOM00"] = pygame.mixer.Sound('sons/00.wav') # VERDE
assets["SOM01"] = pygame.mixer.Sound('sons/01.wav') # VERMELHO
assets["SOM02"] = pygame.mixer.Sound('sons/02.wav') # AMARELO
assets["SOM03"] = pygame.mixer.Sound('sons/03.wav') # AZUL
assets["SOMERRO"] = pygame.mixer.Sound('sons/erro.wav') # SOM DE ERRO
assets["SOMVITORIA"] = pygame.mixer.Sound('sons/vitoria.wav') #SOM VITORIA
assets["SOMTELAPRINCIPAL"] = pygame.mixer.Sound('sons/tela_inicial.ogg') #SOM TELA PRINCIPAL
assets["SOMMENU"] = pygame.mixer.Sound('sons/som_menu.wav') #SOM MENU