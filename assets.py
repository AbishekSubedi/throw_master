"""
assets.py

This module handles the loading of image assets used in the game, including background layers,
the ground tile, the player character, and the game icon.
"""

import pygame

def load_assets() -> tuple:
    """
    Loads all graphical assets required for the game.

    Returns:
        tuple: A tuple containing:
            - bg_images (list): A list of 5 background layer images.
            - ground_img (Surface): The image used for the ground layer.
            - player_img (Surface): The player character image.
    """
    bg_images = [pygame.image.load(
        f"assets/plx-{i}.png").convert_alpha() for i in range(1, 6)]
    ground_img = pygame.image.load("assets/ground.png").convert_alpha()
    player_img = pygame.image.load("assets/player.png")
    icon_img = pygame.image.load("assets/javelin-throw.png")
    spear_img = pygame.image.load("assets/spear.png")
    spear_img = pygame.transform.scale(spear_img, (100, 80))
    spear_img = pygame.transform.rotate(spear_img, -16) # 164)
    pygame.display.set_icon(icon_img)
    return bg_images, ground_img, player_img, spear_img
