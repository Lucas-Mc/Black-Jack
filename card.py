class Card:

  def __init__(self, suit, value):
    # Each card has a suit and a value
    self.suit = suit
    self.value = value

  def get_suit(self):
    # Get the suit of the card
    return self.suit

  def get_value(self):
    # Get the value of the card
    return self.value

  def __str__(self):
    # Print the object in the desired format
    return "{} of {}".format(self.value, self.suit)

        