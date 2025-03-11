import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Throw Master")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # gameDisplay.fill("Black")

    # pygame.display.flip()

    clock.tick(60)

pygame.quit()
