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
import random
import time

pygame.init()
pygame.mixer.init()

assets = {}
assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
assets["play_again_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 14)

score = 0

# Carrega os sons do jogo
SOM00 = pygame.mixer.Sound('sons/00.wav') # VERDE
SOM01 = pygame.mixer.Sound('sons/01.wav') # VERMELHO
SOM02 = pygame.mixer.Sound('sons/02.wav') # AMARELO
SOM03 = pygame.mixer.Sound('sons/03.wav') # AZUL
SOMERRO = pygame.mixer.Sound('sons/erro.wav') # SOM DE ERRO
SOMVITORIA = pygame.mixer.Sound('sons/vitoria.wav') #SOM VITORIA
SOMTELAPRINCIPAL = pygame.mixer.Sound('sons/tela_inicial.ogg') #SOM TELA PRINCIPAL

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
def jogar_novamente(decisao):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if botao.collidepoint(pos):
                    window.fill((0, 0, 0))
                    pygame.display.update()
                    return True
                elif botao_sair.collidepoint(pos):
                    return False
        
        window.fill((0, 0, 0))

        #Botão jogar novamente
        botao = pygame.draw.rect(window, (255, 140, 0), (100, 175, 300, 50))
        text_surface = assets['play_again_font'].render("Jogar novamente", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (250,  190)
        window.blit(text_surface, text_rect)
        #Botão sair
        botao_sair = pygame.draw.rect(window, (255, 140, 0), (125, 275, 250, 50))
        text_surface = assets['play_again_font'].render("Sair", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (250,  290)
        window.blit(text_surface, text_rect)
        #Decide entre se o jogador perdeu ou ganhou
        if decisao=="derrota":
            #Exibe mensagem "Você perdeu"
            texto_surface = assets['score_font'].render("Você perdeu", True, (255, 255, 255))
            texto_rect = text_surface.get_rect()
            texto_rect.midtop = (125,  60)
            window.blit(texto_surface, texto_rect)
            #Mostra a pontuação
            text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (250,  140)
            window.blit(text_surface, text_rect)
            texto_surface = assets['score_font'].render("Pontuação:", True, (255, 255, 255))
            texto_rect = text_surface.get_rect()
            texto_rect.midtop = (230,  100)
            window.blit(texto_surface, texto_rect)
        elif decisao=="vitoria":
            #Exibe a mensagem "Você ganhou"
            texto_surface = assets['score_font'].render("Você ganhou", True, (255, 255, 255))
            texto_rect = text_surface.get_rect()
            texto_rect.midtop = (130,  60)
            window.blit(texto_surface, texto_rect)

        pygame.display.update()
# Gerando sequencia de 10 cores
lista = []
ck = ["z"]
def nivel():
 while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if botao_10.collidepoint(pos):
                    window.fill((0, 0, 0))
                    pygame.display.update()
                    return int(10)
                elif botao_20.collidepoint(pos):
                    return int(20)
                elif botao_40.collidepoint(pos):
                    return int(40)
        #Texto escrito "selecione"
        window.fill((0, 0, 0))
        text_surface = assets['score_font'].render("Selecione:", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (250,  30)
        window.blit(text_surface, text_rect)
        #Botão 10 níveis
        botao_10 = pygame.draw.rect(window, (255, 140, 0), (100, 75, 300, 50))
        text_surface = assets['play_again_font'].render("10 níveis", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (250,  90)
        window.blit(text_surface, text_rect)
        #Botão 20 níveis
        botao_20 = pygame.draw.rect(window, (255, 140, 0), (100, 175, 300, 50))
        text_surface = assets['play_again_font'].render("20 níveis", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (250,  190)
        window.blit(text_surface, text_rect)
        #Botão 40 níveis
        botao_40 = pygame.draw.rect(window, (255, 140, 0), (100, 275, 300, 50))
        text_surface = assets['play_again_font'].render("40 níveis", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (250,  290)
        window.blit(text_surface, text_rect)

        pygame.display.update()
def aleatorio(j):
    i=0
    while i < j:
        lista.append(random.randint(0, 3))
        i += 1
    print(lista)
    return lista

#POSSIBILIDADES DE RETÂNGULOS
def r_base(window):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    placar(score)
    pygame.display.update()
def r_verde_claro(window):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE_CLARO), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    placar(score)
    pygame.display.update()
def r_vermelho_claro(window):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO_CLARO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    placar(score)
    pygame.display.update()
def r_amarelo_claro(window):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO_CLARO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))
    placar(score)
    pygame.display.update()
def r_azul_claro(window):
    window.fill((0,0,0))
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL_CLARO), (azul_rect))
    placar(score)
    pygame.display.update()

def novo_teste(liga):
    if liga == 0:
        r_verde_claro(window)
        SOM00.play()
        pygame.time.wait(300)
    elif liga == 1:
        r_vermelho_claro(window)
        SOM01.play()
        pygame.time.wait(300)
    elif liga == 2:
        r_amarelo_claro(window)
        SOM02.play()
        pygame.time.wait(300)
    elif liga == 3:
        r_azul_claro(window)
        SOM03.play()
        pygame.time.wait(300)

def mostra_round(r):
    for cor in lista[:r]:
        r_base(window)
        pygame.time.wait(250)
        novo_teste(cor)   
# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('GENIUS')

# ----- Inicia estruturas de dados
game = False
flag0 = True
round_atual = 1
cor_atual = 0
tela_principal=True

while tela_principal:
    fundo = pygame.image.load('assets/img/Tela_principal.jpeg').convert()
    window.blit(fundo, (0,0))
    pygame.display.update()
    SOMTELAPRINCIPAL.play()
    pygame.time.wait(2000)
    fundo = pygame.image.load('assets/img/guide.png').convert()
    window.blit(fundo, (0,0))
    pygame.display.update()
    SOMTELAPRINCIPAL.play()
    pygame.time.wait(10000)
    j=nivel()
    aleatorio(j)
    tela_principal=False
    game=True
    
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        r_base(window)

        #TOCA O 1
        if flag0 == True:
            pygame.time.wait(1500)
            novo_teste(lista[0])
            flag0 = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if verde_rect.collidepoint(pos) == 1:
                print("Você apertou verde")
                r_verde_claro(window)
                SOM00.play()
                pygame.time.wait(250)
                ck.append(0)
                print(ck)
            if vermelho_rect.collidepoint(pos) == 1:
                print("Você apertou vermelho")
                r_vermelho_claro(window)
                SOM01.play()
                pygame.time.wait(250)
                ck.append(1)
                print(ck)
            if amarelo_rect.collidepoint(pos) == 1:
                print("Você apertou amarelo")
                r_amarelo_claro(window)
                SOM02.play()
                pygame.time.wait(250)
                ck.append(2)
                print(ck)
            if azul_rect.collidepoint(pos) == 1:
                print("Você apertou azul")
                r_azul_claro(window)
                SOM03.play()
                pygame.time.wait(250)
                ck.append(3)
                print(ck)
          
            if ck[0]=="z":
                if ck[-1] == lista[cor_atual]:
                    if len(ck) - 1 == round_atual:
                        round_atual += 1
                        score+=100
                        if score==100*j:
                            SOMVITORIA.play()
                            game=jogar_novamente("vitoria")
                            if game:
                                lista=[]
                                j=nivel()
                                lista = aleatorio(j)
                                ck = ["z"]
                                score=0
                                flag0 = True
                                round_atual = 1
                                cor_atual = 0
                            else:
                                pygame.quit()
                        else:
                            mostra_round(round_atual)
                            cor_atual = 0
                            ck = ["z"] 
                    else:
                        cor_atual += 1
                else:
                    SOMERRO.play()
                    game=jogar_novamente("derrota")
                    if game:
                        lista = []
                        ck = ["z"]
                        j=nivel()
                        lista=aleatorio(j)
                        score=0
                        flag0 = True
                        round_atual = 1
                        cor_atual = 0
                        continue
                    else:
                        pygame.quit()

    def placar(score):
    #Exibe a pontuação   
        text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (125,  10)
        window.blit(text_surface, text_rect)

    # FINALIZA
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
        