import unittest
import sys
sys.path.append("../freecell")
from card import *
from suit_cell import *


class SuitCellTest(unittest.TestCase):
    """Tests for the SuitCell class."""

    def test_validate_move_to_empty_cell_1(self):
        """Returns True when there is one selected Ace card and the suit cell is empty."""

        sc = SuitCell()
        self.assertTrue(sc.valid_move([Card(1, 1)]))

    def test_validate_move_to_empty_cell_2(self):
        """Returns False when there is one selected card but it is not an Ace, and the 
        suit cell is empty"""

        sc = SuitCell()
        self.assertFalse(sc.valid_move([Card(1, 10)]))

    def test_validate_move_to_occupied_cell_1(self):
        """Returns True when there is one selected card, the card in the cell is of the same suit, and the
        selected card has a value of 1 higher than the card in the cell."""

        sc = SuitCell()
        sc.add_card(Card(4, 1))
        self.assertTrue(sc.valid_move([Card(4, 2)]))

    def test_validate_move_to_occupied_cell_2(self):
        """Returns False when there is one selected card, the card in the cell is of the same suit, but the
        selected card does not have a value of 1 higher than the card in the cell."""

        sc = SuitCell()
        sc.add_card(Card(3, 1))
        self.assertFalse(sc.valid_move([Card(3, 3)]))

    def test_validate_move_to_occupied_cell_3(self):
        """Returns False when there is one selected card and that card has a value of 1 higher than the card
        in the cell, but it's suit does not match."""

        sc = SuitCell()
        sc.add_card(Card(2, 1))
        self.assertFalse(sc.valid_move([Card(1, 2)]))

    def test_validate_move_multiple_cards(self):
        """Returns False when there are multiple cards in the list passed as a parameter."""

        sc = SuitCell()
        self.assertFalse(sc.valid_move([Card(1, 1), Card(1, 2), Card(1, 3)]))


if __name__ == "__main__":
    unittest.main()
