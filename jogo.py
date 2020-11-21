# ===== Inicialização =====
# ----- Importa e inicia pacotes
# 0 - Verde
# 1 - Vermelho
# 2 - Amarelo
# 3 - Azul

import pygame
import random

pygame.init()
pygame.mixer.init()

# Carrega os sons do jogo
SOM00 = pygame.mixer.Sound('sons/00.wav')
SOM01 = pygame.mixer.Sound('sons/01.wav')
SOM02 = pygame.mixer.Sound('sons/02.wav')
SOM03 = pygame.mixer.Sound('sons/03.wav')
#VERDE
VERDE = (0,155,0)
VERDE_CLARO = (0,255,0)
#AZUL
AZUL = (0,0,155)
AZUL_CLARO = (0,0,255)
#VERMELHO
VERMELHO = (155,0,0)
VERMELHO_CLARO = (255,0,0)
#AMARELO
AMARELO = (155,155,0)
AMARELO_CLARO = (225,225,0)

# Variaveis para os retangulos
verde_rect = pygame.Rect(80,10,150,150)
amarelo_rect = pygame.Rect(80,180,150,150)
vermelho_rect = pygame.Rect(250,10,150,150)
azul_rect = pygame.Rect(250,180,150,150)

# Gerando sequencia para o jogo
lista = []
i = 0

while i < 10:
    lista.append(random.randint(0, 3))
    i += 1
print(lista)

# MANIPULA DADOS
#print(lista)

contador = 0
flag = True


# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('GENIUS')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
     # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (AMARELO), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (VERMELHO), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (AZUL), (azul_rect))

    while contador == lista[0]:
        print("oi")
        contador = contador + 1

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        # INICIA O PRIMEIRO SOM
        while flag:
            if lista[0] == 0:
                SOM00.play()
                flag = False

            elif lista[0] == 1:
                SOM01.play()
                flag = False
            elif lista[0] == 2:
                SOM02.play()
                flag = False
            elif lista[0] == 3:
                SOM03.play()
                flag = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            #print(pos)
            if verde_rect.collidepoint(pos):
                print("Parabéns o correto é verde!")
                SOM00.play()
            if vermelho_rect.collidepoint(pos):
                print("Vermelho")
                SOM01.play()
            if amarelo_rect.collidepoint(pos):
                print("Amarelo")
                SOM02.play()
            if azul_rect.collidepoint(pos):
                print("Azul")
                SOM03.play()
                #and lista[0] == 0

    #PERGUNTAR AQUI

    #r_verde_pressionado = pygame.draw.rect(window, (0,255,0), (150,20,40,40))
    #r_amarelo_pressionado = pygame.draw.rect(window, (255,255,0), (150,100,40,40))
    #r_vermelho_pressionado = pygame.draw.rect(window, (255,0,0), (200,20,40,40))
    #r_azul_pressionado = pygame.draw.rect(window, (0,0,255), (200,100,40,40))


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
