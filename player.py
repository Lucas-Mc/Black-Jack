from card import Card

class Player:

    def __init__(self):
        # Each player starts with an empty hand
        self.cards = []

    def receive_card(self,card):
        # Add the new card to the player's hand
        self.cards.append(card)

    def remove_card(self):
        # Remove a card from the player's hand
        self.cards.pop()

    def print_cards(self):
        for card in self.cards:
            print(card)

    def add_cards(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total

    def make_decision(self):
        decision = "a"
        while ((decision != "s") and (decision != "h")):
            decision = input("Type 's' for stand, or 'h' for hit: ")
            if ((decision != "s") and (decision != "h")):
                print("Incorrect input")
        return decision
