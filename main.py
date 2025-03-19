'''Javeline Throwing Game Made from Pygame'''

import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

background = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_img = pygame.image.load("assets/player.png")

icon_img = pygame.image.load("assets/javelin-throw.png")

pygame.display.set_caption("Throw Master")
pygame.display.set_icon(icon_img)

PLAYER_X = 30
PLAYER_Y = 380
PLAYER_X_CHNAGE = 0
player_rect = player_img.get_rect(topleft=(PLAYER_X, PLAYER_Y))

RUNNING = True

def player(x: int, y: int) -> None:
    gameDisplay.blit(player_img, (x, y))

while RUNNING:

    gameDisplay.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER_X_CHNAGE = -1
            elif event.key == pygame.K_RIGHT:
                PLAYER_X_CHNAGE = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PLAYER_X_CHNAGE = 0

    player_rect.x += PLAYER_X_CHNAGE

    if player_rect.x <= 0:
        player_rect.x = 0
    elif player_rect.x >= SCREEN_WIDTH - player_rect.width:
        player_rect.x = SCREEN_WIDTH - player_rect.width

    player(player_rect.x, player_rect.y)

    pygame.display.update()

pygame.quit()
