import random

#Base variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

# Class Card
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return ("{} of {}".format(self.rank, self.suit))

# Deck Class
class Deck(Card):

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append("{} of {}".format(rank, suit))

    def __str__(self):
        return self.deck

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        player.cards.append(self.deck.pop(0))
        dealer.cards.append(self.deck.pop(0))

# Hand class
class Hand():
    def __init__(self, name, cards=[], value=0, aces=0):
        self.name = name
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self):
        self.value = 0
        for card in self.cards:
            card = card.split()
            if card[0] != "Ace":
                self.value += values[card[0]]
        return int(self.value)

    def adjust_for_ace(self):
        for card in self.cards:
            card = card.split()
            if card[0] == "Ace" and self.value <= 10:
                self.aces = 11
                self.value += self.aces
            elif card[0] == "Ace":
                self.aces == 1
                self.value += self.aces
            else:
                break
        return self.value

    def __str__(self):
        return self.cards

# Chips class
class Chips():

    def __init__(self, total=100, bet=0):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet

    def __str__(self):
        return self.total

# Taking bets
def initial_money(Chips):
    while True:
        try:
            chips.total = int(input("How much do you want to start with? "))
        except:
            print ("Please insert a number ")
            continue
        else:
            break

def take_bet(Chips):
    while True:
        try:
            chips.bet = int(input("How much do you want to bet? "))
            while chips.bet > chips.total:
                chips.bet = int(input("You don't have enough funds. How much do you want to bet? "))
        except:
            print ("Please insert a number ")
            continue
        else:
            print ("Your bet is of {}".format(chips.bet))
            break

# Hit
def hit(deck,player):
    player.cards.append(deck.deck.pop(0))

# Hit or stand
def hit_or_stand(Deck,Hand):
    while True and not player_busts(Hand, Chips):
        option = input("Do you want to hit or stand? ")
        if option == "hit":
            hit(deck, player)
            player.add_card()
            player.adjust_for_ace()
            show_some(player,dealer)
            continue
        elif option == "stand":
            break
        else:
            print("Please insert a valid option ")

# Dealer's action
def dealer_action(Deck, Hand, Chips):
    if not player_busts_2(Hand, Chips):
        while dealer.value <= 17:
            dealer.cards.append(deck.deck.pop(0))
            dealer.value = dealer.add_card()
            dealer.value = dealer.adjust_for_ace()
            print("-----------------------------------------------")
            show_some(player,dealer)
            print("-----------------------------------------------")
        print("-----------------------------------------------")
        show_all(player,dealer)
        print("-----------------------------------------------")
        dealer_busts()
        player_wins()
        dealer_wins()
        push()
    else:
        print("-----------------------------------------------")
        show_all(player,dealer)
        print("-----------------------------------------------")
        player_wins()
        dealer_wins()
        push()

# Show Cards
def show_some(player,dealer):
    print ("Player: {}".format(player.cards[0:]))
    print ("Dealer: {}".format(dealer.cards[1:]))
def show_all(player,dealer):
    print ("Player: {}".format(player.cards[0:]))
    print ("Dealer: {}".format(dealer.cards[0:]))

# Scenarios
def player_busts(Hand, Chips):
    if player.value > 21:
        print("I am sorry,  you lost this time!")
        chips.lose_bet()
        return True
    else:
        return False


def player_busts_2(Hand, Chips):
    if player.value > 21:
        return True


def dealer_busts():
    if dealer.value > 21:
        print("Congratulations, you have won!")
        chips.win_bet()


def player_wins():
    if dealer.value < player.value <= 21:
        print("Congratulations, you have won!")
        chips.win_bet()


def dealer_wins():
    if player.value < dealer.value <= 21:
        print("I am sorry,  you lost this time!")
        chips.lose_bet()


def push():
    if player.value == dealer.value:
        print("Push!")

#Replay
def replay():
    option = ""
    print("-----------------------------------------------")
    option = input("Do you want to play again? Yes or No? ").capitalize()
    print("-----------------------------------------------")
    while option != "":
        if option == "Yes":
            player.cards.clear()
            dealer.cards.clear()
            player.value = 0
            dealer.value = 0
            player.aces = 0
            dealer.aces = 0
            deck = Deck()
            deck.shuffle()
            return True
        elif option == "No":
            return False
        else:
            print("-----------------------------------------------")
            option = input("Insert a valid option. Do you want to play again? Yes or no? ").capitalize()
            print("-----------------------------------------------")

# GAME
# Opening Statement
print("Welcome to Fede's Blackjack! Get ready to start")

# Game classes
chips = Chips()
player = Hand("Player")
dealer = Hand("Dealer")
initial_money(chips)

while True:

    # Shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    deck.deal()
    deck.deal()
    # Set up the Player's chips
    print("-----------------------------------------------")
    print("Your total amount is {}".format(chips.total))
    take_bet(chips)
    print("-----------------------------------------------")

    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)
    print("-----------------------------------------------")

    # Prompt for Player to Hit or Stand
    hit_or_stand(deck, player)

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    dealer.value = dealer.add_card()
    dealer.valule = dealer.adjust_for_ace()
    dealer_action(deck,dealer,chips)

    # Inform Player of their chips total
    print("-----------------------------------------------")
    print("Your total amount is {}".format(chips.total))
    print("-----------------------------------------------")

    if chips.total == 0:
        print("-----------------------------------------------")
        print("I am sorry, you run out of money!")
        print("-----------------------------------------------")
        break

    # Ask to play again
    if not replay():
        print("-----------------------------------------------")
        print("Thank you for playing Fede's Blackjack")
        print("-----------------------------------------------")

        break

