import random

suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "Jack", "Queen", "King", "Ace")
values = {"two":2, "three":3,"four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return self.rank + ' - ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))


    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck contains:' + deck_comp


    def shuffle(self):
        random.shuffle(self.deck)


    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0


    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet?"))
        except ValueError:
            print("Sorry the bet must be a number!")
        else:
            if chips.bet > chips.total:
                print("Sorry your bet must not exceed ", chips.total)
            else:
                break


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