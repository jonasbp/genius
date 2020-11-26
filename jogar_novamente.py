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
import assets

def jogar_novamente(decisao,window,score):
        while True:
            #Identifica em que botão o usuário clicou
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if botao.collidepoint(pos):
                        window.fill((0, 0, 0))
                        assets.assets["SOMMENU"].play()
                        return True
                    elif botao_sair.collidepoint(pos):
                        assets.assets["SOMMENU"].play()
                        return False
            
            window.fill((0, 0, 0))

            #Botão jogar novamente
            botao = pygame.draw.rect(window, (255, 140, 0), (100, 175, 300, 50))
            text_surface = assets.assets['play_again_font'].render("Jogar novamente", True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (250,  190)
            window.blit(text_surface, text_rect)
            #Botão sair
            botao_sair = pygame.draw.rect(window, (255, 140, 0), (125, 275, 250, 50))
            text_surface = assets.assets['play_again_font'].render("Sair", True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (250,  290)
            window.blit(text_surface, text_rect)
            #Decide entre se o jogador perdeu ou ganhou
            if decisao=="derrota":
                #Exibe mensagem "Você perdeu"
                texto_surface = assets.assets['score_font'].render("Você perdeu", True, (255, 255, 255))
                texto_rect = text_surface.get_rect()
                texto_rect.midtop = (125,  60)
                window.blit(texto_surface, texto_rect)
                #Mostra a pontuação
                text_surface = assets.assets['score_font'].render("{:08d}".format(score), True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.midtop = (250,  140)
                window.blit(text_surface, text_rect)
                texto_surface = assets.assets['score_font'].render("Pontuação:", True, (255, 255, 255))
                texto_rect = text_surface.get_rect()
                texto_rect.midtop = (230,  100)
                window.blit(texto_surface, texto_rect)
            elif decisao=="vitoria":
                #Exibe a mensagem "Você ganhou"
                texto_surface = assets.assets['score_font'].render("Você ganhou", True, (255, 255, 255))
                texto_rect = text_surface.get_rect()
                texto_rect.midtop = (130,  60)
                window.blit(texto_surface, texto_rect)

            pygame.display.update()