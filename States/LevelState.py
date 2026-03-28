from States.State import state
import pygame, entities
from constants import *
from levels import *

class LevelState(state):
    def __init__(self, surface, level):
        super().__init__("LevelState", surface)

        self.player = entities.Player(TILESIZE * 2, TILESIZE * 2)
        self.room = None

        if (level == "Level 1"):
            self.room = lvl1Start
        # elif (level == "Level 2"):
        #     self.room = lvl2
        # elif (level == "Level 3"):
        #     self.room = lvl3
        # elif (level == "Level 4"):
        #     self.room = lvl4
        # elif (level == "Level 5"):
        #     self.room = lvl5
        self.paused = False

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(0, -PLAYERSPEED, self.room.walls)
        if keys[pygame.K_s]:
            self.player.move(0, PLAYERSPEED, self.room.walls)
        if keys[pygame.K_d]:
            self.player.move(PLAYERSPEED, 0, self.room.walls)
        if keys[pygame.K_a]:
            self.player.move(-PLAYERSPEED, 0, self.room.walls)

    def update(self):
        newRoom = self.player.change_room(self.room, lvl1)
        if newRoom is not None:
            self.room = newRoom
        
        self.surface.fill((0, 0, 128))

        self.room.draw(self.surface)
        self.player.draw(self.surface)

        