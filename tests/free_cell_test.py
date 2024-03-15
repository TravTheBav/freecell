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
        result = fc.valid_selection(ace_spades)

        self.assertTrue(result)

    def test_invalid_selection_free_cell_1(self):
        """Returns False if the free cell is empty."""

        fc = FreeCell()
        ace_spades = Card(2, 1)
        result = fc.valid_selection(ace_spades)

        self.assertFalse(result)

    def test_invalid_selection_free_cell_2(self):
        """Returns False if the card that is passed does not match the card in the free cell."""

        fc = FreeCell()
        ace_spades = Card(2, 1)
        two_clubs = Card(1, 2)
        fc.add_card(ace_spades)
        result = fc.valid_selection(two_clubs)

        self.assertFalse(result)
    

if __name__ == "__main__":
    unittest.main()