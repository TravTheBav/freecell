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
        self.init_card_areas()   # initialize the 16 card areas and fill columns with cards
        self.fill_columns()

        # selected cards stored here and their previous location is saved when they are being moved
        self._selected_cards = []
        self._previous_cards_area = None

    def get_card_areas(self):
        """Returns the card areas dictionary."""

        return self._card_areas
    
    def get_selected_cards(self):
        """Returns the selected cards list."""

        return self._selected_cards
    
    def get_previous_cards_area(self):
        """Returns the card area where the currently selected cards used to be located."""

        return self._previous_cards_area

    def init_card_areas(self):
        """Fills the card areas dictionary with 4 free cells, 4 suit cells, and 8 column cells."""

        # initialize 4 free cells and 4 suit cells
        for id in range(1, 5):
            self._card_areas["free-cells"][id] = FreeCell()
            self._card_areas["suit-cells"][id] = SuitCell()

        # initialize 8 column cells
        for id in range(1, 9):
            self._card_areas["column-cells"][id] = ColumnCell()

    def fill_columns(self):
        """Distributes the 52 cards amongst the 8 columns."""

        # fill left 4 columns with 7 cards each and right 4 columns with 6 cards each
        for col_idx in range(1, 9):
            cards_amt = 7 if col_idx < 5 else 6 

            for i in range(cards_amt):
                column = self._card_areas["column-cells"][col_idx]
                card = self._deck.draw_card()
                column.add_card(card)

    def valid_selection(self, card, card_area):
        """Takes a card object and a card_area object as parameters. If selecting the card from the card area would be 
        a valid selection, returns True. Else returns False."""

        # A card is never allowed to be selected from a Suit Cell
        if isinstance(card_area, SuitCell): return False

        return card_area.valid_selection(card)
    
    def select_card(self, card, card_area):
        """Removes the card(s) from the card area, appends them to the game's selected cards list, and updates the previous
        cards location data attribute. Selections do not need to be validated since the valid_selection method will be called first."""
        
        # from bottom to top, continuosly remove cards from the card area until the selected card is reached, then remove that card as well
        # all removed cards are add to selected cards
        cards = card_area.get_cards()
        idx = len(cards) - 1

        while idx >= 0:
            removed_card = cards.pop()
            self._selected_cards.append(removed_card)

            if removed_card == card: break

            idx -= 1

        # selected cards must be reversed since cards were added from the 'bottom-up'
        self._selected_cards.reverse()
        # set card's previous area data attribute to the passed in card area
        self._previous_cards_area = card_area
    
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
                    print(" " * 22, end="")
                else:
                    if finished_printing == True: finished_printing = False  # while loop keeps going if at least one card is printed this iteration

                    card_str_length = cards[idx].get_string_length()
                    print(cards[idx], end=" "*(white_space_buffer - card_str_length))

            print()
            idx += 1
