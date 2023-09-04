import random

COLOR_RESET = '\x1b[0m'
COLOR_BLUE = '\x1b[0;34;48m'
COLOR_BLUE_BG = '\x1b[7;34;48m'
COLOR_PURPLE = '\x1b[0;35;48m'
COLOR_RED = '\x1b[0;31;48m'
COLOR_RED_BG = '\x1b[7;31;48m'
COLOR_TEAL_BG = '\x1b[7;36;48m'
COLOR_GREEN = '\x1b[7;36;48m'
COLOR_YELLOW = '\x1b[7;33;48m'
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            print('')
            chips.bet = int(input(COLOR_TEAL_BG+BOLD+'How many chips would you like to bet?'+COLOR_RESET + ' '))
        except ValueError:
            print('')
            print(FAIL+BOLD+'Invalid! Please try again'+COLOR_RESET)
        else:
            if chips.bet > chips.total:
                print('')
                print(FAIL+BOLD+"Exceeding limit (100 chips)")
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input(COLOR_BLUE_BG+BOLD+"Would you like to Hit or Stand? Enter 'h' or 's':" + COLOR_RESET + " ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print('')
            print(OKGREEN+"Player stands. Dealer is playing."+COLOR_RESET)
            playing = False

        else:
            print('')
            print(FAIL+BOLD+"Sorry, please try again."+COLOR_RESET)
            print('')
            continue
        break


def show_some(player,dealer):
    print(WARNING+"\nDealer's Hand:"+COLOR_RESET)
    print('')
    print(FAIL+' '+"|Hidden Card|"+COLOR_RESET)
    print('',COLOR_BLUE+f"{dealer.cards[1]}"+COLOR_RESET)  
    print(WARNING+"\nPlayer's Hand:"+COLOR_RESET)
    print(COLOR_BLUE)
    print('',*player.cards, sep='\n ')
    print(COLOR_RESET)


def show_all(player,dealer):
    print(WARNING+"\nDealer's Hand:"+COLOR_RESET)
    print('') 
    print(COLOR_BLUE)
    print('',*dealer.cards, sep='\n ')
    print(COLOR_RESET)
    print(WARNING+f"Dealer's Hand = {dealer.value}"+COLOR_RESET)
    print(WARNING+"\nPlayer's Hand:"+COLOR_RESET) 
    print('')
    print(COLOR_BLUE)
    print(*player.cards, sep='\n ')
    print(COLOR_RESET)
    print(WARNING+f"Player's Hand = {player.value}"+COLOR_RESET)

def player_busts(player,dealer,chips):
    print('')
    print(COLOR_PURPLE+BOLD+"Player busts!"+COLOR_RESET)
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('')
    print(OKGREEN+"Player wins!"+COLOR_RESET)
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('')
    print(OKCYAN+BOLD+"Dealer busts!"+COLOR_RESET)
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('')
    print(OKGREEN+"Dealer wins!"+COLOR_RESET)
    chips.lose_bet()
    
def push(player,dealer):
    print('')
    print(COLOR_RED_BG+BOLD+"Dealer and Player tie!"+COLOR_RESET)

while True:
    # Print an opening statement
    print(COLOR_PURPLE+'__________.__                 __        ____.              __    '+COLOR_RESET)
    print(COLOR_PURPLE+'\______   \  | _____    ____ |  | __   |    |____    ____ |  | __'+COLOR_RESET)
    print(COLOR_PURPLE+' |    |  _/  | \__  \ _/ ___\|  |/ /   |    \__  \ _/ ___\|  |/ /'+COLOR_RESET)
    print(COLOR_PURPLE+' |    |   \  |__/ __ \\  \___|    </\__|    |/ __ \\  \___|    < '+COLOR_RESET)
    print(COLOR_PURPLE+' |______  /____(____  /\___  >__|_ \________(____  /\___  >__|_ \\'+COLOR_RESET)
    print(COLOR_PURPLE+'        \/          \/     \/     \/             \/     \/     \/'+COLOR_RESET)
    print('')
    print(COLOR_BLUE_BG+BOLD+'Welcome to BlackJack! Get as close to 21 as you can without going over!'+COLOR_RESET)
    print('')
    print(COLOR_RED_BG+BOLD+'Dealer hits until she reaches 17. Aces count as 1 or 11.'+COLOR_RESET)
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print(COLOR_TEAL_BG+BOLD+f"\nPlayer's winnings stand at {player_chips.total}"+COLOR_RESET)
    print('')
    
    # Ask to play again
    def new_game_func():
        global new_game
        new_game = input(COLOR_BLUE_BG+BOLD+"Would you like to play another hand? Enter 'y' or 'n':"+COLOR_RESET + ' ')

    new_game_func()

    if new_game[0].lower()=='y':
        playing=True
        continue
    if new_game[0].lower() == 'n':
        print('')
        print(COLOR_RED_BG+BOLD+"Thanks for playing!"+COLOR_RESET)
        break
    else:
        print('')
        print(FAIL+BOLD+'Invalid Input, please try again'+COLOR_RESET)
        print('')
        new_game_func()