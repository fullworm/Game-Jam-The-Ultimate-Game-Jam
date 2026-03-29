import pygame, entities, levels
from constants import *
from States.StateManager import StateManager

# -------------------- Setup --------------------
pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
surface = pygame.Surface(GAMESIZE)

state_manager = StateManager(screen, surface)

pygame.display.set_caption("Super Awesome Omega game")

clock = pygame.time.Clock()
running = True

# ============================== GAME LOOP ==============================
while running:

    # -------------------- Events --------------------
    events = pygame.event.get()
    for event in events:
        # Quit
        if event.type == pygame.QUIT:
            running = False

        # Key Press

    screen.blit(surface, ( (SCREENX / 2) - (GAMEX / 2), (SCREENY / 2) - (GAMEY / 2) ))
    state_manager.update(events)

    # ----------------------------------------
    pygame.display.flip()
    clock.tick(FPS)

# ============================================================
pygame.quit()