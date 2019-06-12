from dealer import Dealer
from player import Player
from deck import Deck
from card import Card

# Initialize a dealer object
dealer = Dealer()
# Initialize a deck object
deck = Deck()
print(deck)
# Start by shuffling the deck
deck.shuffle()
print(deck)

# Initialize two players for the game
player1 = Player()
player2 = Player()
print(player1.cards)
print(player2.cards)

# Receive a new card from the dealer
new_card = dealer.deal()
player1.receive_card(new_card)
new_card = dealer.deal()
player2.receive_card(new_card)
#print(player1.cards)
#print(player2.cards)

for c in player1.cards:
    print(Card.get_suit(c))
    print(Card.get_value(c))

for c in player2.cards:
    print(Card.get_suit(c))
    print(Card.get_value(c))

# Receive a new card from the dealer
new_card = dealer.deal()
player1.receive_card(new_card)
new_card = dealer.deal()
player2.receive_card(new_card)
#print(player1.cards)
#print(player2.cards)

for c in player1.cards:
    print(Card.get_suit(c))
    print(Card.get_value(c))

for c in player2.cards:
    print(Card.get_suit(c))
    print(Card.get_value(c))

