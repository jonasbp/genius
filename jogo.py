# PROJETO FINAL DESIGN DE SOFTWARE
# JOGO GENIUS
# INSPER 2020
# Jonas Bonfá Pelegrina,Layne Pereira Silva,Giancarlo

# CONVERSÃO DE NÚMERO PARA COR
# 0 - Verde
# 1 - Vermelho
# 2 - Amarelo
# 3 - Azul

import pygame
import random
import time

pygame.init()
pygame.mixer.init()

assets = {}
assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
score = 0

# Carrega os sons do jogo
SOM00 = pygame.mixer.Sound('sons/00.wav') # VERDE
SOM01 = pygame.mixer.Sound('sons/01.wav') # VERMELHO
SOM02 = pygame.mixer.Sound('sons/02.wav') # AMARELO
SOM03 = pygame.mixer.Sound('sons/03.wav') # AZUL
SOMERRO = pygame.mixer.Sound('sons/erro.wav') # SOM DE ERRO

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

# Gerando sequencia de 10 cores
lista = []
lista_cor =["Verde", 'Amarelo', 'Vermelho', 'Azul']
ck = []
i = 0
while i < 10:
    lista.append(random.randint(0, 3))
    i += 1
print(lista)
#POSSIBILIDADES DE RETÂNGULOS
def r_base(window):
    window.fill((0, 0, 0))  # Preenche com a cor branca
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    pygame.display.update()
def r_verde_claro(window):
    window.fill((0, 0, 0))  # Preenche com a cor branca
    r_verde = pygame.draw.rect(window, (VERDE_CLARO), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    pygame.display.update()
def r_vermelho_claro(window):
    window.fill((0, 0, 0))  # Preenche com a cor branca
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO_CLARO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    pygame.display.update()
def r_amarelo_claro(window):
    window.fill((0, 0, 0))  # Preenche com a cor branca
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO_CLARO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    pygame.display.update()
def r_azul_claro(window):
    window.fill((0, 0, 0))  # Preenche com a cor branca
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL_CLARO), (azul_rect))
    pygame.display.update()

def novo_teste(liga):
    if liga == 0:
        r_verde_claro(window)
        SOM00.play()
        pygame.time.wait(500)
    elif liga == 1:
        r_vermelho_claro(window)
        SOM01.play()
        pygame.time.wait(500)
    elif liga == 2:
        r_amarelo_claro(window)
        SOM02.play()
        pygame.time.wait(500)
    elif liga == 3:
        r_azul_claro(window)
        SOM03.play()
        pygame.time.wait(500)

def round3():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])

def mostra_round(r):
    for cor in lista[:r]:
        r_base(window)
        pygame.time.wait(500)
        novo_teste(cor)


# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('GENIUS')

# ----- Inicia estruturas de dados
game = True
flag0 = True
round_atual = 2
cor_atual = 0

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        r_base(window)

        #TOCA O 1
        if flag0 == True:
            novo_teste(lista[0])
            flag0 = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if verde_rect.collidepoint(pos) == 1:
                print("Você apertou verde")
                r_verde_claro(window)
                SOM00.play()
                pygame.time.wait(500)
                ck.append(0)
                print(ck)
            if vermelho_rect.collidepoint(pos) == 1:
                print("Você apertou vermelho")
                r_vermelho_claro(window)
                SOM01.play()
                pygame.time.wait(500)
                ck.append(1)
                print(ck)
            if amarelo_rect.collidepoint(pos) == 1:
                print("Você apertou amarelo")
                r_amarelo_claro(window)
                SOM02.play()
                pygame.time.wait(500)
                ck.append(2)
                print(ck)
            if azul_rect.collidepoint(pos) == 1:
                print("Você apertou azul")
                r_azul_claro(window)
                SOM03.play()
                pygame.time.wait(500)
                ck.append(3)
                print(ck)
            if ck[0] != "z":
                if ck[0] == lista[0]:
                    print("0i")
                    round3()
                    ck = ["z"]
                    score += 100
                else:
                    print("você perdeu")
                    game=False
                    
            else:
                if ck[-1] == lista[cor_atual]:
                    if len(ck) - 1 == round_atual:
                        round_atual += 1
                        mostra_round(round_atual)
                        cor_atual = 0
                        ck = ["z"] 
                        score+=100
                    else:
                        cor_atual += 1
                else:
                    game=False
                    pass

    text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (150,  10)
    window.blit(text_surface, text_rect)

    pygame.display.update()
                    # FINALIZA
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados