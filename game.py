import pygame, entities
from constants import *

# -------------------- Setup --------------------
pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
surface = pygame.Surface(GAMESIZE)

clock = pygame.time.Clock()
running = True

# -------------------- Loading --------------------
player = entities.Player(0, 0)

# ========================= GAME LOOP =============================================
while running:

    # -------------------- Events --------------------
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            running = False

        # Key Press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move(0, -TILESIZE)
            if event.key == pygame.K_s:
                player.move(0, TILESIZE)
            if event.key == pygame.K_d:
                player.move(TILESIZE, 0)
            if event.key == pygame.K_a:
                player.move(-TILESIZE, 0)

    # -------------------- Game Logic --------------------


    # -------------------- Draw --------------------
    surface.fill((0, 0, 128))
    player.draw(surface)

    # ----------------------------------------
    screen.blit(surface, ( (SCREENX / 2) - (GAMEX / 2), (SCREENY / 2) - (GAMEY / 2) ))
    pygame.display.flip()
    clock.tick(60)

# ======================================================================
pygame.quit()