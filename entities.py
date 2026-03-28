import pygame
from constants import *

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        # Todo: temporary
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, TILESIZE, TILESIZE))

    def move(self, x, y):
        self.x += x
        self.y += y

        if (-1 < self.x < GAMEX) is not True or (-1 < self.y < GAMEY) is not True:
            self.x -= x
            self.y -= y


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)