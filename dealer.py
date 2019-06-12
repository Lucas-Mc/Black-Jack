from deck import Deck
from card import Card

class Dealer:

    def __init__(self):
        self.deck = Deck().cards
        print(len(self.deck))
        
    def deal(self):
        # Take the card on the top of the deck
        give_card = self.deck[0]
        # Remove the dealt card from the deck
        self.deck = self.deck[1:len(self.deck)]
        print(len(self.deck))
        return give_card

    