from card import Card
from cardlist import CardList

class Player(CardList):

  def __init__(self):
    # Each player starts with an empty hand
    CardList.__init__(self,0)

  def receive_card(self,card):
    # Add the new card to the player's hand
    self.cards.append(card)

  def make_decision(self):
    # Decide between stand ('s') and hit ('h') 
    decision = "a"
    while ((decision != "s") and (decision != "h")):
      decision = input("Type 's' for stand, or 'h' for hit: ")
      if ((decision != "s") and (decision != "h")):
        print("Incorrect input")
    return decision

  def flush_cards(self):
    # Remove all the cards in the player's hand
    for _ in range(self.number_of_cards):
      self.pop_card()
