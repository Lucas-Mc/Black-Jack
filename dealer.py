from deck import Deck

class Dealer():

  def __init__(self):
    self.deck = Deck()
    self.cards = self.deck.cards
    
  def deal(self):
    # Take the card on the top of the deck and remove
    return self.deck.pop_card()

