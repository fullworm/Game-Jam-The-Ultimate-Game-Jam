import pygame
from constants import *

class Room:
    def __init__(self, up, down, left, right, walls, enemies, player):
        self.up: Room = up
        self.down: Room = down
        self.left: Room = left
        self.right: Room = right
        self.walls: list[list] = walls
        self.entities: list = enemies
        self.player = player

    def draw(self, surface):
        # doors will be drawn base on if the value passed to them are null or not. Ig this means rooms will be fixed size or we need to find the middle of each wall seperately
        pass
    def change_room(self):
        pass