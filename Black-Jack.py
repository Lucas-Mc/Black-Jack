from dealer import Dealer
from player import Player
import sys

# Available game types: battle, blackjack
game_type = "blackjack"

# Initialize a dealer object
dealer = Dealer()

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
print("\n")

# Receive a new card from the dealer
new_card = dealer.deal()
player1.receive_card(new_card)
new_card = dealer.deal()
player2.receive_card(new_card)

# Show their hands after two cards each
print("Second Deal:")
print("Player 1:")
player1.print_cards()
player1_total = player1.add_cards()
print("Player 1 Total = {}".format(player1_total))
print("Player 2:")
player2.print_cards()
player2_total = player2.add_cards()
print("Player 2 Total = {}".format(player2_total))
print("\n")

if (game_type == "battle"):

    player1_wins = 0
    player2_wins = 0
    if (player1_total > player2_total):
        player1_wins += 1
    elif (player2_total > player1_total):
        player2_wins += 1
    else: 
        pass
    print("Player 1 wins: {}".format(player1_wins))
    print("Player 2 wins: {}".format(player2_wins))

elif (game_type == "blackjack"):

    if (player1_total > 21):

        print("Player 2 wins!")
        sys.exit()

    elif (player2_total > 21):

        print("Player 1 wins!")
        sys.exit()

    else:

        print("Player 1:")
        player1_decision = player1.make_decision()
        
        if (player1_decision == "s"):

            print("Player 1:")
            player1.print_cards()
            player1_total = player1.add_cards()
            print("Player 1 Total = {}".format(player1_total))

        elif (player1_decision == "h"):

            while (player1_decision == "h"):

                new_card = dealer.deal()
                player1.receive_card(new_card)
                print("Player 1:")
                player1.print_cards()
                player1_total = player1.add_cards()
                print("Player 1 Total = {}".format(player1_total))

                if (player1_total > 21):
                    print("Player 2 wins!")
                    sys.exit()
                else:
                    player1_decision = player1.make_decision()  

        print("Player 2:")
        player2_decision = player2.make_decision()

        if (player2_decision == "s"):

            print("Player 2:")
            player2.print_cards()
            player2_total = player2.add_cards()
            print("Player 2 Total = {}".format(player2_total))

        elif (player2_decision == "h"):

            while (player2_decision == "h"):

                new_card = dealer.deal()
                player2.receive_card(new_card)
                print("Player 2:")
                player2.print_cards()
                player2_total = player2.add_cards()
                print("Player 2 Total = {}".format(player2_total))
                            
                if (player2_total > 21):
                    print("Player 1 wins!")
                    sys.exit()
                else:
                    player2_decision = player2.make_decision()

