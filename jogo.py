# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

VERDE = (0,200,0)
# Variaveis para os retangulos
verde_rect = pygame.Rect(150,20,40,40)
amarelo_rect = pygame.Rect(150,100,40,40)
vermelho_rect = pygame.Rect(200,20,40,40)
azul_rect = pygame.Rect(200,100,40,40)

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('GENIUS')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        # PERGUNTAR DA POSIÇÃO
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            print(pos)
            if verde_rect.collidepoint(pos):
                print("Verde")
            if amarelo_rect.collidepoint(pos):
                print("Amarelo")
            if vermelho_rect.collidepoint(pos):
                print("Vermelho")
            if azul_rect.collidepoint(pos):
                print("Azul")

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
