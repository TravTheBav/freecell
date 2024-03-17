import unittest
import sys
sys.path.append("../freecell")
from card import *
from column_cell import *


class ColumnCellTests(unittest.TestCase):
    """Tests for the ColumnCell class."""

    def test_valid_selection_column_1(self):
        """Returns True when the selected card is the only card in the column."""

        cc = ColumnCell()
        ace_spades = Card(2, 1)
        cc.add_card(ace_spades)
        result = cc.valid_selection(ace_spades)

        self.assertTrue(result)

    def test_valid_selection_column_2(self):
        """Returns True when the selected card is the last card in the column."""

        cc = ColumnCell()
        ace_spades = Card(2, 1)
        two_clubs = Card(1, 2)
        cc.add_card(ace_spades)
        cc.add_card(two_clubs)
        result = cc.valid_selection(two_clubs)

        self.assertTrue(result)

    def test_valid_selection_column_3(self):
        """Returns True when all cards below the selected card decrement sequentially and alternate color."""

        cc = ColumnCell()
        king_hearts = Card(4, 13)
        cards = [king_hearts, Card(2, 12), Card(3, 11), Card(1, 10), Card(4, 9)]
        for card in cards:
            cc.add_card(card)

        result = cc.valid_selection(king_hearts)

        self.assertTrue(result)

    def test_invalid_selection_column_1(self):
        """Returns False when the passed in card is not in the column."""
        
        cc = ColumnCell()
        king_hearts = Card(4, 13)
        queen_spades = Card(2, 12)
        cc.add_card(king_hearts)
        result = cc.valid_selection(queen_spades)

        self.assertFalse(result)

    def test_invalid_selection_column_2(self):
        """Returns False when the column is empty."""

        cc = ColumnCell()
        king_hearts = Card(4, 13)
        result = cc.valid_selection(king_hearts)

        self.assertFalse(result)

    def test_invalid_selection_column_3(self):
        """Returns False when all cards below selected card decrement by 1 but the last card breaks the alternating color pattern."""

        cc = ColumnCell()
        king_hearts = Card(4, 13)
        cards = [Card(1, 2), Card(4, 4), king_hearts, Card(2, 12), Card(3, 11), Card(3, 10)]
        for card in cards:
            cc.add_card(card)

        result = cc.valid_selection(king_hearts)

        self.assertFalse(result)

    def test_invalid_selection_column_4(self):
        """Returns False when all cards below the selected card decrement by 1 and alternate color EXCEPT for the last card, which
        decrements by 2 instead."""

        cc = ColumnCell()
        king_hearts = Card(4, 13)
        cards = [Card(1, 2), Card(4, 4), king_hearts, Card(2, 12), Card(3, 11), Card(1, 9)]
        for card in cards:
            cc.add_card(card)

        result = cc.valid_selection(king_hearts)

        self.assertFalse(result)

    def test_validate_move_to_empty_column_1(self):
        """Returns True when there is one card and the column is empty."""

        pass

    def test_validate_move_to_empty_column_2(self):
        """Returns True when there are multiple cards and the column is empty."""

        pass

    def test_validate_move_to_occupied_column_1(self):
        """Returns True when there are multiple cards and:
           1.) the last card in the column is one value higher than the first card in the selected
           cards list
           2.) the last card in the column has a different color than the first card in the selected
           cards list"""
        
        pass

    def test_validate_move_to_occupied_column_2(self):
        """Returns False when there are multiple cards and the last card in the column has the same 
        color as the first card in the selected cards list."""

        pass

    def test_validate_move_to_occupied_column_3(self):
        """Returns False when there are multiple cards and the last card in the column does not have
        exactly one value higher than the first card in the selected cards list."""

        pass


if __name__ == "__main__":
    unittest.main()
    