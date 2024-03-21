from deck import Deck
from free_cell import FreeCell
from column_cell import ColumnCell
from suit_cell import SuitCell
from display import Display

class Game:
    """Represents a game of free cell solitaire. The Game checks for all game logic, such as
    if a card selection or placement is valid, as well as checking when the game is won. A Game
    has a deck and various card areas for cards to be placed."""

    def __init__(self):
        self._display = Display(self)
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

    def get_display(self):
        """Returns the display."""

        return self._display

    def get_card_areas(self):
        """Returns the card areas dictionary."""

        return self._card_areas
    
    def get_selected_cards(self):
        """Returns the selected cards list."""

        return self._selected_cards
    
    def set_selected_cards(self, cards=None):
        """Sets the selected cards list to the given list of Cards."""

        if not cards:
            self._selected_cards = []
        else:
            self._selected_cards = cards
    
    def get_previous_cards_area(self):
        """Returns the card area where the currently selected cards used to be located."""

        return self._previous_cards_area
    
    def set_previous_cards_area(self, card_area=None):
        """Sets the previous card's area to the given CardArea."""

        if not card_area:
            self._previous_cards_area = None
        else:
            self._previous_cards_area = card_area

    def init_card_areas(self):
        """Fills the card areas dictionary with 4 free cells, 4 suit cells, and 8 column cells."""

        # initialize 4 free cells and set their positions
        dummy = FreeCell()  # just using a cell-type object to get its width and height; this object is not used otherwise
        cell_width, cell_height = dummy.get_scaled_width(), dummy.get_scaled_height()
        x, y = 10, 10

        for id in range(1, 5):
            free_cell = FreeCell()
            free_cell.set_pos(x, y)
            self._card_areas["free-cells"][id] = free_cell
            x += (free_cell.get_scaled_width() + 10)

        # initialize 4 suit cells and set their positions
        x = self._display.get_width() - (cell_width + 10)

        for id in range(4, 0, -1):
            suit_cell = SuitCell()
            suit_cell.set_pos(x, y)
            self._card_areas["suit-cells"][id] = suit_cell
            x -= (cell_width + 10)

        # initialize 8 column cells and set their positions
        x = (self._display.get_width() - (240 + 8 * cell_width)) / 2
        y = 40 + cell_height

        for id in range(1, 9):
            column_cell = ColumnCell()
            column_cell.set_pos(x, y)
            self._card_areas["column-cells"][id] = column_cell
            x += (cell_width + 30)

    def fill_columns(self):
        """Distributes the 52 cards amongst the 8 columns and updates their coordinates."""

        # fill left 4 columns with 7 cards each and right 4 columns with 6 cards each
        for col_idx in range(1, 9):
            cards_amt = 7 if col_idx < 5 else 6
            column = self._card_areas["column-cells"][col_idx]
            x, y = column.get_pos()

            # add cards to column and update coordinates
            for i in range(cards_amt):
                card = self._deck.draw_card()
                column.add_card(card)
                card.set_pos(x, y)
                y += 40  # staggers out cards vertically

    def valid_selection(self, card, card_area):
        """Takes a card object and a card_area object as parameters. If selecting the card from the card area would be 
        a valid selection, returns True. Else returns False."""

        # A card is never allowed to be selected from a Suit Cell
        if isinstance(card_area, SuitCell): return False

        return card_area.valid_selection(card)
    
    def select_card(self, card, card_area):
        """Removes the card(s) from the card area, appends them to the game's selected cards list, and updates the previous
        cards location data attribute. If all is successful then returns True, else returns False."""
        
        # validate selection first
        if not self.valid_selection(card, card_area): return False
        
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

        return True

    def moves_count(self):
        """Returns the count of all empty free cells and column cells, plus one."""

        moves = 1
        free_cells = self.get_card_areas()["free-cells"]
        columns = self.get_card_areas()["column-cells"]

        for free_cell in free_cells.values():
            if free_cell.is_empty(): moves += 1

        for column in columns.values():
            if column.is_empty(): moves += 1

        return moves

    def valid_move(self, card_area):
        """Takes a list of cards and a destination card area. If placing the card(s) in the destination
        card area would result in a valid move, returns True, otherwise False. A free cell can only take
        one card while a column may take as many cards as there are moves available."""

        if self.moves_count() < len(self._selected_cards): return False  # cannot move more cards than there are available moves

        return card_area.valid_move(self._selected_cards)

    def move_selection_to_area(self, card_area):
        """Moves the selected cards to the destination card area."""

        card_area.place_cards(self._selected_cards)
        self.clear_selection()  # selection and previous area are cleared after card(s) are moved

    def move_selection_to_previous_area(self):
        """Moves all selected cards back to their previous area."""

        # check all free cells and columns (cards will never be moved back to a suit cell, since once they are
        # placed in a suit cell they are locked) to see if the previous area matches the current area
        areas_to_check = []

        for free_cell in self._card_areas["free-cells"].values():
            areas_to_check.append(free_cell)

        for column in self._card_areas["column-cells"].values():
            areas_to_check.append(column)

        for card_area in areas_to_check:
            if card_area == self._previous_cards_area:
                card_area.place_cards(self._selected_cards)
                break

        self.clear_selection()  # selection and previous area are cleared after card(s) are moved

    def clear_selection(self):
        """Resets the selected cards data attribute to an empty list and the previous cards area data attribute to None."""

        self.set_selected_cards()
        self.set_previous_cards_area()
    
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
        white_space_buffer = 20  # used to align all columns vertically

        while not finished_printing:
            finished_printing = True

            for column in columns.values():
                cards = column.get_cards()

                if idx >= len(cards):
                    print(" " * white_space_buffer, end="")
                else:
                    if finished_printing == True: finished_printing = False  # while loop keeps going if at least one card is printed this iteration

                    card_str_length = cards[idx].get_string_length()
                    print(cards[idx], end=" "*(white_space_buffer - card_str_length))

            print()
            idx += 1

