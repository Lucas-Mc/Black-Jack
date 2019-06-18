import random

class CardList:
    """
    CardList is a container object used for managing a list of cards
    during a card game.
    """
    def __init__(self):
        # initialize the card list as an empty list
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def pop_card(self):
        """
        Return the top card on the deck and remove it from the card list
        """
        return self.cards.pop()

    def print_cards(self):
        """
        Print info for each the cards in the deck
        """
        for card in self.cards:
            print(card)

    def shuffle(self):
        index_list = random.sample(range(self.number_of_cards), self.number_of_cards)
        self.cards = [self.cards[index] for index in index_list]

    @property
    def value(self):
        """
        Calculate the sum of all cards in the deck
        """
        return sum([card.value for card in self.cards])

    @property
    def number_of_cards(self):
        """
        Return the number of cards in the deck
        """
        return len(self.cards)
