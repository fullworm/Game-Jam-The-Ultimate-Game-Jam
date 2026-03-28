import pygame
from constants import *

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        # Todo: temporary
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, CHARACTERSIZE, CHARACTERSIZE))

    # Todo: these use walls and I dont like it
    def collides(self, walls):
        if walls[self.y // TILESIZE][self.x // TILESIZE] == 1:
            return True
        if walls[(self.y + CHARACTERSIZE) // TILESIZE][self.x // TILESIZE] == 1:
            return True
        if walls[self.y // TILESIZE][(self.x + CHARACTERSIZE) // TILESIZE] == 1:
            return True
        if walls[(self.y + CHARACTERSIZE) // TILESIZE][(self.x + CHARACTERSIZE) // TILESIZE] == 1:
            return True
        return False

    def move(self, x, y, walls):
        self.x += x
        self.y += y

        if self.collides(walls):
            self.x -= x
            self.y -= y


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)