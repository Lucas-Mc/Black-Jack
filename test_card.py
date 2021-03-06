import unittest
from card import Card

class TestCard(unittest.TestCase):

  _suit = 'heart'
  _value = 10

  @classmethod
  def setUpClass(cls):
    cls.card1 = Card(TestCard._suit,TestCard._value)

  def test_suit(self):
    self.assertEqual(Card.get_suit(self.card1), TestCard._suit)

  def test_value(self):
    self.assertEqual(Card.get_value(self.card1), TestCard._value)

  def test__str__(self):
    t_string = str(TestCard._value) + ' of ' + TestCard._suit
    self.assertEqual(str(self.card1), t_string)


if __name__ == '__main__':
  unittest.main()