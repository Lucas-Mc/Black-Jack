from card import Card
import random

class Cardlist:

    def __init__(self,no_of_cards):
        # Set a variable to the number of cards in the deck
        self.no_of_cards = no_of_cards
        # Create a deck of cards: 52 split 4 ways with heart, club, spade, and diamond suit
        self.cards = [Card("heart", i) for i in range(13)]
        self.cards += [Card("club", i) for i in range(13)]
        self.cards += [Card("spade", i) for i in range(13)]
        self.cards += [Card("diamond", i) for i in range(13)]
        # Reduce the full deck to the desired number of cards
        index_list = random.sample(range(52), no_of_cards)
        self.cards = [self.cards[index_list[i]] for i in range(len(index_list))]

    def remove_card(self):
        # Remove the top card from the deck
        self.no_of_cards -= 1
        return self.cards.pop()

    def give_card(self):
        # Remove the top card from the deck
        self.no_of_cards += 1
        return self.cards[0]

    def count_cards(self):
        # Return the total number of cards in the deck
        return self.no_of_cards

    def print_cards(self):
        # Display each of the cards in the current deck
        for card in self.cards:
            print(card)

    def add_cards(self):
        # Determine the sum of all the cards in the deck
        total = 0
        for card in self.cards:
            total += card.value
        return total
        
