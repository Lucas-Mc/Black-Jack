from card import Card
import random

class Deck:
    
    def __init__(self):
        # Create a deck of cards: 52 split 4 ways with heart, club, spade, and diamond suit
        self.cards = [Card("heart", i) for i in range(13)]
        self.cards += [Card("club", i) for i in range(13)]
        self.cards += [Card("spade", i) for i in range(13)]
        self.cards += [Card("diamond", i) for i in range(13)]

    def shuffle(self):
        #print(self.cards)
        # Change the order of the cards to simulate a shuffle
        random.shuffle(self.cards)
        #print(self.cards)
        return self.cards

