import unittest
from card import Card
from cardlist import CardList

class TestCardlist(unittest.TestCase):

  def test_add_card(self):
    # built up the baseline objects
    baseline_value = 10
    baseline_suit = 'heart'
    baseline_card = Card(baseline_suit, baseline_value)
    
    # create the test object
    test_cardlist = CardList(0)
    test_cardlist.add_card(baseline_card)

    # assertions - test that a card was added and that its the right card
    self.assertEqual(len(test_cardlist.cards), 1)
    self.assertEqual(test_cardlist.cards[0], baseline_card)

  def test_create_deck(self):
    # TODO: not sure how to do this one without using other functions
    cardlist1 = CardList(0)
    cardlist1.create_deck(10)
    self.assertEqual(len(cardlist1.cards),10)

  def test_pop_card(self):
    # built up the baseline objects
    baseline_value = 10
    baseline_suit = 'heart'
    baseline_card = Card(baseline_suit, baseline_value)
    baseline_card2 = Card(baseline_suit, baseline_value + 1)
    
    # create the test object
    # - the card list should look like this: [Card(heart, 10), Card(heart, 11)]
    test_cardlist = CardList(0)
    test_cardlist.add_card(baseline_card)
    test_cardlist.add_card(baseline_card2)

    # assertions
    popped_card = test_cardlist.pop_card()

    #  - test that a card was removed and returned
    self.assertTrue(type(popped_card), Card)
    self.assertEqual(test_cardlist.number_of_cards, 1)

    #  - test that the card return is the one on the top of the deck/last in the list
    self.assertEqual(popped_card, baseline_card2)

    #  - test that the case where no card are available is handled
    popped_card = test_cardlist.pop_card() 
    popped_card = test_cardlist.pop_card()
    self.assertTrue(type(popped_card), None)

  def test_print_cards(self):
    # TODO: build up a card list as demonstrated above and verify it doesnt crash
    # - make a list with 0 cards and run this function
    # - make a list with > 1 card and run it

    # Returning false so that it fails and we remember to fix this
    self.assertTrue(False)
  
  def test_shuffle(self):
    cardlist_temp = CardList(52)
    cardlist1 = [t for t in cardlist_temp.cards]
    cardlist_temp.shuffle()
    self.assertFalse(cardlist1 == cardlist_temp.cards)

  def test_value(self):
    # TODO: test the value if there are no cards

    # built up the baseline objects
    baseline_suit = 'heart'
    baseline_card = Card(baseline_suit, 10)
    baseline_card2 = Card(baseline_suit, 11)

    # create the test object
    # - the card list should look like this: [Card(heart, 10), Card(heart, 11)]
    test_cardlist = CardList(0)
    test_cardlist.add_card(baseline_card)
    test_cardlist.add_card(baseline_card2)
    
    # assertions
    #  - test that the value is 21
    self.assertEqual(test_cardlist.value, 21)

  def test_number_of_cards(self):
    # built up the baseline objects
    baseline_suit = 'heart'
    baseline_card = Card(baseline_suit, 10)
    baseline_card2 = Card(baseline_suit, 11)

    # create the test object
    # - the card list should look like this: [Card(heart, 10), Card(heart, 11)]
    test_cardlist = CardList(0)
    test_cardlist.add_card(baseline_card)
    test_cardlist.add_card(baseline_card2)
    
    # assertions
    #  - test that the number of cards is 2
    self.assertEqual(test_cardlist.number_of_cards, 2)


if __name__ == '__main__':
  unittest.main()

