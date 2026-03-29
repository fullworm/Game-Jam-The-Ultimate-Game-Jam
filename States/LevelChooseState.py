from States.LevelState import *
from States.State import state
from pygame_widgets.button import ButtonArray
from constants import *
class LevelChooseState(state):
    def __init__(self, surface):
        super().__init__("LevelChooseState", surface)

        self.LevelArray = ButtonArray(
            self.surface,
            (SCREENX - 600) // 2,
            (SCREENY - 300) // 2,
            600,
            300,
            (5, 1),
            border = 20,
            texts=('Level 1 ', "Level 2 ", "Level 3 ", "Level 4 ", "Level 5 "),
            hoverColours=((0, 255, 255),(0, 255, 255),(0, 255, 255),(0, 255, 255),(0, 255, 255),),
            inactiveColours=((50, 150, 150),(50, 150, 150),(50, 150, 150),(50, 150, 150),(50, 150, 150),),
            onClicks=(
                lambda: self.set_next_state("Level 1"), 
                lambda: self.set_next_state("Level 2"), 
                lambda: self.set_next_state("Level 3"), 
                lambda: self.set_next_state("Level 4"), 
                lambda: self.set_next_state("Level 5")
            )
        )
    def update(self, events= None):
        pass
    def clean_up(self):
        self.LevelArray.hide()
        self.LevelArray.disable()
