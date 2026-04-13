# Tysiac

import random

symbols = {
    "Kier": "♥",
    "Karo": "♦",
    "Trefl": "♣",
    "Pik": "♠"
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

class Card:
    def __init__(self, figure, color):
        self.figure = figure
        self.color = color
    
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

    def value(self):
        values = {
            "9": 0,
            "10": 10,
            "J": 2,
            "D": 3,
            "K": 4,
            "A": 11
        }
        return values[self.figure]
    
colors = ("Kier", "Pik", "Karo", "Trefl")
figures = ("A", "10", "K", "D", "J", "9")
cards = [Card(figure, color) for figure in figures for color in colors]

def print_cards(cards):
    for card in cards:
        print("(", card, ")", end = " ")
    print() 
    print("   0       1       2       3       4       5       6       7       8       9")
    print() 
       

class Player:
    def __init__(self, name, id):
        self.name = name
        self.cards = []
        self.score = 0
        self.id = id

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name, 0)

    def make_a_move(self):
        pass

class ComputerPlayer(Player):
    def __init__(self, name, id):
        super().__init__(name, id)
    

def evaluate_cards(self, player_deck):
        value = 0
        rest_of_deck = [x for x in cards if x not in player_deck]
        rest_of_deck.sort(key = lambda card: card.value(), reverse = True)
        for card in player_deck:
            value += card.value()
        if cards[8] in player_deck and cards[12] in player_deck:
            value += 100
            print("Sto!")
        if cards[9] in player_deck and cards[13] in player_deck:
            value += 40
            print("Czterdzieści!")
        if cards[10] in player_deck and cards[14] in player_deck:
            value += 80
            print("Osiemdziesiąt!")
        if cards[11] in player_deck and cards[15] in player_deck:
            value += 60
            print("Sześćdziesiąt!")
        
        
        return value

def is_valid_move(player_deck, card_to_play, on_table, atut):
    if not on_table:
        return True
    winning_card = on_table[0]
    for card in on_table:
                if card.color == winning_card.color and card.value() > winning_card.value():
                    winning_card = card
                elif card.color == atut and winning_card.color != atut:
                    winning_card = card
                elif atut != "" and card.color == atut and winning_card.color == atut and card.value() > winning_card.value():
                    winning_card = card
    leading_color = on_table[0].color
    has_color = any(card.color == leading_color for card in player_deck)
    has_atut = any(card.color == atut for card in player_deck)
    if has_color:
        if card_to_play.color != leading_color:
            print("You must follow the color of the first card on the table!")
            return False    
        else:
            if card_to_play.value() < winning_card.value() and card_to_play.color == winning_card.color and any(card.value() > winning_card.value() for card in player_deck if card.color == leading_color):
                print("You must play a higher card of the leading color if you have one!")
                return False
        return True
    if has_atut:
        if card_to_play.color != atut: 
            if winning_card.color == atut and not any(card.value() > winning_card.value() for card in player_deck if card.color == atut):
                return True
            print("You must play the atut!")
            return False
        return True
    return True

def is_atut(card, player_deck, atut):
                if card==cards[13] and cards[9] in player_deck:
                    print("Czterdzieści!")
                    return cards[13].color
                elif card==cards[14] and cards[10] in player_deck:
                    print("Osiemdziesiąt!")
                    return cards[14].color
                elif card==cards[15] and cards[11] in player_deck:
                    print("Sześćdziesiąt!")
                    return cards[15].color
                elif card==cards[12] and cards[8] in player_deck:
                    print("Sto!")
                    return cards[12].color
                else:
                    return atut

