from States.State import state
from pygame_widgets.button import ButtonArray
import sys
class MenuState(state):
    def __init__(self, surface):
        super().__init__("MenuState", surface)
        self.ButtonArray = ButtonArray(
                # Mandatory Parameters
            self.surface,  # Surface to place button array on
            50,  # X-coordinate
            50,  # Y-coordinate
            500,  # Width
            300,  # Height
            (3, 1),
            border=50,  # Distance between buttons and edge of array
            texts=('play', 'Creds', 'Exit'),  # Sets the texts of each button (counts left to right then top to bottom)

            onClicks=(lambda: self.set_next_state("LevelChooseState"), lambda: print('creds'), lambda: exit())\
        )
        
    def update(self):
        pass
    def exit():
        sys.exit
        return
    def clean_up(self):
        self.ButtonArray.hide()
        self.ButtonArray.disable()
        
