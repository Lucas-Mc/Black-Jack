from deck import Deck
from card import Card

class Dealer:

    def __init__(self):
        self.deck = Deck()
        self.cards = self.deck.cards
        self.deck.shuffle()
        
    def deal(self):
        # Take the card on the top of the deck and remove
        return self.deck.pop()
