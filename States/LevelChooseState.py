from States.LevelState import *
from States.State import state
from pygame_widgets.button import ButtonArray
class LevelChooseState(state):
    def __init__(self, surface):
        super().__init__("LevelChooseState", surface)

        self.LevelArray = ButtonArray(
            self.surface,
            50,
            50, 
            500,
            500,
            (5, 1),
            border = 150, 
            texts=('Level 1 ', "Level 2 ", "Level 3 ", "Level 4 ", "Level 5 "),
            onClicks=(lambda: print('1'), lambda: print('2'), lambda: print('3'), lambda: print('4'), lambda: print('5'))
        )
    def update(self):
        pass
    def clean_up(self):
        self.LevelArray.hide()