class game:
    
    def __init__(self, player1):
        self.round_nr = 1
        self.players = [player1, Player("Player 2", 1), Player("Player 3", 2)]
        self.player_scores = [0, 0, 0]
        self.table_cards = []

    def deal_cards(self):
        deck = cards.copy()
        random.shuffle(deck)
        self.players[0].cards = []
        self.players[1].cards = []
        self.players[2].cards = []
        i = 0 
        for j in range(7):
            temp = deck.pop(0)
            self.players[0].cards.append(temp)
        for j in range(7):
            temp = deck.pop(0)
            self.players[1].cards.append(temp)
        for j in range(7):
            temp = deck.pop(0)
            self.players[2].cards.append(temp)
        self.players[0].cards.sort(key=lambda card: (color_order[card.color], figure_order[card.figure]))
        self.players[1].cards.sort(key = lambda card: (color_order[card.color], figure_order[card.figure]))
        self.players[2].cards.sort(key = lambda card: (color_order[card.color], figure_order[card.figure]))
        deck.sort(key = lambda card: (color_order[card.color], figure_order[card.figure]))
        return deck


    def bidding_phase(self):
        highest_bid = 100
        highest_bidder = self.players[self.round_nr%3]
        bidder = (self.round_nr+1)%3
        passed_players = []
        while len(passed_players) < 3:
            if bidder in passed_players:
                bidder = (bidder+1)%3
                continue
            if bidder == 0:
                print("Your cards: ")
                print_cards(self.players[0].cards)
                bet = input("Current bet: " + str(highest_bid) + " by: " + highest_bidder.name + "\n, enter your bet increase (or '0' to pass): ")
                if bet == "0":
                    passed_players.append(bidder)
                elif int(bet) <= 0 or int(bet)+highest_bid > 300 or int(bet)%5 != 0:
                    print("Invalid bet, try again")
                    continue
                else:
                    highest_bid += int(bet)
                    highest_bidder = self.players[bidder]
            else:
                print("Player " + str(bidder+1) + "'s bidding turn")
                #print("Evaluation of your hand: " + str(evaluate_cards(self.players[bidder].cards)))
                print_cards(self.players[bidder].cards)
                bet = input("Current bet: " + str(highest_bid) + " by: " + highest_bidder.name + "\n, enter your bet increase (or '0' to pass): ")
                if bet == "0":
                    passed_players.append(bidder)
                elif int(bet) <= 0 or int(bet)+highest_bid > 300 or int(bet)%5 != 0:
                    print("Invalid bet, try again")
                    continue
                else:
                    highest_bid += int(bet)
                    highest_bidder = self.players[bidder]
            bidder = (bidder+1)%3
        
        print("Highest bidder: " + highest_bidder.name + " with a bet of " + str(highest_bid))
        while len(self.table_cards) > 0:
            temp = self.table_cards.pop(0)
            highest_bidder.cards.append(temp)
        highest_bidder.cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        if highest_bidder.id == 0:
            print_cards(highest_bidder.cards)
            l = input("Which cards do you want to discard to left player?")
            card_left = highest_bidder.cards.pop(int(l))
            self.players[(highest_bidder.id+1)%3].cards.append(card_left)
            print_cards(highest_bidder.cards)
            r = input("Which cards do you want to discard to right player?")
            card_right = highest_bidder.cards.pop(int(r))
            self.players[(highest_bidder.id+2)%3].cards.append(card_right)
        else:
            print_cards(highest_bidder.cards)
            l = input("Which cards do you want to discard to left player?")
            card_left = highest_bidder.cards.pop(int(l))
            self.players[(highest_bidder.id+1)%3].cards.append(card_left)
            print_cards(highest_bidder.cards)
            r = input("Which cards do you want to discard to right player?")
            card_right = highest_bidder.cards.pop(int(r))
            self.players[(highest_bidder.id+2)%3].cards.append(card_right)
        self.players[(highest_bidder.id+1)%3].cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        self.players[(highest_bidder.id+2)%3].cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        return highest_bidder.id, highest_bid


    def playing_phase(self, first_player_id):
        sum_from_cards = [0, 0, 0]
        atut = ""
        while len(self.players[0].cards) > 0:
            print("*"*20)
            on_table = []
            for i in range(first_player_id, (first_player_id+3)):
                player_id = i%3
                if player_id == 0:#User player
                    print("Your turn")
                    print_cards(self.players[0].cards)
                    while True:                   
                        x = input(self.players[player_id].name + ", which card do you want to play? ")
                        chosen_card = self.players[player_id].cards[int(x)]
                        if is_valid_move(self.players[player_id].cards, chosen_card, on_table, atut):
                            if on_table == []:
                                atut = is_atut(chosen_card, self.players[player_id].cards, atut)
                            on_table.append(self.players[player_id].cards.pop(int(x)))
                            break
                else:#Computer player
                    print("Player " + str(player_id+1) + "'s turn")
                    print_cards(self.players[player_id].cards)
                    while True:                   
                        x = input(self.players[player_id].name + ", which card do you want to play? ")
                        chosen_card = self.players[player_id].cards[int(x)]
                        if is_valid_move(self.players[player_id].cards, chosen_card, on_table, atut):
                            if on_table == []:
                                atut = is_atut(chosen_card, self.players[player_id].cards, atut)
                            on_table.append(self.players[player_id].cards.pop(int(x)))
                            break
                print("Cards on the table: ")
                print_cards(on_table)
            winning_card = on_table[0]
            for card in on_table:
                if card.color == winning_card.color and card.value() > winning_card.value():
                    print("New winning card: " + str(card) + " Higher in color")
                    winning_card = card
                elif card.color == atut and winning_card.color != atut:
                    print("New winning card: " + str(card) + " Atut beats non-atut")
                    winning_card = card
                elif atut is not None and card.color == atut and winning_card.color == atut and card.value() > winning_card.value():
                    print("New winning card: " + str(card) + " Higher atut")
                    winning_card = card
            winning_player_id = (first_player_id + on_table.index(winning_card))%3
            sum_from_cards[winning_player_id] += sum(card.value() for card in on_table)
            first_player_id = winning_player_id ###
        return sum_from_cards
    
    def is_finnished(self):
        return any(score >= 1000 for score in self.player_scores)

    def round(self):
        print("************************************* Round " + str(self.round_nr) + " *************************************")
        self.table_cards = self.deal_cards()
        highest_bidder_id, highest_bid = self.bidding_phase()
        first_player_id = highest_bidder_id
        sum_from_cards = self.playing_phase(first_player_id)
        for i in range(3):
            if i == highest_bidder_id:
                if sum_from_cards[i] < highest_bid:
                    self.player_scores[i] -= highest_bid
                else:
                    self.player_scores[i] += highest_bid
            else:
                self.player_scores[i] += round(sum_from_cards[i]/5)*5
        print("Scores: ")
        for i in range(3):
            print(self.players[i].name + ": " + str(self.player_scores[i]))
        if self.is_finnished():
            print("Game over!")
        else:
            self.round_nr += 1
            self.round()

    


def main():
    player1 = Player("Mathias", 0)
    game1 = game(player1)
    game1.round()

if __name__ == "__main__":
    main()
