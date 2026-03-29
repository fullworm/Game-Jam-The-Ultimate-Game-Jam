import pygame
from constants import *
import math
player_spritesheet = pygame.image.load("Images/playerSprites.png")
basic_enemy_spritesheet = pygame.image.load("Images/basicEnemySprites.png")
text_sheet = pygame.image.load("Images/text.png")

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = "left"

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

        # if room.entities is not None:
        #     if self.collides_with_enemy(room.entities):
        #         self.x, self.y = room.spawn

        if x < 0:
            self.dir = "left"
        elif x > 0:
            self.dir = "right"
        elif y < 0:
            self.dir = "up"
        elif y > 0:
            self.dir = "down"

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
        self.MessageNumber = 0

    def draw(self, surface, room):
        if room.entities is not None:
            if self.collides_with_enemy(room.entities):
                self.x, self.y = room.spawn

        if self.dir == "left":
            player_sprite = player_spritesheet.subsurface((0, 0, 12, 12))
        elif self.dir == "up":
            player_sprite = player_spritesheet.subsurface((12, 0, 12, 12))
        elif self.dir == "right":
            player_sprite = player_spritesheet.subsurface((24, 0, 12, 12))
        elif self.dir == "down":
            player_sprite = player_spritesheet.subsurface((36, 0, 12, 12))
        else:
            player_sprite = player_spritesheet.subsurface((0, 0, 12, 12))

        player_sprite = pygame.transform.scale(player_sprite, (PLAYERSIZE, PLAYERSIZE))
        surface.blit(player_sprite, (self.x, self.y))

class Projectile(Entity):
    def __init__(self, x, y, dir):
        super().__init__(x, y)
        self.direction = dir
        self.speed = 2
        self.float_x = float(self.x)
        self.float_y = float(self.y)
        self.rect = pygame.Rect(self.x, self.y, PROJECTILESIZE, PROJECTILESIZE)
        self.delete = False

    def draw(self, surface):
        pygame.draw.ellipse(surface, (255,0,0), self.rect, 0)

    def update(self, player, room, surface):
    
        self.float_x += self.direction.x * self.speed
        self.float_y += self.direction.y * self.speed
        
        self.x = int(self.float_x)
        self.y = int(self.float_y)
        self.rect.topleft = (self.x, self.y)

        self.draw(surface)
        
        if self.collides_with_wall(room.walls):
            self.delete = True

        player_rect = pygame.Rect(player.x, player.y, PLAYERSIZE, PLAYERSIZE)
        if self.rect.colliderect(player_rect):
            self.delete = True
            room.reset(player)

class Enemy(Entity):
    def __init__(self, x, y, xsize, ysize, moving_right, moving_down, speed = 0, shoots = False, moves = False):
        super().__init__(x, y)
        self.xsize = xsize
        self.ysize = ysize
        self.moving_right = moving_right
        self.moving_down = moving_down
        self.speed = speed
        self.startx = x
        self.starty = y
        self.shoots = shoots
        self.timer = 0
        self.projectiles = []
        self.move_to_p = moves

    def draw(self, surface):
        ticks = pygame.time.get_ticks() % (FPS * 20)
        if ticks <= 120:
            basic_enemy_sprite = basic_enemy_spritesheet.subsurface((16, 0, 8, 8))
        else:
            basic_enemy_sprite = basic_enemy_spritesheet.subsurface((8, 0, 8, 8))

        basic_enemy_sprite = pygame.transform.scale(basic_enemy_sprite, (PLAYERSIZE, PLAYERSIZE))
        surface.blit(basic_enemy_sprite, (self.x, self.y))

    def move(self, x, y, room):
        self.x += x
        self.y += y
    
    def move_to_player(self, player):

        enemy_vec = pygame.math.Vector2(self.x, self.y)
        player_vec = pygame.math.Vector2(player.x, player.y)

        to_player = player_vec - enemy_vec
        
        angle_to_player = math.degrees(-math.atan2(to_player.x, to_player.y))
        self.enemyOrientation = angle_to_player

        
        if to_player.length() > 0:
            move_vector = to_player.normalize() * self.speed
            self.x += move_vector.x
            self.y += move_vector.y
    
    def shoot(self, player):
        if self.timer > 0:
            self.timer -= 1
        else:
            enemy_vec = pygame.math.Vector2(self.x, self.y)
            player_vec = pygame.math.Vector2(player.x, player.y)
            to_player = player_vec - enemy_vec
            
            if to_player.length() > 0:
                to_player = to_player.normalize()

            new_proj = Projectile(self.x, self.y, to_player)
            self.projectiles.append(new_proj)
            self.timer = 120

    def reset(self):
        self.x = self.startx
        self.y = self.starty
            

class Message(Entity):
    def __init__(self, x, y, xsize, ysize, text, boy):
        super().__init__(x,y)
        self.xsize = xsize
        self.ysize = ysize
        self.active = True
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.text = text
        self.timer = 0
        self.boy = boy

    def draw(self, surface, player):
        player_rect = pygame.Rect(player.x, player.y, PLAYERSIZE, PLAYERSIZE)
         
        if self.active and self.rect.colliderect(player_rect):
            self.active = False
            player.MessageNumber += 1
            self.timer = 120

            
        if self.active:
            if self.boy:
                text_sprite = text_sheet.subsurface((0, 0, 12, 12))
            else:
                text_sprite = text_sheet.subsurface((12, 0, 12, 12))
            text_sprite = pygame.transform.scale(text_sprite, (PLAYERSIZE, PLAYERSIZE))
            surface.blit(text_sprite, (self.x, self.y))

        if self.timer > 0:
            self.render_text(surface)
            self.timer -= 1
    
    def render_text(self, surface):
        font = pygame.font.Font(None, 36)
    
        text_surface = font.render(self.text, True, (255, 255, 255))
        
        bg_rect = text_surface.get_rect(center=(GAMEX // 2, GAMEY - 50))
        pygame.draw.rect(surface, (0, 0, 0), bg_rect.inflate(20, 10))
    
        surface.blit(text_surface, bg_rect)

class Terminal(Entity):
    def __init__(self, x, y, xsize, ysize):
        super().__init__(x, y)
        self.xsize = xsize
        self.ysize = ysize
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.timer = 0
        self.done = False

    def draw(self, surface, player, next_state_func):
        player_rect = pygame.Rect(player.x, player.y, PLAYERSIZE, PLAYERSIZE)

        pygame.draw.rect(surface, (255,0,0), self.rect)
        if self.done and self.timer > 0:
            self.render_text(surface, "Relationship progressed!")
            self.timer -= 1
        elif self.done and self.timer == 0:
            next_state_func("LevelChooseState")
        else:
            if self.rect.colliderect(player_rect):
                if player.MessageNumber < 3:
                    self.render_text(surface, f"{3-player.MessageNumber} Messages left to collect")
                elif player.MessageNumber == 3:
                    self.done = True
                    self.timer = 120
                    self.render_text(surface, "Relationship progressed!")


    def render_text(self, surface, text):
        font = pygame.font.Font(None, 36)
    
        text_surface = font.render(text, True, (255, 255, 255))
        
        bg_rect = text_surface.get_rect(center=(GAMEX // 2, GAMEY - 50))
        pygame.draw.rect(surface, (0, 0, 0), bg_rect.inflate(20, 10))
    
        surface.blit(text_surface, bg_rect)

