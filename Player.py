from Utilities import *
from Card import Card
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
    
    def is_valid_move(self, card_to_play, on_table, atut):
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
        has_color = any(card.color == leading_color for card in self.cards)
        has_atut = any(card.color == atut for card in self.cards)
        if has_color:
            if card_to_play.color != leading_color:
                print("You must follow the color of the first card on the table!")
                return False    
            else:
                if card_to_play.value() < winning_card.value() and card_to_play.color == winning_card.color and any(card.value() > winning_card.value() for card in self.cards if card.color == leading_color):
                    print("You must play a higher card of the leading color if you have one!")
                    return False
            return True
        if has_atut:
            if card_to_play.color != atut: 
                if winning_card.color == atut and not any(card.value() > winning_card.value() for card in self.cards if card.color == atut):
                    return True
                print("You must play the atut!")
                return False
            return True
        return True
    
    def worst_card(self):
        pass

    def best_card(self):
        pass

    

        

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name, 0)

    def make_a_move(self):
        pass

    def make_a_bid(self, highest_bid, highest_bidder, second_bidding):
        print("Your cards: ")
        print_cards(self.cards)
        bet = input("Current bet: " + str(highest_bid) + " by: " + highest_bidder.name + ", enter your bet increase (or '0' to pass): ")
        return bet

class ComputerPlayer(Player):
    def __init__(self, name, id):
        super().__init__(name, id)

    def evaluate_cards(self):
        points = 0
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
                        if found.value() > 4:
                            higher_tan_K += 1  
                    else:
                        continue
                for j in range(0, len(card_in_color[i]) - 2 + higher_tan_K):
                    points += card_in_color[i][j].value()
                    winning_cards[i].append(card_in_color[i][j])
                points += color_value[color]
            else: #if no atu in color
                for figure in figures:
                    found = next((c for c in self.cards if c.color == color and c.figure == figure), None)
                    if found:
                        winning_cards[i].append(found)
                        top_cards[i].append(found)
                        points += found.value()
                    else:
                        break
                for figure in figures:
                    found = next((c for c in self.cards if c.color == color and c.figure == figure), None)
                    if found:
                        card_in_color[i].append(found)
                    else:
                        continue
                if any(card.figure == "10" for card in card_in_color[i]) and any(card.figure != "10" and card.figure != "A" for card in card_in_color[i])and not any(card.figure == "A" for card in card_in_color[i]):
                    points += 10
                    winning_cards[i].append(next(card for card in card_in_color[i] if card.figure == "10"))
            if 6-len(card_in_color[i])-1 <= len(top_cards[i]): #If you take whole color
                for card in card_in_color[i]:
                    if card not in winning_cards[i]:
                        points += card.value()
                        winning_cards[i].append(card)
            i += 1

        # Cards from rest of players that can be taken by winning cards
        full_deck = [Card(figure, color) for figure in figures for color in colors]
        rest_of_cards = [card for card in full_deck if card not in self.cards]
        rest_of_cards.sort(key=lambda c: c.value())
        for card in rest_of_cards:
            if card in self.cards:
                rest_of_cards.remove(card)
        #print("Rest of cards: ", rest_of_cards, end="")
        for color in colors:
            for card in winning_cards[colors.index(color)]:
                for i in range(2):
                    if any(c.color == color and c.value() < card.value() for c in rest_of_cards):
                        found = next((c for c in rest_of_cards if c.color == color), None)
                        if found:
                            points += found.value()
                            rest_of_cards.remove(found)
                    else:
                        points+=rest_of_cards[0].value()
                        rest_of_cards.pop(0)
        #print(f"{self.name}'s card value = {points} for cards: {', '.join(str(card) for card in winning_cards)}")
        return points

    def make_a_bid(self, highest_bid, highest_bidder, second_bidding):
        score = self.evaluate_cards()
        bet = round((score)/5)*5
        if bet > highest_bid:
            if second_bidding:
                return bet - highest_bid
            else:
                return 5
        else:
            return 0
