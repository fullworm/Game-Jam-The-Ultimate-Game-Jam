import pygame
class state:
    def __init__(self, name, surface):
        self.name: str = name
        self.next: str = ""
        self.surface = surface
        self.font = pygame.font.Font("fonts/Jersey10-Regular.ttf", 40)
        pygame.mixer.init()
        self.buttonClick = pygame.mixer.Sound('Sounds/buttonClick.ogg')

    def set_next_state(self, state: str) -> None:
        self.next = state
        return
    
    def draw() -> None:
        pass

    def get_next(self):
        return self.next