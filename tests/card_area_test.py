import unittest
import sys
sys.path.append("../freecell")
from card import *
from card_area import *


class CardAreaTest(unittest.TestCase):
    """Tests for the CardArea class."""

    def test_place_cards_single_card_1(self):
        """Places one card to an empty area."""

        ca = CardArea()
        cards = [Card(1, 11)]  # [Jack of Clubs]
        ca.place_cards(cards)
        
        self.assertEqual(cards, ca.get_cards())

    def test_place_cards_single_card_2(self):
        """Places one card to an occupied area."""

        ca = CardArea()
        ca.add_card(Card(1, 11))  # [Jack of Clubs]
        cards = [Card(3, 10)]  # [10 of Diamonds]
        expected = ca.get_cards() + cards  # expected to be [Jack of Clubs, 10 of Diamonds]

        ca.place_cards(cards)        
        self.assertEqual(expected, ca.get_cards())

    def test_place_cards_empty_area(self):
        """Cards are placed in correct order when the card area is empty."""

        ca = CardArea()
        cards = [Card(1, 3), Card(3, 2), Card(2, 1)]  # [3 of Clubs, 2 of Diamonds, Ace of Spades]
        ca.place_cards(cards)

        self.assertEqual(cards, ca.get_cards())

    def test_place_cards_occupied_area(self):
        """Cards are placed in correct order when the card area is occupied."""

        ca = CardArea()
        ca.add_card(Card(2, 3))
        ca.add_card(Card(1, 2))
        ca.add_card(Card(3, 5))
        ca.add_card(Card(1, 13))  # cards in area == [3 of Spades, 2 of Clubs, 5 of Diamonds, King of Clubs]
        cards = [Card(4, 12), Card(2, 11)]  # [Queen of Hearts, Jack of Spades]
        # expected to be [3 of Spades, 2 of Clubs, 5 of Diamonds, King of Clubs, Queen of Hearts, Jack of Spades]
        expected = ca.get_cards() + cards 

        ca.place_cards(cards)        
        self.assertEqual(expected, ca.get_cards())


if __name__ == "__main__":
    unittest.main()
