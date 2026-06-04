from Utilities import *

class Card:
    def __init__(self, figure, color):
        self.figure = figure
        self.color = color
        self.value = self.standard_value()
    
    def __str__(self):
        if self.color == "Kier" or self.color == "Karo":
            color_code = "\033[31m"
        else:
            color_code = "\033[90m"
        return f"{self.figure} {color_code}{symbols[self.color]}\033[0m"
    
    def __repr__(self):
        if self.color == "Kier" or self.color == "Karo":
            color_code = "\033[31m"
        else:
            color_code = "\033[90m"
        return f"{self.figure} {color_code}{symbols[self.color]}\033[0m"

    def __eq__(self, other):
        return self.figure == other.figure and self.color == other.color
    
    def standard_value(self):
        values = {
            "9": 0,
            "10": 10,
            "J": 2,
            "D": 3,
            "K": 4,
            "A": 11
        }
        return values[self.figure]
    