import pygame

PIROS = (255, 0, 0)
KEK = (0, 0, 255)
SZIN = (54, 183, 93)
FEHER = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Mintapy')

háttér_színe = SZIN

fut = True
while fut:
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:     
            fut = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: 
                háttér_színe = PIROS
            elif event.key == pygame.K_t: 
                háttér_színe = KEK
            elif event.key == pygame.K_z:
                háttér_színe = SZIN

    screen.fill(háttér_színe)

    pygame.draw.circle(screen, FEHER, (400, 300), 100)
    pygame.draw.rect(screen, (255, 0, 0), (30, 30, 150, 75))
    pygame.draw.ellipse(screen, KEK, (50, 50, 200, 75))
    pygame.draw.polygon(screen, KEK, [(120, 90), (120,200), (200, 90)])

    pygame.display.update()     


pygame.quit()
