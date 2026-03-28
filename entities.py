import pygame
from constants import *

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def collides_with_enemy(self, enemies):
        for enemy in enemies:
            xcoll = (enemy.x < self.x < enemy.x + enemy.size) or (enemy.x < self.x + PLAYERSIZE < enemy.x + enemy.size)
            ycoll = (enemy.y < self.y < enemy.y + enemy.size) or (enemy.y < self.y + PLAYERSIZE < enemy.y + enemy.size)
            if xcoll and ycoll:
                return True

    def move(self, x, y, walls, enemies):
        self.x += x
        self.y += y

        if enemies is not None:
            if self.collides_with_enemy(enemies):
                print("Hit an enemy")

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

    def draw(self, surface):
        # Todo: temporary
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, PLAYERSIZE, PLAYERSIZE))

class Enemy(Entity):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.size = size

    def draw(self, surface):
        # Todo: temporary
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, self.size, self.size))