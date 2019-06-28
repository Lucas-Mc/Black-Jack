import unittest
from player import Player
from card import Card

class TestPlayer(unittest.TestCase):

  _suit1 = 'heart'
  _value1 = 10
  _suit2 = 'club'
  _value2 = 5

  def test_receive_card(self):
    player1 = Player()
    self.assertEqual(len(player1.cards),0)
    card1 = Card(TestPlayer._suit1,TestPlayer._value1)
    player1.receive_card(card1)
    self.assertEqual(len(player1.cards),1)
    card2 = Card(TestPlayer._suit2,TestPlayer._value2)
    player1.receive_card(card2)
    self.assertEqual(len(player1.cards),2)

  def test_make_decision(self):
    # TODO: not sure how to do this one
    # self.assertEqual(len(dealer.cards),51)
    pass

  def test_flush_cards(self):
    # TODO: make better? this one involves a lot of outside function calls
    player1 = Player()
    card1 = Card(TestPlayer._suit1,TestPlayer._value1)
    card2 = Card(TestPlayer._suit2,TestPlayer._value2)
    player1.receive_card(card1)
    player1.receive_card(card2)
    self.assertEqual(len(player1.cards),2)
    player1.flush_cards()
    self.assertEqual(len(player1.cards),0)

if __name__ == '__main__':
  unittest.main()