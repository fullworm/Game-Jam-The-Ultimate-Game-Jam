import pygame
from constants import *

class Room:
    def __init__(self, adjacent_rooms, walls, enemies):
        self.adjacent_rooms = adjacent_rooms
        self.walls: list[list] = walls
        self.entities: list = enemies

    def draw(self, surface):
        # Todo: temp
        for y in range(len(self.walls)):
            for x in range(len(self.walls)):
                if self.walls[y][x] == 1:
                    pygame.draw.rect(surface, (128, 128, 128), (x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE))