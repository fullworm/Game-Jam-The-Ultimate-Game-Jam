import pygame

pygame.init()
pygame.font.init()

import entities, levels

from States.State import state
from constants import *
from States.StateManager import StateManager

# -------------------- Setup --------------------

screen = pygame.display.set_mode(SCREENSIZE)
surface = pygame.Surface(GAMESIZE)

state_manager = StateManager(screen, surface)

pygame.display.set_caption("Super Awesome Omega game")

clock = pygame.time.Clock()
running = True


titleBG = pygame.image.load("Images/titleBG.png")
title_BG = pygame.transform.scale(titleBG, (SCREENX, SCREENY))
darkTitleBG = pygame.image.load("Images/darkTitleBG.png")
dark_Title_BG = pygame.transform.scale(darkTitleBG, (SCREENX, SCREENY))
lvlbgbg = pygame.image.load("Images/lvlbgbg.png")
lvl_bgbg = pygame.transform.scale(lvlbgbg, (SCREENX, SCREENY))

# ============================== GAME LOOP ==============================
while running:

    # -------------------- Events --------------------
    events = pygame.event.get()
    for event in events:
        # Quit
        if event.type == pygame.QUIT:
            running = False

        # Key Press
    # -------------------- Draw --------------------

    if state_manager.state.name == "LevelChooseState":
        screen.blit(dark_Title_BG, (0, 0))
    elif state_manager.state.name == "LevelState":
        screen.blit(lvl_bgbg, (0, 0))
    else:
        screen.blit(title_BG, (0, 0))

    if state_manager.state.name != "MenuState" and state_manager.state.name != "LevelChooseState":
        screen.blit(surface, ( (SCREENX / 2) - (GAMEX / 2), (SCREENY / 2) - (GAMEY / 2) ))


    state_manager.update(events)

    # ----------------------------------------
    pygame.display.flip()
    clock.tick(FPS)

# ============================================================
pygame.quit()