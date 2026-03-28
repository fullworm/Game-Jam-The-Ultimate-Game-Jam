import State
from pygame import pygame_widgets
import sys
class MenuState(State):
    def __init__(self, name, surface):
        super.__init__(name, surface)

        self.ButtonArray = pygame_widgets.ButtonArray(
            surface, 
            50,
            50,
            500,
            500,
            (2,2),
            border = 100,
            texts = ('Play', 'Creds', 'Exit'),
            onClicks = (lambda: self.set_next_state("LevelChooseState"), lambda: self.set_next_state("Creds"), lambda: self.exit())
        )

    def exit():
        sys.exit
        return