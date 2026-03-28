import pygame, entities, Room
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
# Todo: temp room test
walls = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]
room = Room.Room(None, None, None, None, walls, None, player)

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
        player.move(0, -PLAYERSPEED, room.walls)
    if keys[pygame.K_s]:
        player.move(0, PLAYERSPEED, room.walls)
    if keys[pygame.K_d]:
        player.move(PLAYERSPEED, 0, room.walls)
    if keys[pygame.K_a]:
        player.move(-PLAYERSPEED, 0, room.walls)

    # -------------------- Game Logic --------------------


    # -------------------- Draw --------------------
    surface.fill((0, 0, 128))
    player.draw(surface)

    # Todo: temp wall drawing
    for y in range(len(room.walls)):
        for x in range(len(room.walls)):
            if room.walls[y][x] == 1:
                pygame.draw.rect(surface, (128, 128, 128), (x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE))

    # ----------------------------------------
    screen.blit(surface, ( (SCREENX / 2) - (GAMEX / 2), (SCREENY / 2) - (GAMEY / 2) ))
    pygame.display.flip()
    clock.tick(60)

# ======================================================================
pygame.quit()