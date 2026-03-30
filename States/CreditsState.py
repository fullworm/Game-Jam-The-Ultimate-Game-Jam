import pygame
from States.State import state
from pygame_widgets.button import Button
from constants import *
from sys import exit
class CreditsState(state):
    def __init__(self, surface):
        super().__init__("CreditsState", surface)
        # self.ButtonArray = ButtonArray(
        #         # Mandatory Parameters
        #     self.surface,  # Surface to place button array on
        #     (SCREENX//2 + GAMEX//2 - 100) // 2,  # X-coordinate
        #     (SCREENY//2 + GAMEY//2 -100) // 2,  # Y-coordinate
        #     100,  # Width
        #     100,  # Height
        #     (1, 1),
        #     border=0,  # Distance between buttons and edge of array
        #     texts=('Return'),  # Sets the texts of each button (counts left to right then top to bottom)
        #     onClicks=(lambda: (self.set_next_state("MenuState"), self.buttonClick.play())),
        #     colour=(37, 47, 18),
        #     hoverColours=((106, 134, 53),),
        #     inactiveColours=((153, 194, 77),),
        #     fonts=self.font,
        #
        # )
        # Creates the button with optional parameters
        self.button = Button(
            # Mandatory Parameters
            surface,  # Surface to place button on
            SCREENX//2-75,  # X-coordinate of top left corner
            SCREENY // 2 + GAMEY // 2 - 125,
            125,  # Width
            100,  # Height
            text='Return',  # Text to display
            inactiveColour=(153, 194, 77),  # Colour of button when not being interacted with
            hoverColour=(106, 134, 53),  # Colour of button when being hovered over
            onClick=lambda: (self.set_next_state("MenuState"), self.buttonClick.play()),  # Function to call when clicked on
            font=self.font
        )
        
    def update(self, events = None):
        pass
    def clean_up(self):
        self.button.hide()
        self.button.disable
        
