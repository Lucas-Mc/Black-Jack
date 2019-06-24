from dealer import Dealer
from player import Player
import sys

def print_state(deal_num):
  '''
  deal_num: the current deal cycle
  '''
  print('Deal '+str(deal_num)+':')
  print('Player 1:')
  player1.print_cards()
  player1_total = player1.value
  print('Player 1 Total = {}'.format(player1_total))
  print('Player 2:')
  player2.print_cards()
  player2_total = player2.value
  print('Player 2 Total = {}'.format(player2_total))
  print('\n')

  return player1_total,player2_total

# Available game types: battle, blackjack
print('Which game do you want to play?')

game_type = ''

while ((game_type != 'battle') and (game_type != 'blackjack')):
  
  game_type = input("Type 'battle' or 'blackjack': ")


# Initialize a dealer object
dealer = Dealer()
deal_num = 0

# Initialize two players for the game
player1 = Player()
player2 = Player()


if game_type == 'battle':
  # Receive a new card from the dealer
  player1.receive_card(dealer.deal())
  player2.receive_card(dealer.deal())
  deal_num += 1

  # Show their hands after one card each
  player1_total, player2_total = print_state(deal_num)

  # Receive a new card from the dealer
  new_card = dealer.deal()
  player1.receive_card(new_card)
  new_card = dealer.deal()
  player2.receive_card(new_card)
  deal_num += 1

  # Show their hands after two cards each
  player1_total, player2_total = print_state(deal_num)

  player1_wins = 0
  player2_wins = 0
  print(player1.value)
  print(player2.value)
  cards_left = 0  # dealer.deck.count_cards()

  while (cards_left > 0):

    if (player1_total > player2_total):
      player1_wins += 1
    elif (player2_total > player1_total):
      player2_wins += 1
    else:
      pass

    print('Player 1 wins: {}'.format(player1_wins))
    print('Player 2 wins: {}'.format(player2_wins))

    # Receive a new card from the dealer
    player1.pop_card()
    new_card = dealer.deal()
    player1.receive_card(new_card)
    player2.pop_card()
    new_card = dealer.deal()
    player2.receive_card(new_card)
    deal_num += 1

    player1_total, player2_total = print_state(deal_num)

    # Re-count the number of cards left
    cards_left = dealer.deck.value


if game_type == 'blackjack':

  # Receive a new card from the dealer
  player1.receive_card(dealer.deal())
  player2.receive_card(dealer.deal())
  deal_num += 1

  # Show their hands after one card each
  player1_total, player2_total = print_state(deal_num)

  # Receive a new card from the dealer
  new_card = dealer.deal()
  player1.receive_card(new_card)
  new_card = dealer.deal()
  player2.receive_card(new_card)
  deal_num += 1

  # Show their hands after two cards each
  player1_total, player2_total = print_state(deal_num)

  if (player1_total > 21):

    print('Player 2 wins!')
    sys.exit()

  elif (player2_total > 21):

    print('Player 1 wins!')
    sys.exit()

  else:

    print('Player 1:')
    player1_decision = player1.make_decision()
      
    if (player1_decision == 's'):

      print('Player 1:')
      player1.print_cards()
      player1_total = player1.value
      print('Player 1 Total = {}'.format(player1_total))

    elif (player1_decision == 'h'):

      while (player1_decision == 'h'):

        new_card = dealer.deal()
        player1.receive_card(new_card)
        print('Player 1:')
        player1.print_cards()
        player1_total = player1.value
        print('Player 1 Total = {}'.format(player1_total))

        if (player1_total > 21):
          print('Player 2 wins!')
          sys.exit()
        else:
          player1_decision = player1.make_decision()  

    print('Player 2:')
    player2_decision = player2.make_decision()

    if (player2_decision == 's'):

      print('Player 2:')
      player2.print_cards()
      player2_total = player2.value
      print('Player 2 Total = {}'.format(player2_total))

      print('\n')
      if (player1_total > player2_total):
        print('Player 1 wins!')
        sys.exit()
      else:
        print('Player 2 wins!')
        sys.exit()

    elif (player2_decision == 'h'):

      while (player2_decision == 'h'):

        new_card = dealer.deal()
        player2.receive_card(new_card)
        print('Player 2:')
        player2.print_cards()
        player2_total = player2.value
        print('Player 2 Total = {}'.format(player2_total))
                    
        if (player2_total > 21):
          print('Player 1 wins!')
          sys.exit()
        else:
          player2_decision = player2.make_decision()

