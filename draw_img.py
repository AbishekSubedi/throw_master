"""
draw_img.py

This module contains drawing functions for the game, such as rendering the background,
ground, and player onto the display surface. Each function is designed to modularize
the rendering logic and keep the main game loop clean and maintainable.
"""

def draw_bg(display, bg_images: list, scroll: int, bg_width: int) -> None:
    """
    Draws the parallax scrolling background layers.

    Parameters:
        display (Surface): The main game display surface.
        bg_images (list): List of background images ordered by depth.
        scroll (int): The current scroll value controlling the view offset.
        bg_width (int): The width of a single background image layer.
    """
    for x in range(5):
        speed = 1
        for img in bg_images:
            display.blit(img, ((x * bg_width) - scroll * speed, 0))
            speed += 0.2

def draw_ground(display, ground_img, scroll: int, ground_width: int, ground_height: int, screen_height: int) -> None:
    """
    Draws the repeating ground tiles for the game world.

    Parameters:
        display (Surface): The main game display surface.
        ground_img (Surface): The image to use for the ground tiles.
        scroll (int): The current scroll value controlling the view offset.
        ground_width (int): Width of a single ground tile.
        ground_height (int): Height of the ground image.
        screen_height (int): Height of the game window to align the ground vertically.
    """
    for x in range(15):
        display.blit(ground_img, ((x * ground_width) - scroll * 2.2, screen_height - ground_height))

def draw_player(display, player_img, x: int, y: int) -> None:
    """
    Draws the player character at the specified coordinates.

    Parameters:
        display (Surface): The main game display surface.
        player_img (Surface): The player's image to render.
        x (int): The horizontal position of the player.
        y (int): The vertical position of the player.
    """
    display.blit(player_img, (x, y))


def draw_spear(display, spear_img, spear_x: int, spear_y: int) -> None:
    """
    Draws the spear at the specified coordinates.

    Parameters:
        display (Surface): The main game display surface.
        spear_img (Surface): The spear image to render.
        x (int): The horizontal position of the spear.
        y (int): The vertical position of the spear.
    """
    display.blit(spear_img, (spear_x, spear_y))
