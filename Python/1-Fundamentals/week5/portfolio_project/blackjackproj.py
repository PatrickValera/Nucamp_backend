from typing import List
import os
import time
import random

# CLEAR CONSOLE =====
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# USED TO COLOR TERMINAL OUTPUT =====
class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
color=bcolors()

# DECK CLASS =======================
class Deck:
    def __init__(self) -> None:
        self.cards:List[Card]=[]
        for suite in ['♠', '♦', '♥', '♣']:
            for value in range(2,11):
                self.cards.append(Card(value,suite,value))
            for face in ["Jack","Queen","King"]:
                self.cards.append(Card(10,suite,face))
            self.cards.append(Card(11,suite,"Ace"))
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
        self.cards:List[Card]=[]
        self.bust=False
        self.blackjack=False
        pass
    def add_card(self,card:Card):
        self.value+=card.value
        self.cards.append(card) 
    def print_hand(self):
        result:List[List]=[[],[],[],[],[]]
        for card in self.cards:
            if card.hidden == False:
                result[0].append('┌───────┐')
                result[1].append('│       │')
                result[2].append('│ {}{}{} {}  │'.format(color.BOLD,' '+card.card[:1] if card.card!='10' else '10',color.END,card.suite))
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
    def __init__(self,credit=1000) -> None:
        self.deck=Deck()
        self.player_hand=Hand()
        self.dealer_hand=Hand()
        self.player_credit=credit
    def input_bet(self):
        bet=' '
        while True:
            try:
                bet=int(input("Enter bet: $"))
                break
            except ValueError:
                try:
                    float(bet)
                    print(f"{color.RED}Bets in whole dollar only{color.END}")
                except ValueError:
                    print(f"{color.RED}Bet must be a whole number{color.END}")
        return bet
    def start_game(self):
        self.display_table()
        while self.player_credit>0:
            self.__init__(self.player_credit)
            print(f"Remaining Credit: $ {color.GREEN}{self.player_credit}{color.END}")
            bet = self.input_bet()
            self.start_player_turn()
            self.dealer_hand.cards[0].hidden=False
            self.display_table(.5)
            if self.player_hand.blackjack:
                print(f"{color.GREEN}{color.BOLD}You got a Blackjack{color.END}{color.END}")
                print(f"{color.GREEN}* YOU WIN *{color.END}")
                self.player_credit+=bet*1.5
                continue
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
                print(f"{color.RED}* DEALER WINS *{color.END}")
            elif self.dealer_hand.value<self.player_hand.value and not self.player_hand.bust or self.dealer_hand.bust:
                self.player_credit+=bet
                print(f"{color.GREEN}* YOU WIN *{color.END}")
            else: 
                print(f"{color.ORANGE}It's A Draw{color.END}")
        print(f"{color.RED}{color.BOLD}GAME OVER. OUT OF CREDIT.\n{color.END}{color.END}")
    # DRAW A CARD FROM DECK AND PLACE IN PASSED IN HAND ======
    def draw_to(self,hand:Hand,card:Card=None):
        hand.add_card(self.deck.draw_card() if not card else card)
    # START PLAYER'S TURN ============================================
    def start_player_turn(self):
        hidden_card=self.deck.draw_card()
        hidden_card.hidden=True
        self.draw_to(self.dealer_hand,hidden_card)
        self.display_table(.5)
        self.draw_to(self.dealer_hand)
        self.display_table(.5)
        self.draw_to(self.player_hand)
        self.display_table(.5)
        self.draw_to(self.player_hand)
        self.display_table(.5)
        if self.player_hand.value==21:
            self.player_hand.blackjack=True
            return
        move='hit'
        while move in ['hit','Hit','1']:
            move=input(f"{color.BOLD}1 - Hit\n2 - Stand\nEnter next move: {color.END}")
            if move not in ['hit','Hit','1']:
                break
            self.player_hand.add_card(self.deck.draw_card())
            if self.player_hand.value>21:
                self.player_hand.bust=True
                return
            self.display_table()
        self.display_table()
    # START DEALER'S TURN ============================================
    def start_dealer_turn(self):
        self.dealer_hand.cards[0].hidden=False
        while self.dealer_hand.value<17:
            self.dealer_hand.add_card(self.deck.draw_card())
            if(self.dealer_hand.value>21):
                self.dealer_hand.bust=True
                return
            self.display_table(.5)
    # DISPLAY TABLE ============================================
    def display_table(self,delay=0):
        clear_console()
        space='            '
        print(f"{color.ORANGE}-------------Blackjack-------------{color.END} \n")
        if not self.dealer_hand.cards:
            print(f"{color.CYAN}{space}Dealer: 0{color.END}")
            print('\n'*4)
        else:
            if(self.dealer_hand.cards[0].hidden): 
                print(f"{color.CYAN}{space}Dealer: {self.dealer_hand.value-self.dealer_hand.cards[0].value}{space}{color.END}")
            else: 
                print(f"{color.CYAN}{space}Dealer: {self.dealer_hand.value}{space}{color.END}")
            self.dealer_hand.print_hand()
        print('=========='*max(len(self.dealer_hand.cards),len(self.player_hand.cards)))
        if not self.player_hand.cards:
            print('\n'*4)
        else:
            self.player_hand.print_hand()
        print(f"{color.CYAN}{space}Player: {self.player_hand.value}{space}{color.END}\n")
        print(f"{color.ORANGE}-----------------------------------{color.END} \n")
        time.sleep(delay)

game=BlackJack()
game.start_game()