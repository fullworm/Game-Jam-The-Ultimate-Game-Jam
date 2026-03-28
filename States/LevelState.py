from States.State import state
import pygame, entities
from constants import *
from levels import *
from pygame_widgets.button import ButtonArray
from sys import exit

class LevelState(state):
    def __init__(self, surface, level):
        super().__init__("LevelState", surface)

        self.player = entities.Player(TILESIZE * 2, TILESIZE * 2)
        self.room = None
        self.paused = False

        self.pauseMenu = ButtonArray(
            self.surface,
            (GAMEX - 500) // 2,
            (GAMEY - 500) // 2,
            500,
            500,
            (3,1), 
            border = 0,
            texts= ("Continue", "Select Level", "Exit game"),
            onClicks= (lambda: self.toggle_pause(), lambda: self.set_next_state("LevelChooseState"), lambda: exit())
        )
        self.pauseMenu._hidden = True
        if level == "Level 1":
            self.room = lvl1Start
        # elif (level == "Level 2"):
        #     self.room = lvl2
        # elif (level == "Level 3"):
        #     self.room = lvl3
        # elif (level == "Level 4"):
        #     self.room = lvl4
        # elif (level == "Level 5"):
        #     self.room = lvl5

    def player_input(self):
        if (not self.paused):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move(0, -PLAYERSPEED, self.room.walls, self.room.entities)
            if keys[pygame.K_s]:
                self.player.move(0, PLAYERSPEED, self.room.walls, self.room.entities)
            if keys[pygame.K_d]:
                self.player.move(PLAYERSPEED, 0, self.room.walls, self.room.entities)
            if keys[pygame.K_a]:
                self.player.move(-PLAYERSPEED, 0, self.room.walls, self.room.entities)

    def toggle_pause(self):
        self.paused = not self.paused
        if self.pauseMenu is not None:
            self.pauseMenu._hidden = not self.paused

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.toggle_pause()
            

    def update(self, events):
        newRoom = self.player.change_room(self.room, lvl1)
        if newRoom is not None:
            self.room = newRoom
        
        self.surface.fill((0, 0, 128))

        self.room.draw(self.surface)
        if self.room.entities is not None:
            for enemy in self.room.entities:
                enemy.draw(self.surface)
        self.player.draw(self.surface)
    def clean_up(self):
        self.pauseMenu.hide()
        self.pauseMenu.disable
        