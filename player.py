from card import Card

class Player:

    def __init__(self):
        # Each player starts with an empty hand
        self.cards = []

    def receive_card(self,card):
        # Add the new card to the player's hand
        self.cards.append(card)

    def print_cards(self):
        for card in self.cards:
            print(card)
