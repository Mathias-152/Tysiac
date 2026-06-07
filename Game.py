import random
from Player import Player, HumanPlayer, ComputerPlayer
from Utilities import *
from Card import Card
import pygame
from sys import exit
from Button import *
import time



class Game:
    
    def __init__(self, player1):
        pygame.init()
        pygame.display.set_caption('Tysiąc')
        self.round_nr = 1
        self.players = [player1, ComputerPlayer("Left", 1), ComputerPlayer("Right", 2)]
        self.player_scores = [0, 0, 0]
        self.table_cards = []
        self.rest_of_cards = []
        self.screen = pygame.display.set_mode((1280,660))
        self.font = pygame.font.Font(None, 30)
        self.sfont = pygame.font.Font(None, 20)
        self.clock = pygame.time.Clock()

    # Deals cards to players and prepares the rest of the cards for the bidding phase
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
    # Draws the bidding screen, showing the players' cards, the current highest bid, and the buttons for placing bids. It also handles the display of the cards that players will give away to the highest bidder after the bidding phase.
    def draw_bidding(self, Bet_Buttons, curr_bet, highest_bet, highest_bidder, reset_button, reset_button_visible = False):
        background_surf = pygame.image.load(f"{path}/Images/Background.png").convert_alpha()
        self.screen.blit(background_surf, (0,0))
        back_card = pygame.image.load(f"{path}/Images/BACK.png")
        back_card = pygame.transform.scale(back_card, (100,150))
        curr_surf = self.font.render(f"Current bet: {curr_bet}", True, 'Gold')
        curr_rect = curr_surf.get_rect(center = (640, 320)) 
        h_bidder_surf = self.font.render(f"Highest bet: {highest_bet}", True, 'Gold')
        h_bidder_surf2 = self.font.render(f"by: {highest_bidder}", True, 'Gold')
        self.screen.blit(h_bidder_surf, (200, 50))
        self.screen.blit(h_bidder_surf2, (200, 80))
        for i in range(len(self.players[1].cards)):
            self.screen.blit(back_card, (0,0+40*i))
        for i in range(len(self.players[2].cards)):    
            self.screen.blit(back_card, (1130,0+40*i))
        for i in range(len(self.players[0].cards)):    
            c = pygame.image.load(f"{path}/Images/{self.players[0].cards[i].figure}{self.players[0].cards[i].color}.png")
            c = pygame.transform.scale(c, (100,150))
            c_rect = c.get_rect(center = (((1280-len(self.players[0].cards)*100)/2)+i*100, 547))
            self.screen.blit(c, c_rect)
        self.screen.blit(curr_surf, curr_rect)
        for bt in Bet_Buttons:
            self.screen.blit(bt.surface, bt.rect)
        if reset_button_visible:
            self.screen.blit(reset_button.surface, reset_button.rect)
        scores_text = [
        f"Final scores:",
        f"{self.players[0].name}: {self.player_scores[0]}",
        f"{self.players[1].name}: {self.player_scores[1]}",
        f"{self.players[2].name}: {self.player_scores[2]}"
        ]
        start_x = 1100
        start_y = 500
        line_height = 40
        for i, text_line in enumerate(scores_text):
            score_surf = self.sfont.render(text_line, True, 'Red')
            self.screen.blit(score_surf, (start_x, start_y + (i * line_height)))
        pygame.display.update()
    # Draws the screen for the phase where the highest bidder gives away two cards to the other players. It shows the highest bidder's cards and allows the player to select which cards to give away.
    def draw_gave_avay(self, cb, highest_bidder, highest_bet):
        cards = [Card_Button(self.players[0].cards[i], ((1280-len(self.players[0].cards)*100)/2)+i*100,547) for i in range(len(self.players[0].cards))]
        background_surf = pygame.image.load(f"{path}/Images/Background.png").convert_alpha()
        self.screen.blit(background_surf, (0,0))
        back_card = pygame.image.load(f"{path}/Images/BACK.png")
        back_card = pygame.transform.scale(back_card, (100,150))
        h_bidder_surf = self.font.render(f"Highest bet: {highest_bet}", True, 'Gold')
        h_bidder_surf2 = self.font.render(f"by: {highest_bidder}", True, 'Gold')
        self.screen.blit(h_bidder_surf, (200, 50))
        self.screen.blit(h_bidder_surf2, (200, 80))
        for i in range(len(self.players[1].cards)):
            self.screen.blit(back_card, (0,0+40*i))
        for i in range(len(self.players[2].cards)):    
            self.screen.blit(back_card, (1130,0+40*i))
        for c in cards:
            self.screen.blit(c.surface, c.rect)
        give_away = Button("GiveAway", 640, 420, 200, 50)
        self.screen.blit(give_away.surface, give_away.rect)
        for i in range(len(cb)):
            self.screen.blit(cb[i].surface, cb[i].rect)
        scores_text = [
        f"Final scores:",
        f"{self.players[0].name}: {self.player_scores[0]}",
        f"{self.players[1].name}: {self.player_scores[1]}",
        f"{self.players[2].name}: {self.player_scores[2]}"
        ]
        start_x = 1100
        start_y = 500
        line_height = 40
        for i, text_line in enumerate(scores_text):
            score_surf = self.sfont.render(text_line, True, 'Red')
            self.screen.blit(score_surf, (start_x, start_y + (i * line_height)))
            
        pygame.display.update()
        return cards, give_away

    # Handles the bidding phase of the game, where players can place their bids based on their cards and the current highest bid. It also handles the exchange of cards between the highest bidder and the other players.
    def bidding_phase(self):
        highest_bid = 100
        highest_bidder = self.players[self.round_nr%3]
        bidder = self.players[(self.round_nr+1)%3]
        passed_players = []
        possible_bet = [0, 5, 10, 15, 20, 50, 100]
        reset_button = Button("Reset", 1000, 415, 180, 70)
        bet_buttons = [Bet_Button(f"Bet{str(possible_bet[i])}", 437 + 132 * i if i < 4 else 569 + 132 * (i - 4), 415 if i == 0 else 395 if i < 4 else 435, 120 , 70 if i == 0 else 30, possible_bet[i]) for i in range(len(possible_bet)) ]
        while len(passed_players) < 2:
            if bidder in passed_players:
                bidder = self.players[(bidder.id+1)%3]
                continue
            if bidder.id!=0:
                bet = bidder.make_a_bid(highest_bid, highest_bidder, 0, self.rest_of_cards)
                if bet == 0:
                    passed_players.append(bidder)
                else:
                    highest_bid += bet
                    highest_bidder = self.players[bidder.id]
                bidder = self.players[(bidder.id+1)%3]
            else:
                action_taken = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    for bb in bet_buttons:
                        if event.type == pygame.MOUSEBUTTONDOWN and bb.is_clicked(pygame.mouse.get_pos()):
                            if bb.value == 0:
                                passed_players.append(bidder)
                                action_taken = True
                            else:
                                highest_bid += bb.value
                                highest_bidder = self.players[bidder.id]
                                action_taken = True
                    if action_taken:
                        bidder = self.players[(bidder.id+1)%3]
            self.draw_bidding(bet_buttons, highest_bid, highest_bid, highest_bidder.name, reset_button)
            self.clock.tick(30)
        # print("Highest bidder: " + highest_bidder.name + " with a bet of " + str(highest_bid))
        while len(self.table_cards) > 0:
            temp = self.table_cards.pop(0)
            highest_bidder.cards.append(temp)
        highest_bidder.cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        self.draw_bidding(bet_buttons, highest_bid, highest_bid, highest_bidder.name, reset_button)


        
        if highest_bidder.id != 0:
            cards_to_give = highest_bidder.gave_away(self.rest_of_cards)
        else:
            done = False
            cards_to_give_b = []
            cards_to_give = []
            while not done:
                card_buttons, ga_button = self.draw_gave_avay(cards_to_give_b, highest_bidder.name, highest_bid)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    temp = True
                    for i in range(len(card_buttons)):
                        if event.type == pygame.MOUSEBUTTONDOWN and card_buttons[i].is_clicked(pygame.mouse.get_pos()) and len(cards_to_give_b) < 2:
                            cards_to_give_b.append(card_buttons[i])
                            card_buttons[i].reposition(490+len(cards_to_give_b)*100, 220)
                            cards_to_give.append(self.players[0].cards[i])
                            self.players[0].cards.pop(i)
                            card_buttons, ga_button = self.draw_gave_avay(cards_to_give_b, highest_bidder.name, highest_bid)
                            temp = False
                            break
                    if temp:
                        for i in range(len(cards_to_give_b)):
                            if event.type == pygame.MOUSEBUTTONDOWN and cards_to_give_b[i].is_clicked(pygame.mouse.get_pos()):
                                self.players[0].cards.append(cards_to_give[i])
                                self.players[0].cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
                                cards_to_give.pop(i)
                                cards_to_give_b.pop(i)
                                if len(cards_to_give_b) == 1:
                                    cards_to_give_b[0].reposition(590, 220)
                                card_buttons, ga_button = self.draw_gave_avay(cards_to_give_b, highest_bidder.name, highest_bid)
                                break
                    if event.type == pygame.MOUSEBUTTONDOWN and ga_button.is_clicked(pygame.mouse.get_pos()):
                        if len(cards_to_give) == 2:
                            done = True
        self.players[(highest_bidder.id+1)%3].cards.append(cards_to_give[0])
        self.players[(highest_bidder.id+2)%3].cards.append(cards_to_give[1])
        self.players[(highest_bidder.id+1)%3].cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        self.players[(highest_bidder.id+2)%3].cards.sort(key = lambda card: (color_order[card.color],figure_order[card.figure]))
        
        reset_value = highest_bid
        if(highest_bidder.id!=0):
            bet = int(highest_bidder.make_a_bid(highest_bid, highest_bidder, 1, self.rest_of_cards))
            highest_bid += bet
            print("New bet: " + str(highest_bid))
        else:
            done = False
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    for bb in bet_buttons:
                        if event.type == pygame.MOUSEBUTTONDOWN and bb.is_clicked(pygame.mouse.get_pos()):
                            if bb.value == 0:
                                done = True
                            else:
                                highest_bid += bb.value
                    if event.type == pygame.MOUSEBUTTONDOWN and reset_button.is_clicked(pygame.mouse.get_pos()):
                        highest_bid = reset_value
                self.draw_bidding(bet_buttons, highest_bid, highest_bid, highest_bidder.name, reset_button, True)
        return highest_bidder.id, highest_bid
    # Draws the playing phase screen, showing the players' cards, the cards on the table, the current atut (trump suit), and the highest bid. It also handles the display of the cards played by each player during their turn.
    def draw_playing(self, on_table, atut, highest_bidder_id, highest_bid, invalid = []):
        cards = [Card_Button(self.players[0].cards[i], ((1280-len(self.players[0].cards)*100)/2)+i*100,547) for i in range(len(self.players[0].cards))]
        for i in invalid:
            cards[i].surface.set_alpha(100)
        background_surf = pygame.image.load(f"{path}/Images/Background.png").convert_alpha()
        self.screen.blit(background_surf, (0,0))
        back_card = pygame.image.load(f"{path}/Images/BACK.png")
        back_card = pygame.transform.scale(back_card, (100,150))
        h_bidder_surf = self.font.render(f"Highest bet: {highest_bid}", True, 'Gold')
        h_bidder_surf2 = self.font.render(f"by: {self.players[highest_bidder_id].name}", True, 'Gold')
        self.screen.blit(h_bidder_surf, (200, 50))
        self.screen.blit(h_bidder_surf2, (200, 80))
        for i in range(len(self.players[1].cards)):
            self.screen.blit(back_card, (0,0+40*i))
        for i in range(len(self.players[2].cards)):    
            self.screen.blit(back_card, (1130,0+40*i))
        for c in cards:
            self.screen.blit(c.surface, c.rect)
        for i in range(len(on_table)):
            c = pygame.image.load(f"{path}/Images/{on_table[i].figure}{on_table[i].color}.png")
            c = pygame.transform.scale(c, (100,150))
            self.screen.blit(c, (440+i*100, 260 if i == 1 else 220))
        if atut != "":
            atut_surf = pygame.image.load(f"{path}/Images/{atut}.png").convert_alpha()
            atut_surf = pygame.transform.scale(atut_surf, (50, 58.5))
            self.screen.blit(atut_surf, (900, 70))
        scores_text = [
        f"Final scores:",
        f"{self.players[0].name}: {self.player_scores[0]}",
        f"{self.players[1].name}: {self.player_scores[1]}",
        f"{self.players[2].name}: {self.player_scores[2]}"
        ]
        start_x = 1100
        start_y = 500
        line_height = 40
        for i, text_line in enumerate(scores_text):
            score_surf = self.sfont.render(text_line, True, 'Red')
            self.screen.blit(score_surf, (start_x, start_y + (i * line_height)))
        pygame.display.update()
        return cards

    # Handles the playing phase of the game, where players play their cards in turns and the winner of each trick is determined based on the rules of the game. It also keeps track of the points earned by each player from the cards they win in tricks.
    def playing_phase(self, first_player_id, highest_bidder, highest_bid):
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
                    return card.color
                else:
                    return atut
        sum_from_cards = [0, 0, 0]
        atut = ""
        while len(self.players[0].cards) > 0:
            print("*"*20)
            on_table = []
            for i in range(first_player_id, (first_player_id+3)):
                chosen_card = None
                player_id = i%3
                if player_id != 0:
                    chosen_card = self.players[player_id].make_a_move(self.rest_of_cards, on_table, atut)
                else:
                    done = False
                    invalid =[]
                    while not done:
                        card_buttons = self.draw_playing(on_table, atut, highest_bidder, highest_bid, invalid)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()
                            for i in range(len(card_buttons)):
                                if event.type == pygame.MOUSEBUTTONDOWN and card_buttons[i].is_clicked(pygame.mouse.get_pos()):
                                    chosen_card = self.players[0].cards[i]
                                    if self.players[0].is_valid_move(chosen_card, on_table, atut):
                                        self.players[0].cards.pop(i)
                                        card_buttons.pop(i)
                                        done = True
                                        break
                                    else:
                                        invalid.append(i)
                                        self.draw_playing(on_table, atut, highest_bidder, highest_bid, invalid)
                if on_table == []:
                    prev_atut = atut
                    atut = is_atut(chosen_card, self.players[player_id].cards, atut)
                    if atut != prev_atut:
                        sum_from_cards[player_id]+=color_value[atut]
                on_table.append(chosen_card)
                self.draw_playing(on_table, atut, highest_bidder, highest_bid)
                time.sleep(0.5)
                
            print("Cards on the table: ")
            print_cards(on_table)
            winning_card = on_table[0]
            for card in on_table:
                if card.color == winning_card.color and card.standard_value() > winning_card.standard_value():
                    #print("New winning card: " + str(card) + " Higher in color")
                    winning_card = card
                elif card.color == atut and winning_card.color != atut:
                    #print("New winning card: " + str(card) + " Atut beats non-atut")
                    winning_card = card
                elif atut is not None and card.color == atut and winning_card.color == atut and card.standard_value() > winning_card.standard_value():
                    #print("New winning card: " + str(card) + " Higher atut")
                    winning_card = card
            winning_player_id = (first_player_id + on_table.index(winning_card))%3
            sum_from_cards[winning_player_id] += sum(card.standard_value() for card in on_table)
            first_player_id = winning_player_id ###
        return sum_from_cards
    # Draws the end game screen, showing the winner and the final scores of all players. It also provides a button to restart the game.
    def draw_winner(self, winner):
        background_surf = pygame.image.load(f"{path}/Images/BackgroundSum.png").convert_alpha()
        self.screen.blit(background_surf, (0,0))
        winner_surf = self.font.render(f"{winner} won!", True, 'Red')
        winner_rect = winner_surf.get_rect(center = (640, 160))
        self.screen.blit(winner_surf, winner_rect)
        scores_text = [
        f"Final scores:",
        f"{self.players[0].name}: {self.player_scores[0]}",
        f"{self.players[1].name}: {self.player_scores[1]}",
        f"{self.players[2].name}: {self.player_scores[2]}"
        ]
        start_x = 500
        start_y = 200
        line_height = 40
        for i, text_line in enumerate(scores_text):
            score_surf = self.sfont.render(text_line, True, 'Red')
            self.screen.blit(score_surf, (start_x, start_y + (i * line_height)))
        restart = Button('Reset', 640, 530, 250, 80)
        self.screen.blit(restart.surface, restart.rect)
        pygame.display.update()
        return restart

    # Checks if any player has reached the score of 1000 or more, which would indicate that the game is finished
    def is_finnished(self):
        return any(score >= 10 for score in self.player_scores)
    
    # Handles the entire flow of a round, including dealing cards, bidding, playing, and updating scores. It also checks for the end of the game and declares the winner if the game is finished.
    def round(self):
        while(True):

            print("************************************* Round " + str(self.round_nr) + " *************************************")
            self.table_cards = self.deal_cards()
            self.players[1].give_points_to_cards(self.rest_of_cards)
            highest_bidder_id, highest_bid = self.bidding_phase()
            first_player_id = highest_bidder_id
            sum_from_cards = self.playing_phase(first_player_id, highest_bidder_id, highest_bid)
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
                m = max(self.player_scores)
                restart = None
                for i in range(3):
                    if self.player_scores[i] == m:
                        restart = self.draw_winner(self.players[i].name)
                        break
                done = False
                while not done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.MOUSEBUTTONDOWN and restart.is_clicked(pygame.mouse.get_pos()):
                            done = True
                            self.round_nr = 1
                            self.player_scores = [0, 0, 0]
                            self.table_cards = []
                            self.rest_of_cards = []

            else:
                self.round_nr += 1
    
    def draw_start(self):
        background_surf = pygame.image.load(f"{path}/Images/StartScreen.png")
        self.screen.blit(background_surf, (0, 0))
        start = Button('StartButton', 640, 430, 250, 80)
        self.screen.blit(start.surface, start.rect)
        pygame.display.update()
        return start

    def setup(self):
        start_button = self.draw_start()
        while(True):
            done = 0
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and start_button.is_clicked(pygame.mouse.get_pos()):
                        done = True
            self.round()

