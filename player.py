class Player:

    def __init__(self):
        self.cards = []

    def receive_card(self,card):
        self.cards.append(card)
        