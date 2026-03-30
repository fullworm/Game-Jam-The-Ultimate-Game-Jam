import pygame
from States.State import state
from pygame_widgets.button import ButtonArray
from constants import *
from sys import exit
class MenuState(state):
    def __init__(self, surface):
        super().__init__("MenuState", surface)
        self.ButtonArray = ButtonArray(
                # Mandatory Parameters
            self.surface,  # Surface to place button array on
            (SCREENX - 700) // 2,  # X-coordinate
            (SCREENY+50) // 2,  # Y-coordinate
            700,  # Width
            200,  # Height
            (3, 1),
            border=20,  # Distance between buttons and edge of array
            texts=('Play', 'Credits', 'Exit Game'),  # Sets the texts of each button (counts left to right then top to bottom)
            onClicks=(lambda: (self.set_next_state("LevelChooseState"), self.buttonClick.play()),
                      lambda: (self.set_next_state("CreditsState"), self.buttonClick.play()),
                      lambda: (self.buttonClick.play(), exit())),
            colour=(37, 47, 18),
            hoverColours=((106, 134, 53), (106, 134, 53), (106, 134, 53),),
            inactiveColours=((153, 194, 77),(153, 194, 77),(153, 194, 77),),
            fonts=(self.font, self.font, self.font),

        )
        
    def update(self, events = None):
        pass
    def clean_up(self):
        self.ButtonArray.hide()
        self.ButtonArray.disable
        
