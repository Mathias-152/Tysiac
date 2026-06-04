import pygame
from Utilities import *
from Card import Card
class Button:
    def __init__(self, image, x, y, tx, ty):
        self.surface = pygame.image.load(f"{path}/Images/{image}.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (tx, ty))
        self.rect = self.surface.get_rect(center = (x,y))
    
    def is_clicked(self, mouse):
        return self.rect.collidepoint(mouse)
    
    def reposition(self, x, y):
        self.rect = self.surface.get_rect(center = (x,y))

class Card_Button(Button):
    def __init__(self, card, x, y, tx=100, ty=150):
        super().__init__(str(card.figure + card.color), x, y, tx, ty)
        #self.rect = self.surface.get_rect(topleft = (x,y))

class Bet_Button(Button):
    def __init__(self, image, x, y, tx, ty, value):
        super().__init__(image, x, y, tx ,ty)
        self.value = value


    