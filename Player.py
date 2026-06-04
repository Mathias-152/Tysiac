from Utilities import *
from Button import *
from Card import Card
import pygame
class Player:
    def __init__(self, name, id):
        self.name = name
        self.cards = []
        self.score = 0
        self.id = id
        self.rest_of_cards = []

    def __str__(self):
        return f"{self.name} ({self.score} points)"
    
    def __repr__(self):
        return f"{self.name} ({self.score} points)"
    
    # Returns the highest card on the table, considering the atut    
    def highest_on_table(self, on_table, atut):
        winning_card = on_table[0]
        for card in on_table:
                    if card.color == winning_card.color and card.standard_value() > winning_card.standard_value():
                        winning_card = card
                    elif card.color == atut and winning_card.color != atut:
                        winning_card = card
                    elif atut != "" and card.color == atut and winning_card.color == atut and card.standard_value() > winning_card.standard_value():
                        winning_card = card
        return winning_card
    
    # Checks if the player has any card that can beat the current winning card on the table, considering the atut
    def if_any_higher_card(self, on_table, atut):
        leading_color = on_table[0].color
        winning_card = self.highest_on_table(on_table, atut)
        has_color = any(card.color == leading_color for card in self.cards)
        has_atut = any(card.color == atut for card in self.cards)
        if has_color:
            if any(card.color == leading_color and card.standard_value() > winning_card.standard_value()for card in self.cards):
                return True
        elif has_atut:
            if any(card.color == leading_color and card.standard_value() > winning_card.standard_value()for card in self.cards):
                return True
        return False
    
    # Checks if the card the player wants to play is a valid move, considering the rules of the game and the cards on the table                    
    def is_valid_move(self, card_to_play, on_table, atut):
        if not on_table:
            return True
        winning_card = self.highest_on_table(on_table, atut)
        leading_color = on_table[0].color
        has_color = any(card.color == leading_color for card in self.cards)
        has_atut = any(card.color == atut for card in self.cards)
        if has_color:
            if card_to_play.color != leading_color:
                if self.id == 0:
                    print("You must follow the color of the first card on the table!")
                return False    
            else:
                if card_to_play.standard_value() < winning_card.standard_value() and card_to_play.color == winning_card.color and any(card.standard_value() > winning_card.standard_value() for card in self.cards if card.color == leading_color):
                    if self.id == 0:
                        print("You must play a higher card of the leading color if you have one!")
                    return False
            return True
        if has_atut:
            if card_to_play.color != atut: 
                if winning_card.color == atut and not any(card.standard_value() > winning_card.standard_value() for card in self.cards if card.color == atut):
                    return True
                if self.id == 0:
                    print("You must play the atut!")
                return False
            return True
        return True

    
class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name, 0)

    # Asks the user for their bid, considering the current highest bid and the rules of the game
    def make_a_bid(self, highest_bid, highest_bidder, second_bidding, NP_rest_of_cards):
        print("Your cards: ")
        print_cards(self.cards)
        if second_bidding == 0:
            bet = input("Current bet: " + str(highest_bid) + " by: " + highest_bidder.name + ", enter your bet increase (or '0' to pass): ")
        else:
            bet = input("You've won the bid, do you want to increase your bet? Current bet: " + str(highest_bid) + ", enter your bet increase (or '0' to pass): ")
        return bet
    
    # Asks the user which cards they want to give away to the other players, considering the rules of the game
    def gave_away(self, NP_rest_of_cards):
        cards_to_give =[]
        print_cards(self.cards)
        l = input("Which cards do you want to discard to left player? ")
        cards_to_give.append(self.cards.pop(int(l)))
        print_cards(self.cards)
        r = input("Which cards do you want to discard to right player? ")
        cards_to_give.append(self.cards.pop(int(r)))
        return cards_to_give
    
    # Asks the user which card they want to play
    def make_a_move(self, NP_rest_of_cards, on_table, atu):
        print("Cards on table:", end = '\n')
        print_cards(on_table)
        print("Your turn")
        print_cards(self.cards)
        while True:                   
            x = input(self.name + ", which card do you want to play? ")
            chosen_card = self.cards[int(x)]
            if self.is_valid_move(chosen_card, on_table, atu):
                self.cards.remove(chosen_card)
                return chosen_card
    

