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
som_00 = pygame.mixer.Sound('sons/00.wav')
som_01 = pygame.mixer.Sound('sons/01.wav')
som_02 = pygame.mixer.Sound('sons/02.wav')
som_03 = pygame.mixer.Sound('sons/03.wav')

VERDE = (0,200,0)
# Variaveis para os retangulos
verde_rect = pygame.Rect(150,20,40,40)
amarelo_rect = pygame.Rect(150,100,40,40)
vermelho_rect = pygame.Rect(200,20,40,40)
azul_rect = pygame.Rect(200,100,40,40)

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

# Importando sons
som_00 = pygame.mixer.Sound("sons/00.wav")

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('GENIUS')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:

    while contador == lista[0]:
        print("oi")
        contador = contador + 1

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            #print(pos)
            if verde_rect.collidepoint(pos):
                print("Parabéns o correto é verde!")
                som_00.play()
            if vermelho_rect.collidepoint(pos):
                print("Vermelho")
                som_01.play()
            if amarelo_rect.collidepoint(pos):
                print("Amarelo")
                som_02.play()
            if azul_rect.collidepoint(pos):
                print("Azul")
                som_03.play()
                #and lista[0] == 0
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    r_verde = pygame.draw.rect(window, (VERDE), (verde_rect))
    r_amarelo = pygame.draw.rect(window, (200,200,0), (amarelo_rect))
    r_vermelho = pygame.draw.rect(window, (200,0,0), (vermelho_rect))
    r_azul = pygame.draw.rect(window, (0,0,255), (azul_rect))

    #PERGUNTAR AQUI

    #r_verde_pressionado = pygame.draw.rect(window, (0,255,0), (150,20,40,40))
    #r_amarelo_pressionado = pygame.draw.rect(window, (255,255,0), (150,100,40,40))
    #r_vermelho_pressionado = pygame.draw.rect(window, (255,0,0), (200,20,40,40))
    #r_azul_pressionado = pygame.draw.rect(window, (0,0,255), (200,100,40,40))


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
