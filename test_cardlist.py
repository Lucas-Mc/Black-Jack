import unittest
from card import Card
from cardlist import CardList

class TestCardlist(unittest.TestCase):

  def test_add_card(self):
    cardlist1 = CardList(1)
    self.assertEqual(len(cardlist1.cards),1)
    card1 = Card('heart',10)
    cardlist1.add_card(card1)
    self.assertEqual(len(cardlist1.cards),2)

  def test_create_deck(self):
    # TODO: not sure how to do this one without using other functions
    cardlist1 = CardList(0)
    cardlist1.create_deck(10)
    self.assertEqual(len(cardlist1.cards),10)

  def test_pop_card(self):
    cardlist1 = CardList(1)
    self.assertEqual(len(cardlist1.cards),1)
    cardlist1.pop_card()
    self.assertEqual(len(cardlist1.cards),0)
    cardlist1.pop_card()
    self.assertEqual(len(cardlist1.cards),0)

  def test_print_cards(self):
    # TODO: not sure how to do this one 
    pass
  
  def test_shuffle(self):
    cardlist_temp = CardList(52)
    cardlist1 = [t for t in cardlist_temp.cards]
    cardlist_temp.shuffle()
    self.assertFalse(cardlist1 == cardlist_temp.cards)

  def test_value(self):
    cardlist1 = Card('heart',10)
    self.assertEqual(cardlist1.value,10)

  def test_number_of_cards(self):
    cardlist1 = CardList(2)
    self.assertEqual(len(cardlist1.cards),2)

if __name__ == '__main__':
  unittest.main()

