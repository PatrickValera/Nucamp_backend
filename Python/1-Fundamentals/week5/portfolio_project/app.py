import os
from typing import List, Dict
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# DECK CLASS =======================
class Deck:
    def __init__(self) -> None:
        self.cards:List[Card]=[]
        for suite in ['♠', '♦', '♥', '♣']:
            for value in range(1,11):
                self.cards.append(Card(value,suite,value))
            for face in ["Jack","Queen","King"]:
                self.cards.append(Card(10,suite,face))
        random.shuffle(self.cards)
    def draw_card(self)->"Card":
        return self.cards.pop()

# Card CLASS =======================
class Card:
    def __init__(self,value,suite,card,hidden=False) -> None:
        self.hidden=hidden
        self.value:int=value
        self.suite:str=suite
        self.card:str=str(card)

# Hand CLASS =======================
class Hand:
    def __init__(self) -> None:
        self.value=0
        self.cards_in_hand:List[Card]=[]
        self.bust=False
        pass
    def add_card(self,card:Card):
        self.value+=card.value
        self.cards_in_hand.append(card) 
    def print_hand(self):
        result:List[List]=[[],[],[],[],[]]
        for card in self.cards_in_hand:
            if card.hidden == False:
                result[0].append('┌───────┐')
                result[1].append('│       │')
                result[2].append('│ {} {}  │'.format(' '+card.card[:1] if card.card!='10' else '10',card.suite))
                result[3].append('│       │')
                result[4].append('└───────┘')
            else:
                result[0].append('┌───────┐')
                result[1].append('│░░░░░░░│')
                result[2].append('│░░░░░░░│')
                result[3].append('│░░░░░░░│')
                result[4].append('└───────┘')
        for line in result:
            for x in line:
                print(x,end=' ')
            print('')

# BlackJack CLASS =======================
class BlackJack:
    def __init__(self) -> None:
        clear_console()
        self.deck=Deck()
        self.player_credit=1000
        self.player_hand=Hand()
        self.dealer_hand=Hand()

        print("Black Jack Game")
        while self.player_credit>0:
            print(f"Remaining Credit: {self.player_credit}")
            bet=int(input("Enter Bet: "))
            self.start_player_turn()
            self.dealer_hand.cards_in_hand[0].hidden=False
            clear_console()
            if self.player_hand.bust:
                self.player_credit-=bet
                self.display_table()
                print("Player Busts.")
            else:
                self.start_dealer_turn()
                if self.dealer_hand.bust:
                    self.display_table()
                    print("Dealer Busts.")
            if self.dealer_hand.value>self.player_hand.value and not self.dealer_hand.bust or self.player_hand.bust:
                self.player_credit-=bet
                print("Dealer Wins")
            elif self.dealer_hand.value<self.player_hand.value and not self.player_hand.bust or self.dealer_hand.bust:
                self.player_credit+=bet
                print("You win")
            else: 
                print("It's A Draw")
            self.deck=Deck()
            self.dealer_hand=Hand()
            self.player_hand=Hand()
    # START PLAYER ============================================
    def start_player_turn(self):
        self.player_hand.add_card(self.deck.draw_card())
        self.player_hand.add_card(self.deck.draw_card())
        hidden_card=self.deck.draw_card()
        hidden_card.hidden=True
        self.dealer_hand.add_card(hidden_card)
        self.dealer_hand.add_card(self.deck.draw_card())
        clear_console()
        self.display_table()
        move=input("Hit or Stand")
        while move in ['hit','Hit','1']:
            clear_console()
            self.player_hand.add_card(self.deck.draw_card())
            if self.player_hand.value>21:
                self.player_hand.bust=True
                return
            self.display_table()
            move=input("Hit or Stand")
        else: return
    # START DEALER ============================================
    def start_dealer_turn(self):
        self.dealer_hand.cards_in_hand[0].hidden=False
        while self.dealer_hand.value<17:
            self.dealer_hand.add_card(self.deck.draw_card())
            if(self.dealer_hand.value>21):
                self.dealer_hand.bust=True
                return
            self.display_table()
            clear_console()
        self.display_table()
    # DISPLAY TABLE ============================================
    def display_table(self):
        if(self.dealer_hand.cards_in_hand[0].hidden): print(f"===== Dealer: {self.dealer_hand.value-self.dealer_hand.cards_in_hand[0].value} =====")
        else: print(f"===== Dealer: {self.dealer_hand.value} =====")
        self.dealer_hand.print_hand()
        self.player_hand.print_hand()
        print(f"===== Player: {self.player_hand.value} =====")

game=BlackJack()