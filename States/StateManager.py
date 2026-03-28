from States.State import state
from constants import *
from States.MenuState import MenuState
from States.LevelChooseState import LevelChooseState
import pygame_widgets
from States.LevelState import LevelState
class StateManager(state):
    def __init__(self, surface):
        super().__init__("StateManager", surface)
        self.state = MenuState(surface)
        self.playing = False


    def update(self, event):

        if (self.state.get_next != ""):
            next = self.state.get_next()
            if (next == "LevelChooseState"):
                self.state.clean_up()
                self.state = LevelChooseState(self.surface)
            elif (next == "Level 1"):
                self.state.clean_up()
                self.state = LevelState(self.surface, "Level 1")
                self.playing = True

        if (self.playing):
            self.state.player_input()
            
        self.state.update()
        pygame_widgets.update(event)