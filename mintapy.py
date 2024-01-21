
import pygame

# inicializálás - kötelező elem
pygame.init()

# játékablak létrehozása
# dupla () --> "tuple" Több érték tárolása egy változón belül
ablak = pygame.display.set_mode((600, 300))

# - ablak címének megváltoztatása
pygame.display.set_caption('Mintapy')

# gameloop és eseményei
fut = True
while fut:
    for esemény in pygame.event.get():      # bejárjuk az összes történő eseményt
        if esemény.type == pygame.QUIT:     # ha az esemény bekövetkezik a while ciklusunk(gameloopunk) véget ér
            fut = False
    pygame.display.update()     # játék ablak frissítése

# quit függvény hívása
pygame.quit()
