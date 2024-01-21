import pygame

pygame.init()

ablak = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Alapok')


fut = True
while fut:
    for esemény in pygame.event.get():
        fut = False
    pygame.display.update()

pygame.quit()
