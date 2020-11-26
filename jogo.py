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
import time
import retangulos
import assets
import jogar_novamente
import nivel_select

def principal(window):
    #Variáveis
    score = 0
    lista = []
    ck = ["z"]
    game = False
    flag0 = True
    round_atual = 1
    cor_atual = 0
    tela_principal=True
    
    def novo_teste(liga):
        if liga == 0:
            retangulos.r_verde_claro(window,score)
            assets.assets["SOM00"].play()
            pygame.time.wait(300)
        elif liga == 1:
            retangulos.r_vermelho_claro(window,score)
            assets.assets["SOM01"].play()
            pygame.time.wait(300)
        elif liga == 2:
            retangulos.r_amarelo_claro(window,score)
            assets.assets["SOM02"].play()
            pygame.time.wait(300)
        elif liga == 3:
            retangulos.r_azul_claro(window,score)
            assets.assets["SOM03"].play()
            pygame.time.wait(300)

    def mostra_round(r):
        for cor in lista[:r]:
            retangulos.r_base(window,score)
            pygame.time.wait(250)
            novo_teste(cor)   

    #Entra na tela inicial
    while tela_principal:
        fundo = pygame.image.load('assets/img/Tela_principal.jpeg').convert()
        window.blit(fundo, (0,0))
        pygame.display.update()
        assets.assets["SOMTELAPRINCIPAL"].play()
        pygame.time.wait(2000)
        fundo = pygame.image.load('assets/img/guide.png').convert()
        window.blit(fundo, (0,0))
        pygame.display.update()
        assets.assets["SOMTELAPRINCIPAL"]
        pygame.time.wait(5000)
        j=nivel_select.nivel(window)
        nivel_select.aleatorio(j,lista)
        tela_principal=False
        game=True

    #Entra no jogo    
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            retangulos.r_base(window,score)

            #Inicia o jogo
            if flag0 == True:
                pygame.time.wait(1500)
                novo_teste(lista[0])
                flag0 = False
            
            #Identifica em qual retângulo o usuário clicou
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if retangulos.verde_rect.collidepoint(pos) == 1:
                    print("Você apertou verde")
                    retangulos.r_verde_claro(window,score)
                    assets.assets["SOM00"].play()
                    pygame.time.wait(250)
                    ck.append(0)
                    print(ck)
                if retangulos.vermelho_rect.collidepoint(pos) == 1:
                    print("Você apertou vermelho")
                    retangulos.r_vermelho_claro(window,score)
                    assets.assets["SOM01"].play()
                    pygame.time.wait(250)
                    ck.append(1)
                    print(ck)
                if retangulos.amarelo_rect.collidepoint(pos) == 1:
                    print("Você apertou amarelo")
                    retangulos.r_amarelo_claro(window,score)
                    assets.assets["SOM02"].play()
                    pygame.time.wait(250)
                    ck.append(2)
                    print(ck)
                if retangulos.azul_rect.collidepoint(pos) == 1:
                    print("Você apertou azul")
                    retangulos.r_azul_claro(window,score)
                    assets.assets["SOM03"].play()
                    pygame.time.wait(250)
                    ck.append(3)
                    print(ck)

                if ck[0]=="z":
                    if ck[-1] == lista[cor_atual]: #Caso o jogador selecione a cor correta 
                        if len(ck) - 1 == round_atual: #Caso ele acerte a última cor da rodada ele passa para a próxma
                            round_atual += 1
                            score+=100 # O jogador ganha 100 pontos
                            if score==100*j: #Caso o jogador acerte todas as rodadas ele vence o jogo
                                assets.assets["SOMVITORIA"].play()
                                game=jogar_novamente.jogar_novamente("vitoria",window,score)
                                if game:
                                    lista=[]
                                    j=nivel_select.nivel(window)
                                    lista = nivel_select.aleatorio(j,lista)
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
                        else: #Caso não seja a última cor da rodada ele passa para a próxima cor para comparar
                            cor_atual += 1
                    else: #Caso o jogador erre a cor
                        assets.assets["SOMERRO"].play()
                        game=jogar_novamente.jogar_novamente("derrota",window,score)
                        if game:
                            lista = []
                            ck = ["z"]
                            j=nivel_select.nivel(window)
                            lista=nivel_select.aleatorio(j,lista)
                            score=0
                            flag0 = True
                            round_atual = 1
                            cor_atual = 0
                        else:
                            pygame.quit() 