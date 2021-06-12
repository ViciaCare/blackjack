import random

suits = pass
ranks = pass
values = pass

playing = True


class Card:
    def __init__(self):
        pass

    def __str__(self):
        pass


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                pass

    def __str__(self):
        pass

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        pass


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        pass

    def adjust_for_ace(self):
        pass


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass


def take_bet():
    pass


def hit(deck, hand):
    pass


def hit_or_stand(deck, hand):
    global playing
    pass


def show_some(player, dealer):
    pass


def show_all(player, dealer):
    pass


def player_busts():
    pass


def player_wins():
    pass


def dealer_busts():
    pass


def dealer_wins():
    pass


def push():
    pass

while True:
    #greating massage
    #create deck of cards
    #set the number of the player's chips
    #ask the player for his bet
    #show the cards (except one card and cards dealer)
    pass
    while playing:
        #ask player, if he wants to draw an additional card or stay with the current cards
        pass