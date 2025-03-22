'''
main.py

This is the main entry point for the Throw Master game.

Responsibilities:
- Initializes Pygame and the game window.
- Loads assets (images and icons) from the assets module.
- Manages the game loop, including player input, drawing, and screen updates.
'''

import sys
import pygame
from config import *
from assets import load_assets
from draw_img import draw_bg, draw_ground, draw_player

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Throw Master")
clock = pygame.time.Clock()

bg_images, ground_img, player_img = load_assets()
bg_width = bg_images[0].get_width()
ground_width = ground_img.get_width()
ground_height = ground_img.get_height()

def main():
    """
    The main loop of the game.

    Continuously handles:
    - Timing via FPS control.
    - Drawing background, ground, and player layers.
    - Scrolling the screen based on user key inputs.
    - Handling quit events.
    """
    scroll = 0
    running = True

    while running:
        clock.tick(FPS)

        # Draw
        draw_bg(gameDisplay, bg_images, scroll, bg_width)
        draw_ground(gameDisplay, ground_img, scroll, ground_width, ground_height, SCREEN_HEIGHT)
        draw_player(gameDisplay, player_img, PLAYER_X, PLAYER_Y)
        pygame.display.update()

        # Input Handling
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and scroll > 0:
            scroll -= SCROLL_SPEED
        elif key[pygame.K_RIGHT] and scroll < MAX_SCROLL:
            scroll += SCROLL_SPEED

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
