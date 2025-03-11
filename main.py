'''Javeline Throwing Game Made from Pygame'''

import pygame

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((350, 250, 50, 50))

pygame.display.set_caption("Throw Master")

RUNNING = True

while RUNNING:

    gameDisplay.fill((0, 0, 0))

    pygame.draw.rect(gameDisplay, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        player.move_ip(1, 0)
    elif key[pygame.K_UP]:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player.move_ip(0, 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    pygame.display.update()

pygame.quit()
