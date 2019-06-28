from card import Card
import random

class CardList():
  """
  CardList is a container object used for managing a list of cards
  during a card game.
  """
  def __init__(self, cards_to_start):
    '''
    cards_to_start: number of cards to be intialized
    '''
    # Initialize the card list as an empty list
    self.cards_to_start = cards_to_start
    self.cards = []
    self.create_deck(self.cards_to_start)

  def add_card(self, card):
    """
    Adds a input card to the card list
    """
    if (isinstance(card,Card)):
      self.cards.append(card)
    else:
      print('This is not the correct card type!')

  def create_deck(self, cards_to_start):
    # TODO: this function should be in the Deck class, a card list should know anything
    #  about what makes up a deck, this is just a storage mechanism
    # Create a deck of cards: 52 split 4 ways with heart, club, spade, and diamond suit		
    temp_cards = [Card("heart", i) for i in range(13)]		
    temp_cards += [Card("club", i) for i in range(13)]		
    temp_cards += [Card("spade", i) for i in range(13)]		
    temp_cards += [Card("diamond", i) for i in range(13)]		
    # Reduce the full deck to the desired number of cards		
    index_list = random.sample(range(52), cards_to_start)		
    [self.add_card(temp_cards[index_list[i]]) for i in range(len(index_list))]

  def pop_card(self):
    """
    Return the top card on the deck and remove it from the card list
    """
    if self.number_of_cards == 0:
      return None
    else:
      return self.cards.pop()

  def print_cards(self):
    """
    Print info for each the cards in the deck
    """
    if (self.number_of_cards == 0):
      print('There are no cards left in this deck!')
    else:
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
