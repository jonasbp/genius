import pygame
from jogo import principal

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('GENIUS')

principal(window) # Executa a função principal do jogo

pygame.quit()  # Função do PyGame que finaliza os recursos utilizados