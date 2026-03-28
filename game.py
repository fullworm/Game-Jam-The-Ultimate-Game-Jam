import pygame, entities
from constants import *

# -------------------- Setup --------------------
pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
surface = pygame.Surface(GAMESIZE)

pygame.display.set_caption("Super Awesome Omega game")

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

    # Key Hold
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.move(0, -PLAYERSPEED)
    if keys[pygame.K_s]:
        player.move(0, PLAYERSPEED)
    if keys[pygame.K_d]:
        player.move(PLAYERSPEED, 0)
    if keys[pygame.K_a]:
        player.move(-PLAYERSPEED, 0)

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