import pygame

from levels import lvl1Start, lvl1Down, lvl1Left, lvl2Down, lvl1Right, lvl2Right, lvl2Left, lvl3Right, lvl3Left, \
    lvl3Down

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
title = pygame.image.load("Images/title.png")
smol_title = pygame.transform.scale(title, (330, 100))
text_sheet = pygame.image.load("Images/text.png")
font = pygame.font.Font("fonts/Jersey10-Regular.ttf", 36)
font2 = pygame.font.Font("fonts/Jersey10-Regular.ttf", 20)
txt_color = (0, 93, 182)
pygame.mixer.init()
music = pygame.mixer.Sound('Sounds/music.wav')
music.play(loops=-1)

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
        screen.blit(title, (SCREENX // 2 - 330, 100))

    elif state_manager.state.name == "CreditsState":
        screen.blit(dark_Title_BG, (0, 0))
        screen.blit(smol_title, (SCREENX // 2 - 165, 75))
        cred1 = font2.render("Code: Adriel Rosado and Joshuem Medina", True, (255, 255, 255))
        cred2 = font2.render("Level Design: Adriel Rosado", True, (255, 255, 255))
        cred3 = font2.render("Art: Joshuem Medina", True, (255, 255, 255))
        cred41 = font2.render("SFX: Retro video game sfx - Bounce by OwlStorm -- https://freesound.org/s/404769/ -- License: Creative Commons 0", True, (255, 255, 255))
        cred42 = font2.render("Soft UI Button Click by Jummit -- https://freesound.org/s/528561/ -- License: Creative Commons 0", True, (255, 255, 255))
        cred43 = font2.render("Glitch Plonks 1 by tripjazz -- https://freesound.org/s/509069/ -- License: Creative Commons 0", True, (255, 255, 255))
        cred44 = font2.render("Completed.wav by Kenneth_Cooney -- https://freesound.org/s/609336/ -- License: Creative Commons 0", True, (255, 255, 255))
        cred45 = font2.render("8 bit game loop 011  simple mix 4 long 120 bpm.wav by josefpres -- https://freesound.org/s/657667/ -- License: Creative Commons 0", True, (255, 255, 255))
        cred5 = font2.render("Font: Jersey 10 by Sarah Cadigan-Fried -- https://fonts.google.com/specimen/Jersey+10 -- License: SIL Open Font License, Version 1.1", True, (255, 255, 255))
        cred6 = font2.render("Made with Pygame", True, (255, 255, 255))
        screen.blit(cred1, (200, 200))
        screen.blit(cred2, (200, 235))
        screen.blit(cred3, (200, 270))
        screen.blit(cred41, (200, 305))
        screen.blit(cred42, (200, 330))
        screen.blit(cred43, (200, 355))
        screen.blit(cred44, (200, 380))
        screen.blit(cred45, (200, 405))
        screen.blit(cred5, (200, 440))
        screen.blit(cred6, (200, 475))


    elif state_manager.state.name == "LevelState":
        screen.blit(lvl_bgbg, (0, 0))
    else:
        screen.blit(title_BG, (0, 0))
        screen.blit(title, (SCREENX // 2 - 330, 100))

    if state_manager.state.name == "LevelState":
        screen.blit(surface, ( (SCREENX / 2) - (GAMEX / 2), (SCREENY / 2) - (GAMEY / 2) ))

    if state_manager.state.name == "LevelState":
        stt = state_manager.state
        if stt.room.boy:
            text_sprite = text_sheet.subsurface((0, 0, 12, 12))
            txt_color = (0, 93, 182)
        else:
            text_sprite = text_sheet.subsurface((12, 0, 12, 12))
            txt_color = (241, 52, 132)
        text_sprite = pygame.transform.scale(text_sprite, (TILESIZE, TILESIZE))

        # Messages left
        text1 = font.render("Messages Left:", True, (255, 255, 255))
        screen.blit(text1, (75, 100))
        if stt.player.MessageIDS % 2 != 0:
            screen.blit(text_sprite, (75, 150))
            msg1 = font.render("Text 1", True, (255, 255, 255))
            screen.blit(msg1, (135, 155))
        if stt.player.MessageIDS % 3 != 0:
            screen.blit(text_sprite, (75, 175+TILESIZE))
            msg2 = font.render("Text 2", True, (255, 255, 255))
            screen.blit(msg2, (135, 180+TILESIZE))
        if stt.player.MessageIDS % 5 != 0:
            screen.blit(text_sprite, (75, 200+TILESIZE*2))
            msg3 = font.render("Text 3", True, (255, 255, 255))
            screen.blit(msg3, (135, 205+TILESIZE*2))


        txt_cntnt1 = ""
        txt_cntnt2 = ""
        txt_cntnt3 = ""
        if stt.room in levels.lvl1.values():
            txt_cntnt1 = lvl1Left.collectable.text
            txt_cntnt2 = lvl1Down.collectable.text
            txt_cntnt3 = lvl1Right.collectable.text
        elif stt.room in levels.lvl2.values():
            txt_cntnt1 = lvl2Right.collectable.text
            txt_cntnt2 = lvl2Left.collectable.text
            txt_cntnt3 = lvl2Down.collectable.text
        elif stt.room in levels.lvl3.values():
            txt_cntnt1 = lvl3Right.collectable.text
            txt_cntnt2 = lvl3Left.collectable.text
            txt_cntnt3 = lvl3Down.collectable.text

        # Messages collected
        text2 = font.render("Messages Collected:", True, (255, 255, 255))
        screen.blit(text2, ((SCREENX / 2) + (GAMEX / 2) + 55, 100))
        if stt.player.MessageIDS % 2 == 0:
            msg4 = font2.render(txt_cntnt1, True, txt_color)
            screen.blit(msg4, ((SCREENX / 2) + (GAMEX / 2) + 5, 155))
        if stt.player.MessageIDS % 3 == 0:
            msg5 = font2.render(txt_cntnt2, True, txt_color)
            screen.blit(msg5, ((SCREENX / 2) + (GAMEX / 2) + 5, 155+TILESIZE))
        if stt.player.MessageIDS % 5 == 0:
            msg6 = font2.render(txt_cntnt3, True, txt_color)
            screen.blit(msg6, ((SCREENX / 2) + (GAMEX / 2) + 5, 155+TILESIZE*2))


    state_manager.update(events)

    # ----------------------------------------
    pygame.display.flip()
    clock.tick(FPS)

# ============================================================
pygame.quit()