from pathlib import Path

path = Path.cwd().as_posix()
symbols = {
    "Kier": "♥",
    "Karo": "♦",
    "Trefl": "♣",
    "Pik": "♠"
}

color_value = {
    "Kier": 100,
    "Karo": 80,
    "Trefl": 60,
    "Pik": 40
}

color_order = {
    "Kier": 0,
    "Pik": 1,
    "Karo": 2,
    "Trefl": 3
}

figure_order = {
    "A": 0,
    "10": 1,
    "K": 2,
    "D": 3,
    "J": 4,
    "9": 5
}

def print_cards(cards):
    for card in cards:
        print("(", card, ")", end = " ")
    print()
    for i in range(len(cards)):
        print(f"   {i}    ", end="")
    print()

def print_cards_with_value(cards, player_name):
    print(player_name, end="")
    for card in cards:
        print("(", card, ")", end = " ")
    print(f"\n{player_name}", end="")
    for i in range(len(cards)):
        print(f"   {int(cards[i].value)}    ", end="")
    print()

    
colors = ("Kier", "Pik", "Karo", "Trefl")
figures = ("A", "10", "K", "D", "J", "9")

