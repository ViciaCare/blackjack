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
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Do you want to take an extra card (h - Hit) or stay with the current cards (s - Stand)? Enter 'h' or 's'")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("The player stays with the current cards. Dealer's move." )
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    print('\nDealer cards:')
    print('<card hidden>')
    print('', dealer.cards[1])
    print('\nPlayer cards:', *player.cards, sep='\n ')


def show_all(player, dealer):
    print('\nDealer cards:', *dealer.cards, sep='\n ')
    print('Dealer cards =', dealer.value)
    print('\nPlayer.cards:', *player.cards, sep='\n ')
    print('Player cards =', player.value)


def player_busts(player, dealer, chips):
    print('The player has exceeded 21!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player win!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('The dealer has exceeded 21!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer win!')
    chips.lose_bet()


def push(player, dealer):
    print('Draw!')


while True:
    print('Welcome to Blackjack game! Try to get as close to the sum of 21 as possible without exceeding it!\n\
    The dealer takes additional cards until he receives an amount greater than 17. The ace counts as 1 or 11.')
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        #ask player, if he wants to draw an additional card or stay with the current cards
        pass