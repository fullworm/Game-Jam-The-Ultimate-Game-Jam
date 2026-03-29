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
            (SCREENY+200) // 2,  # Y-coordinate
            700,  # Width
            200,  # Height
            (3, 1),
            border=30,  # Distance between buttons and edge of array
            texts=('play', 'Creds', 'Exit'),  # Sets the texts of each button (counts left to right then top to bottom)
            onClicks=(lambda: self.set_next_state("LevelChooseState"), lambda: print('creds'), lambda: exit()),
            colour=(0, 0, 0),
            hoverColours=((0, 255, 255), (0, 255, 255), (0, 255, 255)),
            inactiveColours=((50, 150, 150),(50, 150, 150),(50, 150, 150))
        )
        
    def update(self, events = None):
        pass
    def clean_up(self):
        self.ButtonArray.hide()
        self.ButtonArray.disable
        