# ---------------------------------------------------------------------------------------------------------
# METHODS FOR PLAYING IN TERMINAL: These are not used in the Pygame implementation, just for 
# playing/debugging in the console.
# ---------------------------------------------------------------------------------------------------------

    def select_from_column_with_validation(self, column_id, card_idx):
        """Takes in a column_id integer (1-8) and card_idx integer. Selects the card at the given index from the 
        column with the given id. If the selection is valid, selects the card and returns True. If the selection
        is invalid, no selection is made and returns False."""

        # verify that there is not already any selected cards
        if self.get_selected_cards(): return False

        # verify that column id is in range [1, 8]
        if column_id not in range(1, 9): return False

        column = self.get_card_areas()["column-cells"][column_id]

        # verify that the card index is a valid index for the given column
        if card_idx not in range(column.cards_count()): return False

        card = column.get_cards()[card_idx]

        if self.valid_selection(card, column):
            self.select_card(card, column)
            return True
        
        return False

    def select_from_free_cell_with_validation(self, free_cell_id):
        """Takes in a free_cell_id integer (1-4). Selects the card from the free cell with the given id (if the cell
         has a card.) If the selection is valid, selects the card and returns True. If the selection is invalid,
         no selection is made and returns False."""
        
        # verify that there are not already any selected cards
        if self.get_selected_cards(): return False

        # verify that free cell id is in range [1, 4]
        if free_cell_id not in range(1, 5): return False

        free_cell = self.get_card_areas()["free-cells"][free_cell_id]

        # verify that the free cell is not empty
        if free_cell.is_empty(): return False

        card = free_cell.get_cards()[0]

        if self.valid_selection(card, free_cell):
            self.select_card(card, free_cell)
            return True
        
        return False

    def move_cards_with_validation(self, area_type, area_id):
        """Takes in an area_type string, which should be 'free-cell', 'suit-cell', or 'column-cell', and an
         area_id integer [(1-8) for columns, (1-4) for free/suit cells]. If the movement is valid, moves the
         current selection to the card area with the given area_id and returns True. If the movement is invalid
         selected cards are moved back to previous card area and returns False."""
        
        # if there are no selected cards, exit early
        if not self._selected_cards: return False

        # area id must be in range [1, 8]
        if area_id not in range(1, 9): return False
        
        # verify that area_type string is valid
        valid_strings = ["free-cell", "suit-cell", "column-cell"]
        if area_type not in valid_strings: return False
        
        # verify that area_id is in range for the area_type
        if (area_type == "free-cell" or area_type == "suit-cell") and \
            area_id not in range(1, 5):
            return False
        elif area_type == "column-cell" and area_id not in range(1, 9):
            return False

        # pluralize the string so it can be used as a key for card areas dictionary
        area_type += "s"

        card_area = self.get_card_areas()[area_type][area_id]
        
        if self.valid_move(card_area):
            self.move_selection_to_area(card_area)
            return True
        else:
            self.move_selection_to_previous_area()
            return False
