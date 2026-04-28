
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
    print("   0       1       2       3       4       5       6       7       8       9")

    
colors = ("Kier", "Pik", "Karo", "Trefl")
figures = ("A", "10", "K", "D", "J", "9")

