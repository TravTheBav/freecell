from deck import Deck
from free_cell import FreeCell
from column_cell import ColumnCell
from suit_cell import SuitCell


class Game:
    """Represents a game of free cell solitaire. The Game checks for all game logic, such as
    if a card selection or placement is valid, as well as checking when the game is won. A Game
    has a deck and various card areas for cards to be placed."""

    def __init__(self):
        self._deck = Deck()      # create a new deck and shuffle it
        self._deck.shuffle()
        self._card_areas = {     # format example: card_areas["free-cells"][1] would return the first FreeCell object
            "free-cells": {},
            "column-cells": {},
            "suit-cells": {}
        }
        self.init_card_areas()   # initialize the 16 card areas

    def get_card_areas(self):
        """Returns the card areas dictionary."""

        return self._card_areas

    def init_card_areas(self):
        """Fills the card areas dictionary with 4 free cells, 4 suit cells, and 8 column cells."""

        # initialize 4 free cells and 4 suit cells
        for id in range(1, 5):
            self._card_areas["free-cells"][id] = FreeCell()
            self._card_areas["suit-cells"][id] = SuitCell()

        # initialize 8 column cells
        for id in range(1, 9):
            self._card_areas["column-cells"][id] = ColumnCell()

    def print_table(self):
        """Prints out the cards to the console in a readable format."""

        # prints free cells at top left
        free_cells = self._card_areas["free-cells"]
        for free_cell in free_cells.values():
            print(free_cell, end=" ")

        print (" " * 8, end=" ")

        # prints suit cells at top right
        suit_cells = self._card_areas["suit-cells"]
        for suit_cell in suit_cells.values():
            print(suit_cell, end=" ")

        print("\n" * 4)

        # prints each column from left to right; top of each column is card at index 0
        columns = self._card_areas["column-cells"]
        finished_printing = False
        idx = 0
        white_space_buffer = 22  # used to align all columns vertically

        while not finished_printing:
            finished_printing = True

            for column in columns.values():
                cards = column.get_cards()

                if idx >= len(cards):
                    continue
                else:
                    if finished_printing == True: finished_printing = False  # while loop keeps going if at least one card is printed this iteration

                    card_str_length = len(cards[idx].__repr__())
                    print(cards[idx], end=" "*(white_space_buffer - card_str_length))

            print()
            idx += 1

    def fill_columns(self):
        """Distributes the 52 cards amongst the 8 columns."""

        # fill left 4 columns with 7 cards each and right 4 columns with 6 cards each
        for col_idx in range(1, 9):
            cards_amt = 7 if col_idx < 5 else 6 

            for i in range(cards_amt):
                column = self._card_areas["column-cells"][col_idx]
                card = self._deck.draw_card()
                column.add_card(card)

    def valid_selection(card, card_area):
        """Takes a card object and a card_area object as parameters. If selecting the card from the card area would be 
        a valid selection, returns True. Else returns False."""

        # A card is never allowed to be selected from a Suit Cell
        if isinstance(card_area, SuitCell): return False

        return card_area.valid_selection(card)
