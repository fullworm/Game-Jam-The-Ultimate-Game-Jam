from States.State import state
from constants import *
from States.MenuState import MenuState
from States.LevelChooseState import LevelChooseState
import pygame_widgets
from States.LevelState import LevelState
class StateManager(state):
    def __init__(self, screen, surface):
        super().__init__("StateManager", screen)
        self.state = MenuState(screen)
        self.playing = False
        self.playSurface = surface


    def update(self, event):

        if (self.state.get_next != ""):
            next = self.state.get_next()
            if (next == "LevelChooseState"):
                self.state.clean_up()
                self.playSurface.fill((210, 210, 180))
                self.state = LevelChooseState(self.surface)
                self.playing = False
            elif (next == "Level 1"):
                self.state.clean_up()
                self.state = LevelState(self.playSurface, "Level 1", self.surface)
                self.playing = True
            elif (next == "Level 2"):
                self.state.clean_up()
                self.state = LevelState(self.playSurface, "Level 2", self.surface)
                self.playing = True
            elif (next == "Level 3"):
                self.state.clean_up()
                self.state = LevelState(self.playSurface, "Level 3", self.surface)
                self.playing = True
            

        if hasattr(self.state, 'player_input'):
            self.state.player_input()

        if hasattr(self.state, 'handle_event'):
            self.state.handle_event(event)
            
        self.state.update(event)
        pygame_widgets.update(event)