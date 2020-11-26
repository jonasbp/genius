# PROJETO FINAL DESIGN DE SOFTWARE
#INICIALIZAR O JOGO NESSE ARQUIVO
# JOGO GENIUS
# INSPER 2020
# Jonas Bonfá Pelegrina,Layne Pereira Silva,Giancarlo Vanoni Ruggiero

# CONVERSÃO DE NÚMERO PARA COR
# 0 - Verde
# 1 - Vermelho
# 2 - Amarelo
# 3 - Azul
import pygame
from jogo import principal

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('GENIUS')

principal(window) # Executa a função principal do jogo

pygame.quit()  # Função do PyGame que finaliza os recursos utilizados