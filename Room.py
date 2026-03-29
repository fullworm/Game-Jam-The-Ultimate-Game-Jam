import pygame
from constants import *

wall_sprite = pygame.image.load("Images/wall.png")
wall_sprite = pygame.transform.scale(wall_sprite, (TILESIZE, TILESIZE))

class Room:
    def __init__(self, adjacent_rooms, walls, enemies, spawn, collectable = None):
        self.adjacent_rooms = adjacent_rooms
        self.walls: list[list] = walls
        self.entities: list = enemies
        self.spawn = spawn
        self.collectable = collectable

    def draw(self, surface):
        # Todo: temp
        for y in range(len(self.walls)):
            for x in range(len(self.walls)):
                if self.walls[y][x] == 1:
                    surface.blit(wall_sprite, (x * TILESIZE, y * TILESIZE))