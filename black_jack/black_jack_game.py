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