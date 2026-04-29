import random
from Player import Player, HumanPlayer, ComputerPlayer
from Utilities import *
from Card import Card


### Do usuniecia
def is_valid_move(player_deck, card_to_play, on_table, atut):
    if not on_table:
        return True
    winning_card = on_table[0]
    for card in on_table:
                if card.color == winning_card.color and card.standard_value() > winning_card.standard_value():
                    winning_card = card
                elif card.color == atut and winning_card.color != atut:
                    winning_card = card
                elif atut != "" and card.color == atut and winning_card.color == atut and card.standard_value() > winning_card.standard_value():
                    winning_card = card
    leading_color = on_table[0].color
    has_color = any(card.color == leading_color for card in player_deck)
    has_atut = any(card.color == atut for card in player_deck)
    if has_color:
        if card_to_play.color != leading_color:
            print("You must follow the color of the first card on the table!")
            return False    
        else:
            if card_to_play.standard_value() < winning_card.standard_value() and card_to_play.color == winning_card.color and any(card.standard_value() > winning_card.standard_value() for card in player_deck if card.color == leading_color):
                print("You must play a higher card of the leading color if you have one!")
                return False
        return True
    if has_atut:
        if card_to_play.color != atut: 
            if winning_card.color == atut and not any(card.standard_value() > winning_card.standard_value() for card in player_deck if card.color == atut):
                return True
            print("You must play the atut!")
            return False
        return True
    return True





class Game:
    
    def __init__(self, player1):
        self.round_nr = 1
        self.players = [player1, ComputerPlayer("Player 2", 1), ComputerPlayer("Player 3", 2)]
        self.player_scores = [0, 0, 0]
        self.table_cards = []
        self.rest_of_cards = []

    def deal_cards(self):
        deck = [Card(figure, color) for figure in figures for color in colors]
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
        full_deck = [Card(figure, color) for figure in figures for color in colors]
        self.rest_of_cards = full_deck
        deck.sort(key = lambda card: (color_order[card.color], figure_order[card.figure]))
        return deck


    def bidding_phase(self):
        highest_bid = 100
        highest_bidder = self.players[self.round_nr%3]
        bidder = self.players[(self.round_nr+1)%3]
        passed_players = []
        while len(passed_players) < 3:
            if bidder in passed_players:
                bidder = self.players[(bidder.id+1)%3]
                continue
            bet = bidder.make_a_bid(highest_bid, highest_bidder, 0, self.rest_of_cards)
            if int(bet) == 0:
                passed_players.append(bidder)
            elif int(bet) <= 0 or int(bet)+highest_bid > 300 or int(bet)%5 != 0:
                print("Invalid bet, try again")
                continue
            else:
                highest_bid += int(bet)
                highest_bidder = self.players[bidder.id]
            bidder = self.players[(bidder.id+1)%3]
        print("Highest bidder: " + highest_bidder.name + " with a bet of " + str(highest_bid))
        while len(self.table_cards) > 0:
            temp = self.table_cards.pop(0)
            highest_bidder.cards.append(temp)
        highest_bidder.cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        cards_to_give = highest_bidder.gave_away(self.rest_of_cards)
        self.players[(highest_bidder.id+1)%3].cards.append(cards_to_give[0])
        self.players[(highest_bidder.id+2)%3].cards.append(cards_to_give[1])
        self.players[(highest_bidder.id+1)%3].cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        self.players[(highest_bidder.id+2)%3].cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        print_cards(self.players[0].cards)
        print_cards(self.players[1].cards)
        print_cards(self.players[2].cards)
        
        return highest_bidder.id, highest_bid


    def playing_phase(self, first_player_id):
        def is_atut(card, player_deck, atut):
                if card.figure == "D" and card.color == "Pik" and any(c.figure == "K" and c.color == "Pik" for c in player_deck):
                    print("Czterdzieści!")
                    return card.color
                elif card.figure == "D" and card.color == "Karo" and any(c.figure == "K" and c.color == "Karo" for c in player_deck):
                    print("Osiemdziesiąt!")
                    return card.color
                elif card.figure == "D" and card.color == "Trefl" and any(c.figure == "K" and c.color == "Trefl" for c in player_deck):
                    print("Sześćdziesiąt!")
                    return card.color
                elif card.figure == "D" and card.color == "Kier" and any(c.figure == "K" and c.color == "Kier" for c in player_deck):
                    print("Sto!")
                    return card.colora
                else:
                    return atut
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
        self.players[1].give_points_to_cards(self.rest_of_cards)
        highest_bidder_id, highest_bid = self.bidding_phase()
        
        # first_player_id = highest_bidder_id
        # sum_from_cards = self.playing_phase(first_player_id)
        # for i in range(3):
        #     if i == highest_bidder_id:
        #         if sum_from_cards[i] < highest_bid:
        #             self.player_scores[i] -= highest_bid
        #         else:
        #             self.player_scores[i] += highest_bid
        #     else:
        #         self.player_scores[i] += round(sum_from_cards[i]/5)*5
        # print("Scores: ")
        # for i in range(3):
        #     print(self.players[i].name + ": " + str(self.player_scores[i]))
        # if self.is_finnished():
        #     print("Game over!")
        # else:
        #     self.round_nr += 1
        #     self.round()