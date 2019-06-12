from card import Card

class Deck:
    
    def __init__(self):
        self.cards = [Card("heart", i) for i in range(13)]
        self.cards += [Card("club", i) for i in range(13)]
        self.cards += [Card("spade", i) for i in range(13)]
        self.cards += [Card("diamond", i) for i in range(13)]

    def shuffle(self):
        pass