class ComputerPlayer(Player):
    def __init__(self, name, id):
        super().__init__(name, id)

    # Returns a list of cards that are going to win the trick if played
    def worthfull_cards(self, NP_rest_of_cards):
        rest_of_cards = [card for card in NP_rest_of_cards if card not in self.cards]
        top_cards = [[] for _ in range(len(colors))]
        winning_cards = [[] for _ in range(len(colors))]
        card_in_color = [[] for _ in range(len(colors))]
        i = 0
        for color in colors:            
            if any(c.figure == "D" and c.color == color for c in self.cards) and any(c.figure == "K" and c.color == color for c in self.cards):# If atu in color
                higher_tan_K = 0
                for figure in figures:
                    found = next((c for c in self.cards if c.color == color and c.figure == figure), None)
                    if found:
                        card_in_color[i].append(found)
                        if found.standard_value() > 4:
                            higher_tan_K += 1  
                    else:
                        continue
                for j in range(0, len(card_in_color[i]) - 2 + higher_tan_K):
                    winning_cards[i].append(card_in_color[i][j])
            else: #if no atu in color
                for figure in figures:                        
                    found = next((c for c in self.cards if c.color == color and c.figure == figure), None)
                    if found:
                        winning_cards[i].append(found)
                        top_cards[i].append(found)
                    elif not any(c.figure == figure and c.color == color for c in rest_of_cards):
                        continue
                    else:
                        break
                for figure in figures:
                    found = next((c for c in self.cards if c.color == color and c.figure == figure), None)
                    if found:
                        card_in_color[i].append(found)
                    else:
                        continue
                if any(card.figure == "10" for card in card_in_color[i]) and any(card.figure != "10" and card.figure != "A" for card in card_in_color[i])and not any(card.figure == "A" for card in card_in_color[i]):
                    winning_cards[i].append(next(card for card in card_in_color[i] if card.figure == "10"))
            if 6-len(card_in_color[i])-1 <= len(top_cards[i]): #If you take whole color
                for card in card_in_color[i]:
                    if card not in winning_cards[i]:
                        winning_cards[i].append(card)
            i += 1
        return winning_cards
    # Evaluates the player's cards and returns a score based on their potential to win tricks, considering the cards that are still in play

    def evaluate_cards(self, NP_rest_of_cards):        
        winning_cards = self.worthfull_cards(NP_rest_of_cards)
        points = 0
        for color in colors:            
            if any(c.figure == "D" and c.color == color for c in self.cards) and any(c.figure == "K" and c.color == color for c in self.cards):
                points += color_value[color]
        for i in range(4):
            for card in winning_cards[i]:
                points += card.standard_value()
        rest_of_cards = [card for card in NP_rest_of_cards if card not in self.cards]
        rest_of_cards.sort(key=lambda c: c.standard_value())
        for card in rest_of_cards:
            if card in self.cards:
                rest_of_cards.remove(card)
        #print("Rest of cards: ", rest_of_cards, end="")### usuń
        for color in colors:
            for card in winning_cards[colors.index(color)]:
                for i in range(2):
                    if any(c.color == color and c.standard_value() < card.standard_value() for c in rest_of_cards):
                        found = next((c for c in rest_of_cards if c.color == color), None)
                        if found:
                            points += found.standard_value()
                            rest_of_cards.remove(found)
                    else:
                        points+=rest_of_cards[0].standard_value()
                        rest_of_cards.pop(0)
        return points
    
    # Determines the computer player's bid based on the cards value
    def make_a_bid(self, highest_bid, highest_bidder, second_bidding, NP_rest_of_cards):
        if highest_bidder.id == self.id and second_bidding == 0:
            return 0
        score = self.evaluate_cards(NP_rest_of_cards)
        bet = round((score)//5)*5
        if bet > highest_bid:
            if second_bidding:
                return bet - highest_bid
            else:
                return 5
        else:
            return 0
        
    # Determinates card value based on played cards, cards in hand and cards that are still in play
    def give_points_to_cards(self, NP_rest_of_cards):
        rest_of_cards = [card for card in NP_rest_of_cards if card not in self.cards]
        for color in colors: 
            card_in_color = []
            for card in self.cards:
                if color == card.color:
                    card_in_color.append(card)
            # +20 if there is pair
            if any(c.figure == "D" for c in card_in_color) and any(c.figure == "K" for c in card_in_color):
                for card in self.cards:
                    if color == card.color:
                        card.value+=20
                        if card.figure=="D":
                            card.value+=20
                            card.value+=color_value[color]/10
                    
            # +2*(n-1) points for n cards in color
            for card in self.cards:
                if color == card.color:
                    card.value+=2*(len(card_in_color)-1)
            # +8 if there is "10" and only one other card in color
            if len(card_in_color)==2 and any(c.figure == "10" for c in card_in_color):
                for c in card_in_color:
                    c.value+=8
            # +5 if card is highest in color
            for card in card_in_color:
                if not any(c.standard_value()>card.standard_value() for c in rest_of_cards):
                    card.value+=5
        return 
    
    # Determines which cards the computer player will give away to the other players
    def gave_away(self, NP_rest_of_cards):
        cards_to_gave_away = []
        self.give_points_to_cards(NP_rest_of_cards)
        self.cards.sort(key = lambda c:c.value)
        cards_to_gave_away.append(self.cards[0])
        self.cards.pop(0)
        self.give_points_to_cards(NP_rest_of_cards)
        self.cards.sort(key = lambda c:c.value)
        cards_to_gave_away.append(self.cards[0])
        self.cards.pop(0)
        self.cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        return cards_to_gave_away
    
    # Determines which card the computer player will play, considering the cards on the table, the atut and the cards that are still in play    
    def make_a_move(self, NP_rest_of_cards, on_table, atu):
        #print_cards(self.cards)
        self.give_points_to_cards(NP_rest_of_cards)
        card_to_give = Card("A", "Error")
        if on_table:
            if self.if_any_higher_card(on_table, atu):
                self.cards.sort(key = lambda c:c.value, reverse=True)
                for card in self.cards:
                    if self.is_valid_move(card, on_table, atu):
                        card_to_give = card
                        break
                self.cards.remove(card_to_give)
                self.cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
                return card_to_give
            else:
                self.cards.sort(key = lambda c:c.value)
                for card in self.cards:
                    if self.is_valid_move(card, on_table, atu):
                        card_to_give = card
                        break
                self.cards.remove(card_to_give)
                self.cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
                return card_to_give
        else:
            for color in colors:
                if any(c.figure == "D" and c.color == color for c in self.cards) and any(c.figure == "K" and c.color == color for c in self.cards) and any(c.figure == "A" and c.color == color for c in self.cards):
                    found = next((c for c in self.cards if c.figure == "A" and c.color == color), None)
                    if found and atu == "":
                        found.value+=20
                    else:
                        print("Make a move error")
                if any(c.figure == "10" and c.color == color for c in self.cards) and any(c.figure != "10" and c.color == color for c in self.cards) and (sum(c.color == color for c in self.cards) == 2):
                    found = next((c for c in self.cards if c.figure != "10" and c.color == color), None)
                    if found and atu == "":
                        found.value+=11
                    else:
                        print("Make a move error")        
            self.cards.sort(key = lambda c:c.value, reverse = True)
            card_to_give = self.cards[0]
            self.cards.pop(0)
            self.cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
            return card_to_give
            
            
        


            
