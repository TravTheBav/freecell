import unittest
import sys
sys.path.append("../freecell")
from card import *
from free_cell import *


class FreeCellTest(unittest.TestCase):
    """Tests for the FreeCell class."""

    def test_valid_select_free_cell(self):
        """Returns True when the card that is passed is the card in the free cell."""

        fc = FreeCell()
        ace_spades = Card(2, 1)
        fc.add_card(ace_spades)

        self.assertTrue(fc.valid_selection(ace_spades))

    def test_invalid_selection_free_cell_1(self):
        """Returns False if the free cell is empty."""

        fc = FreeCell()
        ace_spades = Card(2, 1)

        self.assertFalse(fc.valid_selection(ace_spades))

    def test_invalid_selection_free_cell_2(self):
        """Returns False if the card that is passed does not match the card in the free cell."""

        fc = FreeCell()
        ace_spades = Card(2, 1)
        two_clubs = Card(1, 2)
        fc.add_card(ace_spades)

        self.assertFalse(fc.valid_selection(two_clubs))

    def test_validate_move_to_empty_free_cell_1(self):
        """Returns True when there is one selected card and the free cell is empty."""

        fc = FreeCell()
        selected_cards = [Card(1, 1)]

        self.assertTrue(fc.valid_move(selected_cards))

    def test_validate_move_to_empty_free_cell_2(self):
        """Returns False when there are 2 selected cards and the free cell is empty."""

        fc = FreeCell()
        selected_cards = [Card(1, 2), Card(3, 1)]
        
        self.assertFalse(fc.valid_move(selected_cards))

    def test_validate_move_to_full_free_cell(self):
        """Returns False when the free cell is occupied."""

        fc = FreeCell()
        fc.add_card(Card(2, 1))
        selected_cards = [Card(1, 1)]

        self.assertFalse(fc.valid_move(selected_cards))
    

if __name__ == "__main__":
    unittest.main()