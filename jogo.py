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

def round3():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])

def round4():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])
    pygame.time.wait(500)
    novo_teste(lista[2])
def round5():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])
    pygame.time.wait(500)
    novo_teste(lista[2])
    pygame.time.wait(500)
    novo_teste(lista[3])
def round6():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])
    pygame.time.wait(500)
    novo_teste(lista[2])
    pygame.time.wait(500)
    novo_teste(lista[3])
    pygame.time.wait(500)
    novo_teste(lista[4])
def round7():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])
    pygame.time.wait(500)
    novo_teste(lista[2])
    pygame.time.wait(500)
    novo_teste(lista[3])
    pygame.time.wait(500)
    novo_teste(lista[4])
    pygame.time.wait(500)
    novo_teste(lista[5])
def round8():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])
    pygame.time.wait(500)
    novo_teste(lista[2])
    pygame.time.wait(500)
    novo_teste(lista[3])
    pygame.time.wait(500)
    novo_teste(lista[4])
    pygame.time.wait(500)
    novo_teste(lista[5])
    pygame.time.wait(500)
    novo_teste(lista[6])
def round9():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])
    pygame.time.wait(500)
    novo_teste(lista[2])
    pygame.time.wait(500)
    novo_teste(lista[3])
    pygame.time.wait(500)
    novo_teste(lista[4])
    pygame.time.wait(500)
    novo_teste(lista[5])
    pygame.time.wait(500)
    novo_teste(lista[6])
    pygame.time.wait(500)
    novo_teste(lista[7])
def round10():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])
    pygame.time.wait(500)
    novo_teste(lista[2])
    pygame.time.wait(500)
    novo_teste(lista[3])
    pygame.time.wait(500)
    novo_teste(lista[4])
    pygame.time.wait(500)
    novo_teste(lista[5])
    pygame.time.wait(500)
    novo_teste(lista[6])
    pygame.time.wait(500)
    novo_teste(lista[7])
    pygame.time.wait(500)
    novo_teste(lista[8])
def round11():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])
    pygame.time.wait(500)
    novo_teste(lista[2])
    pygame.time.wait(500)
    novo_teste(lista[3])
    pygame.time.wait(500)
    novo_teste(lista[4])
    pygame.time.wait(500)
    novo_teste(lista[5])
    pygame.time.wait(500)
    novo_teste(lista[6])
    pygame.time.wait(500)
    novo_teste(lista[7])
    pygame.time.wait(500)
    novo_teste(lista[8])
    pygame.time.wait(500)
    novo_teste(lista[9])
def round12():
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[0])
    pygame.time.wait(500)
    r_base(window)
    pygame.time.wait(500)
    novo_teste(lista[1])
    pygame.time.wait(500)
    novo_teste(lista[2])
    pygame.time.wait(500)
    novo_teste(lista[3])
    pygame.time.wait(500)
    novo_teste(lista[4])
    pygame.time.wait(500)
    novo_teste(lista[5])
    pygame.time.wait(500)
    novo_teste(lista[6])
    pygame.time.wait(500)
    novo_teste(lista[7])
    pygame.time.wait(500)
    novo_teste(lista[8])
    pygame.time.wait(500)
    novo_teste(lista[9])
    pygame.time.wait(500)
    novo_teste(lista[10])

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('GENIUS')

# ----- Inicia estruturas de dados
game = True
flag0 = True
flag1 = True
flag2 = True
flag3 = True
flag4 = True
flag5 = True
flag6 = True
flag7 = True
flag8 = True
flag9 = True
flag10 = True
flag11 = True
flag12 = True
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
                print("Você apertou certo")
                r_verde_claro(window)
                SOM00.play()
                pygame.time.wait(500)
                ck.append(0)
                print(ck)
            if vermelho_rect.collidepoint(pos) == 1:
                print("Você apertou certo")
                r_vermelho_claro(window)
                SOM01.play()
                pygame.time.wait(500)
                ck.append(1)
                print(ck)
            if amarelo_rect.collidepoint(pos) == 1:
                print("Você apertou certo")
                r_amarelo_claro(window)
                SOM02.play()
                pygame.time.wait(500)
                ck.append(2)
                print(ck)
            if azul_rect.collidepoint(pos) == 1:
                print("Você apertou certo")
                r_azul_claro(window)
                SOM03.play()
                pygame.time.wait(500)
                ck.append(3)
                print(ck)

            if ck[0] == lista[0] and ck[0] != "z":
                print("0i")
                round3()
                ck = ["z"]
            
            
            if len(ck) >= 3:
                if ck[1] == lista[0] and ck[2] == lista[1] and flag4 == True:
                    print("Next level")
                    round4()
                    print("aquiii")
                    flag4 = False
                    ck = ["z"]
                

            if len(ck) >= 4:
                if ck[1] == lista[0] and ck[2] == lista[1] and ck[3] == lista[2] and flag5 == True:
                    print("PASSOU")
                    round5()
                    flag5 = False
                    ck = ["z"]
                

            if len(ck) >= 5:
                if ck[1] == lista[0] and ck[2] == lista[1] and ck[3] == lista[2] and ck[4] == lista[3] and flag6 == True:
                    print("NOVIDADE")
                    round6()
                    flag6 = False
                    ck = ["z"]
                

            if len(ck) >= 6:
                if ck[1] == lista[0] and ck[2] == lista[1] and ck[3] == lista[2] and ck[4] == lista[3] and ck[5] == lista[4] and flag7 == True:
                    print("FASE DA LAYNE")
                    round7()
                    flag7 = False
                    ck = ["z"]
                

            if len(ck) >= 7:
                if ck[1] == lista[0] and ck[2] == lista[1] and ck[3] == lista[2] and ck[4] == lista[3] and ck[5] == lista[4] and ck[6] == lista[5] and flag8 == True:
                    print("FASE DA JONAS")
                    round8()
                    flag8 = False
                    ck = ["z"]
                

            if len(ck) >= 8:
                if ck[1] == lista[0] and ck[2] == lista[1] and ck[3] == lista[2] and ck[4] == lista[3] and ck[5] == lista[4] and ck[6] == lista[5] and ck[7] == lista[6] and flag9 == True:
                    print("OLHAA")
                    round9()
                    flag9 = False
                    ck = ["z"]
                

            if len(ck) >= 9:
                if ck[1] == lista[0] and ck[2] == lista[1] and ck[3] == lista[2] and ck[4] == lista[3] and ck[5] == lista[4] and ck[6] == lista[5] and ck[7] == lista[6] and ck[8] == lista[7] and flag10 == True:
                    print("Quase")
                    round10()
                    flag10 = False
                    ck = ["z"]
               

            if len(ck) >= 10:
                if ck[1] == lista[0] and ck[2] == lista[1] and ck[3] == lista[2] and ck[4] == lista[3] and ck[5] == lista[4] and ck[6] == lista[5] and ck[7] == lista[6] and ck[8] == lista[7] and ck[9] == lista[8] and flag11 == True:
                    print("Uiii")
                    round11()
                    flag11 = False
                    ck = ["z"]
                

            if len(ck) >= 11:
                if ck[1] == lista[0] and ck[2] == lista[1] and ck[3] == lista[2] and ck[4] == lista[3] and ck[5] == lista[4] and ck[6] == lista[5] and ck[7] == lista[6] and ck[8] == lista[7] and ck[9] == lista[8] and ck[10] == lista[9] and flag12 == True:
                    print("Uiii")
                    round12()
                    flag12 = False
                    ck = ["z"]
                
                


# FINALIZA
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
#lista[0] == 3