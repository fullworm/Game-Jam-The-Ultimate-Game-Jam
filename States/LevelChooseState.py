from States.LevelState import *
from States.State import state
from pygame_widgets.button import ButtonArray
from constants import *
class LevelChooseState(state):
    def __init__(self, surface):
        super().__init__("LevelChooseState", surface)

        self.LevelArray = ButtonArray(
            self.surface,
            (SCREENX - 500) // 2,
            (SCREENY - 500) // 2, 
            500,
            500,
            (5, 1),
            border = 20, 
            texts=('Level 1 ', "Level 2 ", "Level 3 ", "Level 4 ", "Level 5 "),
            onClicks=(lambda: print('1'), lambda: print('2'), lambda: print('3'), lambda: print('4'), lambda: print('5'))
        )
    def update(self):
        pass
    def clean_up(self):
        self.LevelArray.hide()
