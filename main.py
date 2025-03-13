'''Javeline Throwing Game Made from Pygame'''

import pygame

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

background = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_img = pygame.image.load("assets/player.png")
player_img = pygame.transform.scale(player_img, (300, 300))

player_rect = player_img.get_rect()
player_rect.bottomleft = (0, 0)

pygame.display.set_caption("Throw Master")

RUNNING = True

while RUNNING:

    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(background, (0, 0))

    gameDisplay.blit(player_img, player_rect.topleft)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player_rect.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        player_rect.move_ip(1, 0)
    elif key[pygame.K_UP]:
        player_rect.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player_rect.move_ip(0, 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    pygame.display.update()

pygame.quit()
