import unittest
import sys
sys.path.append("../freecell")
from game import *
from card import Card


class GameTest(unittest.TestCase):
    """Tests for the Game class."""

    def test_fill_columns(self):
        """Fills the left 4 columns with 7 cards each and the right 4 columns with 6 cards each."""

        g = Game()
        columns = g.get_card_areas()["column-cells"]

        for idx in range(1, 9):
            cards = columns[idx].get_cards()

            if idx < 5:
                self.assertEqual(7, len(cards))
            else:
                self.assertEqual(6, len(cards))

    def test_select_bottom_card_in_column(self):
        """Selects one card from the bottom of a column."""

        g = Game()
        column = g.get_card_areas()["column-cells"][1]
        card = column.get_cards()[-1]  # last card in the first column
        g.select_card(card, column)

        self.assertEqual(6, column.cards_count())  # card is removed
        self.assertEqual(card, g.get_selected_cards()[0])  # card is added to selected cards
        self.assertEqual(column, g.get_previous_cards_area())  # previous cards area contains the card area passed as an argument

    def test_select_card_from_free_cell(self):
        """Selects the only card from a free cell."""

        g = Game()
        free_cell = g.get_card_areas()["free-cells"][1]
        card = Card(1, 1)
        free_cell.add_card(card)
        g.select_card(card, free_cell)

        self.assertEqual(0, free_cell.cards_count())  # card is removed
        self.assertEqual(card, g.get_selected_cards()[0])  # card is added to selected cards
        self.assertEqual(free_cell, g.get_previous_cards_area())  # previous cards area contains the card area passed as an argument

    def test_select_all_cards(self):
        """Selects all cards from a column when they are all stacked in descending order with alternating colors."""

        g = Game()
        column = g.get_card_areas()["column-cells"][1]
        cards = [Card(1, 5), Card(3, 4), Card(1, 3), Card(3, 2), Card(1, 1)]
        copy = cards.copy()
        column.set_cards(cards)
        card = column.get_cards()[0]
        g.select_card(card, column)

        self.assertEqual(0, column.cards_count())  # all cards are removed
        self.assertEqual(copy, g.get_selected_cards())  # selected cards matches the entire list of cards that was removed
        self.assertEqual(column, g.get_previous_cards_area())  # previous cards area contains the card area passed as an argument

    def test_select_multiple_cards(self):
        """Selects 3 cards from the bottom of a column with 6 cards."""

        pass

if __name__ == "__main__":
    unittest.main()
