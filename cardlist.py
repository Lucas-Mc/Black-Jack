from card import Card
import random

class CardList():
  """
  CardList is a container object used for managing a list of cards
  during a card game.
  """
  def __init__(self, card_to_start):
    # initialize the card list as an empty list
    self.card_to_start = card_to_start
    self.create_deck(self.card_to_start)
    # print(self.cards)
    # self.cards = []

  def add_card(self, card):
    """
    Adds a input card to the card list
    """
    #TODO: add a safety check on input
    self.cards.append(card)

  def create_deck(self, card_to_start):
    # Create a deck of cards: 52 split 4 ways with heart, club, spade, and diamond suit	
    # TODO: make this use the `add_card` method?	
    self.cards = [Card("heart", i) for i in range(13)]		
    self.cards += [Card("club", i) for i in range(13)]		
    self.cards += [Card("spade", i) for i in range(13)]		
    self.cards += [Card("diamond", i) for i in range(13)]		
    # Reduce the full deck to the desired number of cards		
    index_list = random.sample(range(52), card_to_start)		
    self.cards = [self.cards[index_list[i]] for i in range(len(index_list))]

  def pop_card(self):
    """
    Return the top card on the deck and remove it from the card list
    """
    #TODO: handle errors like no cards available
    return self.cards.pop()

  def print_cards(self):
    """
    Print info for each the cards in the deck
    """
    #TODO: handle errors like no cards available
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
