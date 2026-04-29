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
                    if card.color == winning_card.color and card.standard_value() > winning_card.standard_value():
                        winning_card = card
                    elif card.color == atut and winning_card.color != atut:
                        winning_card = card
                    elif atut != "" and card.color == atut and winning_card.color == atut and card.standard_value() > winning_card.standard_value():
                        winning_card = card
        leading_color = on_table[0].color
        has_color = any(card.color == leading_color for card in self.cards)
        has_atut = any(card.color == atut for card in self.cards)
        if has_color:
            if card_to_play.color != leading_color:
                print("You must follow the color of the first card on the table!")
                return False    
            else:
                if card_to_play.value() < winning_card.standard_value() and card_to_play.color == winning_card.color and any(card.standard_value() > winning_card.standard_value() for card in self.cards if card.color == leading_color):
                    print("You must play a higher card of the leading color if you have one!")
                    return False
            return True
        if has_atut:
            if card_to_play.color != atut: 
                if winning_card.color == atut and not any(card.standard_value() > winning_card.standard_value() for card in self.cards if card.color == atut):
                    return True
                print("You must play the atut!")
                return False
            return True
        return True

    

        

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name, 0)

    def make_a_move(self):
        pass

    def make_a_bid(self, highest_bid, highest_bidder, second_bidding, NP_rest_of_cards):
        print("Your cards: ")
        print_cards(self.cards)
        bet = input("Current bet: " + str(highest_bid) + " by: " + highest_bidder.name + ", enter your bet increase (or '0' to pass): ")
        return bet
    
    def gave_away(self, NP_rest_of_cards):
        cards_to_give =[]
        print_cards(self.cards)
        l = input("Which cards do you want to discard to left player?")
        cards_to_give.append(self.cards.pop(int(l)))
        print_cards(self.cards)
        r = input("Which cards do you want to discard to right player?")
        cards_to_give.append(self.cards.pop(int(r)))
        return cards_to_give

class ComputerPlayer(Player):
    def __init__(self, name, id):
        super().__init__(name, id)

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
        #print("Rest of cards: ", rest_of_cards, end="")
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
        print_cards(self.cards)
        print(f"{self.name}'s card value = {points} for cards: {', '.join(str(card) for card in winning_cards)}")
        return points

    def make_a_bid(self, highest_bid, highest_bidder, second_bidding, NP_rest_of_cards):
        if highest_bidder.id == self.id and second_bidding == 0:
            return 0
        score = self.evaluate_cards(NP_rest_of_cards)
        bet = round((score)/5)*5
        if bet > highest_bid:
            if second_bidding:
                return bet - highest_bid
            else:
                return 5
        else:
            return 0


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
            
        #print_cards(self.cards)
        #for card in self.cards:
        #    print("  ", card.value, "  ", end="")
        return 



    def gave_away(self, NP_rest_of_cards):
        print_cards(self.cards)
        print("Player cards")
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
        
                        


            
