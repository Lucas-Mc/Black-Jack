import unittest
from card import Card

class TestCard(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.card1 = Card('Heart',10)

  def test_suit(self):
    self.assertEqual(Card.get_suit(self.card1), 'Heart')

  def test_value(self):
    self.assertEqual(Card.get_value(self.card1), 10)

if __name__ == '__main__':
  unittest.main()