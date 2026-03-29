import pygame
from constants import *

player_spritesheet = pygame.image.load("Images/playerSprites.png")
basic_enemy_spritesheet = pygame.image.load("Images/basicEnemySprites.png")

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
            xcoll = (enemy.x < self.x < enemy.x + enemy.xsize) or (enemy.x < self.x + PLAYERSIZE < enemy.x + enemy.xsize)
            ycoll = (enemy.y < self.y < enemy.y + enemy.ysize) or (enemy.y < self.y + PLAYERSIZE < enemy.y + enemy.ysize)
            if xcoll and ycoll:
                return True

    def move(self, x, y, room):
        self.x += x
        self.y += y

        if room.entities is not None:
            if self.collides_with_enemy(room.entities):
                self.x, self.y = room.spawn

        if self.collides_with_wall(room.walls):
            self.x -= x
            self.y -= y


    def change_room(self, room, levels):
        if self.y <= 0 + PLAYERSPEED:
            self.y = GAMEY - (PLAYERSPEED + PLAYERSIZE)
            return levels[room.adjacent_rooms["Up"]]

        if self.y + PLAYERSIZE + PLAYERSPEED >= GAMEY:
            self.y = 0 + PLAYERSPEED
            return levels[room.adjacent_rooms["Down"]]

        if self.x <= 0 + PLAYERSPEED:
            self.x = GAMEX - (PLAYERSPEED + PLAYERSIZE)
            return levels[room.adjacent_rooms["Left"]]

        if self.x + PLAYERSIZE + PLAYERSPEED >= GAMEX:
            self.x = 0 + PLAYERSPEED
            return levels[room.adjacent_rooms["Right"]]

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, surface):
        player_sprite = player_spritesheet.subsurface((0, 0, 12, 12))
        player_sprite = pygame.transform.scale(player_sprite, (PLAYERSIZE, PLAYERSIZE))
        surface.blit(player_sprite, (self.x, self.y))

class Enemy(Entity):
    def __init__(self, x, y, xsize, ysize):
        super().__init__(x, y)
        self.xsize = xsize
        self.ysize = ysize

    def draw(self, surface):
        basic_enemy_sprite = basic_enemy_spritesheet.subsurface((0, 0, 16, 16))
        basic_enemy_sprite = pygame.transform.scale(basic_enemy_sprite, (PLAYERSIZE, PLAYERSIZE))
        surface.blit(basic_enemy_sprite, (self.x, self.y))

    def move(self, x, y, room):
        self.x += x
        self.y += y