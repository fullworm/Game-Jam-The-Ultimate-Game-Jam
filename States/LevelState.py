from States.State import state

class LevelState(state):
    def __init__(self, name, surface):
        super().__init__("LevelState", surface)
        self.level1
        self.level2
        self.level3
        self.level4
        self.level5