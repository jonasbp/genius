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
verde_rect = pygame.Rect(80,10,150,150)
amarelo_rect = pygame.Rect(80,180,150,150)
vermelho_rect = pygame.Rect(250,10,150,150)
azul_rect = pygame.Rect(250,180,150,150)

# Gerando sequencia de 10 cores
lista = []
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
        pygame.time.wait(1500)
    elif liga == 1:
        r_vermelho_claro(window)
        SOM01.play()
        pygame.time.wait(1500)
    elif liga == 2:
        r_amarelo_claro(window)
        SOM02.play()
        pygame.time.wait(1500)
    elif liga == 3:
        r_azul_claro(window)
        SOM03.play()
        pygame.time.wait(1500)

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('GENIUS')

# ----- Inicia estruturas de dados
game = True
flag0 = True
flag1 = True
flag2 = True
flag3 = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        r_base(window)
        if lista[0] == 0 and flag0 == True:
            r_verde_claro(window)
            SOM00.play()
            pygame.time.wait(1500)
            flag0 = False
        elif lista[0] == 1 and flag0 == True:
            r_vermelho_claro(window)
            SOM01.play()
            pygame.time.wait(1500)
            flag0 = False
        elif lista[0] == 2 and flag0 == True:
            r_amarelo_claro(window)
            SOM02.play()
            pygame.time.wait(1500)
            flag0 = False
        elif lista[0] == 3 and flag0 == True:
            r_azul_claro(window)
            SOM03.play()
            pygame.time.wait(1500)
            flag0 = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            #print(pos)
            if verde_rect.collidepoint(pos) and lista[0] == 0:
                print("Parabéns o correto é verde!")
                r_verde_claro(window)
                SOM00.play()
                pygame.time.wait(1500)
                r_base(window)
                pygame.time.wait(1500)
                novo_teste(lista[0])
                novo_teste(lista[1])

            elif vermelho_rect.collidepoint(pos) and lista[0] == 1:
                print("Vermelho")
                r_vermelho_claro(window)
                SOM01.play()
                pygame.time.wait(1500)
                r_base(window)
                pygame.time.wait(1500)
                novo_teste(lista[0])
                novo_teste(lista[1])

            elif amarelo_rect.collidepoint(pos) and lista[0] == 2:
                print("Amarelo")
                r_amarelo_claro(window)
                SOM02.play()
                pygame.time.wait(1500)
                r_base(window)
                pygame.time.wait(1500)
                novo_teste(lista[0])
                novo_teste(lista[1])

            elif azul_rect.collidepoint(pos) and lista[0] == 3:
                print("Azul")
                r_azul_claro(window)
                SOM03.play()
                pygame.time.wait(1500)
                r_base(window)
                pygame.time.wait(1500)
                novo_teste(lista[0])
                novo_teste(lista[1])

            else:
                print("Você perdeu")
                SOMERRO.play()
                pygame.time.wait(1500)
                game = False


# FINALIZA
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
