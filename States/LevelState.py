from States.State import state
import pygame, entities
from constants import *
from levels import *
from pygame_widgets.button import ButtonArray
from sys import exit

lvlBG = pygame.image.load("Images/lvlsBG.png")
lvl_BG = pygame.transform.scale(lvlBG, (GAMEX, GAMEY))

class LevelState(state):
    def __init__(self, surface, level, screen):
        super().__init__("LevelState", surface)

        self.player = entities.Player(int(TILESIZE * 5.5), int(TILESIZE * 5.5))
        self.room = None
        self.paused = False
        self.screen = screen
        self.level = level

        self.pauseMenu = ButtonArray(
            self.screen,
            (SCREENX - 500) // 2,
            (SCREENY - 500) // 2,
            500,
            500,
            (3,1), 
            border = 0,
            texts= ("Continue", "Select Level", "Exit game"),
            onClicks= (lambda: self.toggle_pause(), lambda: self.set_next_state("LevelChooseState"), lambda: exit())
        )
        self.pauseMenu._hidden = True
        if self.level == "Level 1":
            self.room = lvl1Start
            self.player.x, self.player.y = self.room.spawn
            self.curlevel = lvl1
        elif (self.level == "Level 2"):
            self.room = lvl2Start
            self.player.x, self.player.y = self.room.spawn
            self.curlevel = lvl2
        elif (self.level == "Level 3"):
            self.room = lvl3Start
            self.player.x, self.player.y = self.room.spawn
            self.curlevel = lvl3
        # elif (self.level == "Level 4"):
        #     self.room = lvl4
        # elif (self.level == "Level 5"):
        #     self.room = lvl5

    def player_input(self):
        if (not self.paused):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move(0, -PLAYERSPEED, self.room)
            if keys[pygame.K_s]:
                self.player.move(0, PLAYERSPEED, self.room)
            if keys[pygame.K_d]:
                self.player.move(PLAYERSPEED, 0, self.room)
            if keys[pygame.K_a]:
                self.player.move(-PLAYERSPEED, 0, self.room)

    def toggle_pause(self):
        self.paused = not self.paused
        if self.pauseMenu is not None:
            self.pauseMenu._hidden = not self.paused

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.toggle_pause()
            

    def update(self, events):
        newRoom = self.player.change_room(self.room, self.curlevel)
        if newRoom is not None:
            if self.room.entities is not None:
                for enemy in self.room.entities:
                    enemy.reset()
            self.room = newRoom

        self.surface.blit(lvl_BG, (0, 0))
        self.room.draw(self.surface)

        if self.room.entities is not None:
            for enemy in self.room.entities:
                enemy.draw(self.surface)
                if enemy.shoots and enemy.random_movement:
                    enemy.shoot(self.player)
                    enemy.move_bounce(self.player, self.room)
                    for p in enemy.projectiles:
                        p.update(self.player, self.room, self.surface)
                    enemy.projectiles = [p for p in enemy.projectiles if not p.delete]
                elif enemy.shoots:
                    enemy.shoot(self.player)
                    enemy.move_bounce(self.player, self.room)
                    for p in enemy.projectiles:
                        p.update(self.player, self.room, self.surface)
                    enemy.projectiles = [p for p in enemy.projectiles if not p.delete]
                elif enemy.random_movement:
                    enemy.move_bounce(self.player, self.room)
                else:
                    enemy.move_to_player(self.player)
                    if enemy.x >= 8.5 * TILESIZE:
                            enemy.move(-(ENEMYSPEED/2), 0, self.room)




        if self.room.collectable is not None:
            self.room.collectable.draw(self.surface, self.player)
        if self.room.terminal is not None:
            self.room.terminal.draw(self.surface, self.player, self.set_next_state)

        self.player.draw(self.surface, self.room)

        # a BUNCH of custom room instructions for enemies
        if self.room == lvl1Down:
            for enemy in self.room.entities:
                if enemy.x <= TILESIZE:
                    enemy.moving_right = True
                if enemy.x >= GAMEX - TILESIZE * 2:
                    enemy.moving_right = False

                if enemy.moving_right:
                    enemy.move(ENEMYSPEED, 0, self.room)
                else:
                    enemy.move(-ENEMYSPEED, 0, self.room)

        if self.room == lvl1Right:
            for enemy in self.room.entities:
                if enemy.moving_down == 120:
                    enemy.move(0, GAMEY*2, self.room)
                if enemy.moving_down == 0:
                    enemy.move(0, -GAMEY*2, self.room)

                if enemy.y < GAMEY:
                    enemy.moving_down += 1
                if enemy.y > GAMEY:
                    enemy.moving_down -= 2



        # if self.room == lvl1Left:
        #     for enemy in self.room.entities:
        #         enemy.move_to_player(self.player)
        #         if enemy.x >= 8.5 * TILESIZE:
        #             enemy.move(-ENEMYSPEED, 0, self.room)


    def clean_up(self):
        self.pauseMenu.hide()
        self.pauseMenu.disable

        self.player.MessageNumber = 0
        self.paused = False
        if self.level == "Level 1":
            level = lvl1
        elif (self.level == "Level 2"):
            level = lvl2
        elif (self.level == "Level 3"):
            level = lvl3
        # elif (self.level == "Level 4"):
        #     level = lvl4
        # elif (self.level == "Level 5"):
        #     level = lvl5

        for room in level.values():
            room.reset()
    
        if self.room and hasattr(self.room, 'collectable'):
            if self.room.collectable:
                self.room.collectable.active = True
        