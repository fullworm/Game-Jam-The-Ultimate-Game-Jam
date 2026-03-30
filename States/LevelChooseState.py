from States.LevelState import *
from States.State import state
from pygame_widgets.button import ButtonArray
from constants import *
class LevelChooseState(state):
    def __init__(self, surface):
        super().__init__("LevelChooseState", surface)

        self.LevelArray = ButtonArray(
            self.surface,
            (SCREENX - 700) // 2,  # X-coordinate
            (SCREENY + 50) // 2,  # Y-coordinate
            700,
            200,
            (4, 1),
            border = 20,
            texts=('Level 1', "Level 2", "Level 3","Return"),
            colour=(37, 47, 18),
            hoverColours=((106, 134, 53), (106, 134, 53), (106, 134, 53),(106, 134, 53),),
            inactiveColours=((153, 194, 77),(153, 194, 77),(153, 194, 77),(153, 194, 77),),
            fonts=(self.font, self.font, self.font, self.font),
            onClicks=(
                lambda: (self.set_next_state("Level 1"), self.buttonClick.play()),
                lambda: (self.set_next_state("Level 2"), self.buttonClick.play()),
                lambda: (self.set_next_state("Level 3"), self.buttonClick.play()),
                lambda: (self.set_next_state("MenuState"), self.buttonClick.play()),
            )
        )
    def update(self, events= None):
        pass
    def clean_up(self):
        self.LevelArray.hide()
        self.LevelArray.disable()
