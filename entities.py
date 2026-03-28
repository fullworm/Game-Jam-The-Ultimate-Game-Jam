import pygame
from constants import *

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        # Todo: temporary
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, PLAYERSIZE, PLAYERSIZE))

    def collides_with_wall(self, walls):
        if (self.y + PLAYERSIZE) // TILESIZE >= len(walls) or (self.x + PLAYERSIZE) // TILESIZE >= len(walls[0]):
            return True
        if walls[self.y // TILESIZE][self.x // TILESIZE] == 1:
            return True
        if walls[(self.y + PLAYERSIZE) // TILESIZE][self.x // TILESIZE] == 1:
            return True
        if walls[self.y // TILESIZE][(self.x + PLAYERSIZE) // TILESIZE] == 1:
            return True
        if walls[(self.y + PLAYERSIZE) // TILESIZE][(self.x + PLAYERSIZE) // TILESIZE] == 1:
            return True
        return False

    def move(self, x, y, walls):
        self.x += x
        self.y += y

        if self.collides_with_wall(walls):
            self.x -= x
            self.y -= y

    def change_room(self, room, levels):
        if self.y <= 0:
            self.y = GAMEY - (PLAYERSPEED + PLAYERSIZE)
            return levels[room.adjacent_rooms["Up"]]

        if self.y + PLAYERSIZE + PLAYERSPEED >= GAMEY:
            self.y = 0 + PLAYERSPEED
            return levels[room.adjacent_rooms["Down"]]

        if self.x <= 0:
            self.x = GAMEX - (PLAYERSPEED + PLAYERSIZE)
            return levels[room.adjacent_rooms["Left"]]

        if self.x + PLAYERSIZE + PLAYERSPEED >= GAMEX:
            self.x = 0 + PLAYERSPEED
            return levels[room.adjacent_rooms["Right"]]

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)