import pygame
from constants import *

class Room:
    def __init__(self, list, up, down, left, right, player):
        self.up: Room = up
        self.down: Room = down
        self.left: Room = left
        self.right: Room = right
        self.surface = pygame.Surface(GAMESIZE)
        self.entities: list = list
        self.player = player

    def draw():
        # doors will be drawn base on if the value passed to them are null or not. Ig this means rooms will be fixed size or we need to find the middle of each wall seperately
        pass
    def change_room():
        pass