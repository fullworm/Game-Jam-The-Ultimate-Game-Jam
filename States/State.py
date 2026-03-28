class state:
    def __init__(self, name, surface):
        self.name: str = name
        self.next: str = ""
        self.surface = surface

    def set_next_state(self, state: str) -> None:
        self.next = state
        return
    
    def draw() -> None:
        pass

    def get_next(self):
        return self.next