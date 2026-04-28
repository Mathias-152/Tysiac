# Tysiac

import random
from Utilities import *
from Player import Player, HumanPlayer, ComputerPlayer
from Game import *
from Card import Card


def main():
    player1 = HumanPlayer("Mathias")
    game1 = Game(player1)
    game1.round()

if __name__ == "__main__":
    main()