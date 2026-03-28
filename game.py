import pygame, entities, levels
from constants import *

# -------------------- Setup --------------------
pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
surface = pygame.Surface(GAMESIZE)

pygame.display.set_caption("Super Awesome Omega game")

clock = pygame.time.Clock()
running = True

# -------------------- Loading --------------------
player = entities.Player(TILESIZE * 2, TILESIZE * 2)
room = levels.lvl1Start

# ============================== GAME LOOP ==============================
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
        player.move(0, -PLAYERSPEED, room.walls)
    if keys[pygame.K_s]:
        player.move(0, PLAYERSPEED, room.walls)
    if keys[pygame.K_d]:
        player.move(PLAYERSPEED, 0, room.walls)
    if keys[pygame.K_a]:
        player.move(-PLAYERSPEED, 0, room.walls)

    # -------------------- Game Logic --------------------
    newRoom = player.change_room(room, levels.lvl1)
    if newRoom is not None:
        room = newRoom

    # -------------------- Draw --------------------
    surface.fill((0, 0, 128))

    room.draw(surface)
    player.draw(surface)

    # ----------------------------------------
    screen.blit(surface, ( (SCREENX / 2) - (GAMEX / 2), (SCREENY / 2) - (GAMEY / 2) ))
    pygame.display.flip()
    clock.tick(60)

# ============================================================
pygame.quit()