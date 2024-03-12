from deck import Deck
from free_cell import FreeCell
from column_cell import ColumnCell
from suit_cell import SuitCell


class Game:
    """Represents a game of free cell solitaire. The Game checks for all game logic, such as
    if a card selection or placement is valid, as well as checking when the game is won. A Game
    has a deck and various card areas for cards to be placed."""

    def __init__(self):
        self._deck = Deck()
        self._card_areas = {     # format example: card_areas["free-cells"][1] would return the first FreeCell object
            "free-cells": {},
            "column-cells": {},
            "suit-cells": {}
        }
        self.init_card_areas()   # fill in the 16 card areas

    def init_card_areas(self):
        """Fills the card areas dictionary with 4 free cells, 4 suit cells, and 8 column cells."""

        # initialize 4 free cells and 4 suit cells
        for id in range(1, 5):
            self._card_areas["free-cells"][id] = FreeCell()
            self._card_areas["suit-cells"][id] = SuitCell()

        # initialize 8 column cells
        for id in range(1, 9):
            self._card_areas["column-cells"][id] = ColumnCell()