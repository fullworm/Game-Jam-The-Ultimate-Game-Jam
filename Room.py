import pygame
from constants import *

wall_spritesheet = pygame.image.load("Images/wall.png")

class Room:
    def __init__(self, adjacent_rooms, walls, enemies, spawn, collectable = None, terminal = None):
        self.adjacent_rooms = adjacent_rooms
        self.walls: list[list] = walls
        self.entities: list = enemies
        self.spawn = spawn
        self.collectable = collectable
        self.terminal = terminal

    def draw(self, surface):
        for y in range(len(self.walls)):
            for x in range(len(self.walls)):
                if self.walls[y][x] == 1:
                    left, right, up, down = 1, 1, 1, 1
                    if x == 0:
                        left = 0
                    elif self.walls[y][x-1] == 0:
                        left = 0

                    if x == len(self.walls[0]) - 1:
                        right = 0
                    elif self.walls[y][x+1] == 0:
                        right = 0

                    if y == 0:
                        up = 0
                    elif self.walls[y-1][x] == 0:
                        up = 0

                    if y == len(self.walls) - 1:
                        down = 0
                    elif self.walls[y+1][x] == 0:
                        down = 0


                    if (left, right, up, down) == (0, 0, 0, 0):
                        wall_sprite = wall_spritesheet.subsurface((0, 0, 8, 8))
                    elif (left, right, up, down) == (0, 0, 0, 1):
                        wall_sprite = wall_spritesheet.subsurface((8, 0, 8, 8))
                    elif (left, right, up, down) == (1, 0, 0, 0):
                        wall_sprite = wall_spritesheet.subsurface((16, 0, 8, 8))
                    elif (left, right, up, down) == (0, 0, 1, 0):
                        wall_sprite = wall_spritesheet.subsurface((24, 0, 8, 8))
                    elif (left, right, up, down) == (0, 1, 0, 0):
                        wall_sprite = wall_spritesheet.subsurface((32, 0, 8, 8))
                    elif (left, right, up, down) == (1, 0, 0, 1):
                        wall_sprite = wall_spritesheet.subsurface((40, 0, 8, 8))
                    elif (left, right, up, down) == (1, 0, 1, 0):
                        wall_sprite = wall_spritesheet.subsurface((48, 0, 8, 8))
                    elif (left, right, up, down) == (0, 1, 1, 0):
                        wall_sprite = wall_spritesheet.subsurface((56, 0, 8, 8))
                    elif (left, right, up, down) == (0, 1, 0, 1):
                        wall_sprite = wall_spritesheet.subsurface((64, 0, 8, 8))
                    elif (left, right, up, down) == (0, 0, 1, 1):
                        wall_sprite = wall_spritesheet.subsurface((72, 0, 8, 8))
                    elif (left, right, up, down) == (1, 1, 0, 0):
                        wall_sprite = wall_spritesheet.subsurface((80, 0, 8, 8))
                    elif (left, right, up, down) == (1, 1, 0, 1):
                        wall_sprite = wall_spritesheet.subsurface((88, 0, 8, 8))
                    elif (left, right, up, down) == (1, 0, 1, 1):
                        wall_sprite = wall_spritesheet.subsurface((96, 0, 8, 8))
                    elif (left, right, up, down) == (1, 1, 1, 0):
                        wall_sprite = wall_spritesheet.subsurface((104, 0, 8, 8))
                    elif (left, right, up, down) == (0, 1, 1, 1):
                        wall_sprite = wall_spritesheet.subsurface((112, 0, 8, 8))
                    elif (left, right, up, down) == (1, 1, 1, 1):
                        wall_sprite = wall_spritesheet.subsurface((120, 0, 8, 8))

                    wall_sprite = pygame.transform.scale(wall_sprite, (TILESIZE, TILESIZE))
                    surface.blit(wall_sprite, (x * TILESIZE, y * TILESIZE))
    
    def reset(self, player = None):
            if self.collectable is not None:
                self.collectable.active = True
                self.collectable.timer = 0

            if self.terminal is not None:
                self.terminal.done = False

            self.reset_enemy()
            if player is not None:
                player.x, player.y = self.spawn
    def reset_enemy(self):
        if self.entities is not None:
            for enemy in self.entities:
                enemy.reset()