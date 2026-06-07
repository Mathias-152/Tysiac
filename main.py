# Tysiac

import random
from Utilities import *
from Player import Player, HumanPlayer, ComputerPlayer
from Game import *
from Card import Card
#import pygame


def main():
    player1 = HumanPlayer("Player 1")
    game1 = Game(player1)
    game1.setup()

if __name__ == "__main__":
    main()