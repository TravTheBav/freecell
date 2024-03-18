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

        g = Game()
        column = g.get_card_areas()["column-cells"][1]
        cards = [Card(1, 10), Card(2, 13), Card(4, 9), Card(2, 7), Card(3, 6), Card(1, 5)]
        copy = cards.copy()
        expected = copy[3:]
        column.set_cards(cards)
        card = column.get_cards()[3]
        g.select_card(card, column)

        self.assertEqual(3, column.cards_count())  # 3 remaining cards in the column
        self.assertEqual(expected, g.get_selected_cards())  # selected cards matches the last 3 cards of the copied list
        self.assertEqual(column, g.get_previous_cards_area())  # previous cards area contains the card area passed as an argument

    def test_moves_count_new_game(self):
        """Returns 5 at the start of the game (4 free cells + 1)."""

        g = Game()
        self.assertEqual(5, g.moves_count())

    def test_moves_count_all_cells_full(self):
        """Returns 1 when all free cells and columns contain cards."""

        g = Game()
        column = g.get_card_areas()["column-cells"][1]
        cards = column.get_cards()
        for cell_id in range(1, 5):  # distribute last 4 cards in first column among the free cells
            card = cards.pop()
            free_cell = g.get_card_areas()["free-cells"][cell_id]
            free_cell.add_card(card)

        self.assertEqual(1, g.moves_count())

    def test_moves_count_two_empty_columns(self):
        """Returns 7 when there are 4 empty free cells and 2 empty columns."""

        g = Game()
        columns = g.get_card_areas()["column-cells"]
        columns[1].set_cards([])
        columns[2].set_cards([])

        self.assertEqual(7, g.moves_count())

    def test_move_selection_to_previous_free_cell(self):
        """Moves a card to the previous area, which is an empty free cell."""

        g = Game()
        free_cell = g.get_card_areas()["free-cells"][1]
        cards = [Card(3, 2)]
        g.set_selected_cards(cards)
        g.set_previous_cards_area(free_cell)
        g.move_selection_to_previous_area()
        
        # selection and previous area are cleared upon card movement
        self.assertEqual([], g.get_selected_cards())
        self.assertEqual(None, g.get_previous_cards_area())

        # card has been moved
        self.assertEqual(cards, free_cell.get_cards())

    def test_move_selection_to_previous_column_1(self):
        """Moves a single card to the previous area, which is an empty column."""

        g = Game()
        column_cell = g.get_card_areas()["column-cells"][1]
        column_cell.set_cards()  # empty column
        cards = [Card(2, 4)]
        g.set_selected_cards(cards)
        g.set_previous_cards_area(column_cell)
        g.move_selection_to_previous_area()

        # selection and previous area are cleared upon card movement
        self.assertEqual([], g.get_selected_cards())
        self.assertEqual(None, g.get_previous_cards_area())

        # card has been moved
        self.assertEqual(cards, column_cell.get_cards())

    def test_move_selection_to_previous_column_2(self):
        """Moves a single card to the previous area, which is an occupied column."""

        g = Game()
        column_cell = g.get_card_areas()["column-cells"][1]
        column_cell.set_cards()  # empty column
        column_cell.add_card(Card(1, 1))  # add one card to column
        cards = [Card(2, 4)]
        expected = column_cell.get_cards() + cards
        g.set_selected_cards(cards)
        g.set_previous_cards_area(column_cell)
        g.move_selection_to_previous_area()

        # selection and previous area are cleared upon card movement
        self.assertEqual([], g.get_selected_cards())
        self.assertEqual(None, g.get_previous_cards_area())

        # card has been moved
        self.assertEqual(expected, column_cell.get_cards())

    def test_move_selection_to_previous_column_3(self):
        """Moves multiple cards to the previous area, which is an empty column."""

        g = Game()
        column_cell = g.get_card_areas()["column-cells"][1]
        column_cell.set_cards()
        cards = [Card(2, 4), Card(3, 3), Card(1, 2), Card(4, 1)]
        g.set_selected_cards(cards)
        g.set_previous_cards_area(column_cell)
        g.move_selection_to_previous_area()

        # selection and previous area are cleared upon card movement
        self.assertEqual([], g.get_selected_cards())
        self.assertEqual(None, g.get_previous_cards_area())

        # cards have been moved
        self.assertEqual(cards, column_cell.get_cards())

    def test_move_selection_to_previous_column_4(self):
        """Moves multiple cards to the previous area, which is an occupied column."""

        g = Game()
        column_cell = g.get_card_areas()["column-cells"][1]
        column_cell.set_cards()
        column_cell.add_card(Card(2, 6))
        column_cell.add_card(Card(2, 12))
        column_cell.add_card(Card(1, 10))  # cards in column == [6 of Spades, Queen of Spades, 10 of Clubs]
        cards = [Card(2, 7), (3, 6), (2, 5)]  # selection == [7 of Spades, 6 of Diamonds, 5 of Spades]
        expected = column_cell.get_cards() + cards
        g.set_selected_cards(cards)
        g.set_previous_cards_area(column_cell)
        g.move_selection_to_previous_area()

        # selection and previous area are cleared upon card movement
        self.assertEqual([], g.get_selected_cards())
        self.assertEqual(None, g.get_previous_cards_area())

        # cards have been moved
        self.assertEqual(expected, column_cell.get_cards())
        

if __name__ == "__main__":
    unittest.main()
