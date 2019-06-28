import unittest
from dealer import Dealer

class TestDealer(unittest.TestCase):

  def test_deal(self):
    dealer = Dealer()
    self.assertEqual(len(dealer.cards),52)
    dealer.deal()
    self.assertEqual(len(dealer.cards),51)

if __name__ == '__main__':
  unittest.main()