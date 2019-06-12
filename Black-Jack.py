from dealer import Dealer
from player import Player
from deck import Deck
from card import Card

# Initialize a dealer object
dealer = Dealer()
# Initialize a deck object
deck = Deck()

# Initialize two players for the game
player1 = Player()
player2 = Player()

# Receive a new card from the dealer
new_card = dealer.deal()
player1.receive_card(new_card)
new_card = dealer.deal()
player2.receive_card(new_card)

# Show their hands after one card each
print("\n")
print("First Deal:")
print("Player 1:")
player1.print_cards()
print("Player 2:")
player2.print_cards()

# Receive a new card from the dealer
new_card = dealer.deal()
player1.receive_card(new_card)
new_card = dealer.deal()
player2.receive_card(new_card)
print("\n")

# Show their hands after two cards each
print("Second Deal:")
print("Player 1:")
player1.print_cards()
print("Player 2:")
player2.print_cards()
print("\n")
