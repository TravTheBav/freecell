import pygame as pg
from suit_cell import SuitCell


class Display:
    """A class for linking up the display to the Game logic. Handles mouse movements
     and button clicks by the player."""
        
    def __init__(self, game):
        
        self._game = game
        self._surface = pg.display.set_mode((1280, 720))
        pg.display.set_caption("Free Cell")

        # for card dragging
        self._mouse_drag_x_offset = None
        self._mouse_drag_y_offset = None

    def get_width(self):
        """Returns the width of the screen"""

        return self._surface.get_size()[0]
    
    def get_stagger_value(self, array):
        """Returns an integer value based on how many elements are in the array.
         The more elements the smaller the value will be."""
        
        if len(array) <= 8:
            return 40
        elif len(array) <= 12:
            return 35
        else:
            return 30
    
    def check_event(self, event):
        """Checks the type of the event and calls the related event handlers."""

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            self.check_card_click(mouse_pos)
        elif event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            self.check_card_dragging(mouse_pos)
        elif event.type == pg.MOUSEBUTTONUP:
            mouse_pos = event.pos
            self.check_card_placement(mouse_pos)

    def check_card_click(self, mouse_pos):
        """Takes a mouse position coordinate. Checks if a card has been clicked and updates any game information related
         to a card click."""

        # add free cells and columns to the list of areas to check
        card_areas = []
        free_cells = self._game.get_card_areas()["free-cells"]
        columns = self._game.get_card_areas()["column-cells"]

        for free_cell in free_cells.values():
            card_areas.append(free_cell)
        for column in columns.values():
            card_areas.append(column)

        # check cards in free-cells/columns, starting at the bottom for each area and moving upward
        columns = self._game.get_card_areas()["column-cells"]

        for card_area in card_areas:
            if card_area.is_empty(): continue

            # from bottom to top, check if mouse clicked the card in the card_area
            for card in reversed(card_area.get_cards()):

                if card.get_rect().collidepoint(mouse_pos):
                    self._game.select_card(card, card_area)

                    # update mouse movement offsets
                    mouse_x, mouse_y = mouse_pos
                    self._mouse_drag_x_offset = card.get_x() - mouse_x
                    self._mouse_drag_y_offset = card.get_y() - mouse_y

                    # update card positions in the cell the cards were just chosen from
                    self.update_card_positions(card_area)

                    return  # once card has been clicked, stop searching

    def check_card_dragging(self, mouse_pos):
        """Takes a mouse position coordinate. Checks if any cards are currently being dragged by the player and updates
         the positions for any selected cards."""
        
        selected_cards = self._game.get_selected_cards()

        # if selected cards, update the positions for each card
        if selected_cards:
            mouse_x, mouse_y = mouse_pos
            x = mouse_x + self._mouse_drag_x_offset
            y = mouse_y + self._mouse_drag_y_offset

            y_offset = self.get_stagger_value(selected_cards)
            for card in selected_cards:
                card.set_pos(x, y)
                y += y_offset

    def check_card_placement(self, mouse_pos):
        """Takes a mouse position coordinate. Checks where any selected cards are dropped and moves them to the correct
         position on the display."""
        
        selected_cards = self._game.get_selected_cards()

        # if selected cards, check where they are placed (if multiple cards are being dragged, checks where the top card is placed)
        if selected_cards:

            # get horizontal and vertical mid points for the top selected card
            card_mid_x, card_mid_y = self.calculate_mid_points(selected_cards[0])

            # add all card areas to the list of areas to check
            card_areas = []
            for card_area_type in self._game.get_card_areas().values():
                for card_area in card_area_type.values():
                    card_areas.append(card_area)

            for card_area in card_areas:
                if self.check_move_to_cell(card_area, card_mid_x, card_mid_y):
                    return  #  return early if the player dragged the selection to the area, whether or not it was a valid move

            # after checking all areas, if selected cards were not placed on any valid location, move them back
            previous_area = self._game.get_previous_cards_area()
            self._game.move_selection_to_previous_area()
            self.update_card_positions(previous_area)

    def check_move_to_cell(self, card_area, card_mid_x, card_mid_y):
        """Takes a card area, the middle x value for a card, and the middle y value for a card. If the player
         is attempting to move the selected card(s) to the area:
         1.) moves the cards to the area if valid
         2.) moves the cards back if not valid
         if either #1 or #2, then method returns True. Else returns False."""
        
        # when placing cards in an empty area, user places them on the area itself
        # when placing cards in an occupied area, user places them on the last card in that area
        if card_area.is_empty():
            placement_area = card_area
        else:
            placement_area = card_area.get_cards()[-1]

        # check if mid_x and mid_y of top selected card is within the boundaries of the card area
        left = placement_area.get_x()
        right = placement_area.get_x() + placement_area.get_scaled_width()
        top = placement_area.get_y()
        bottom = placement_area.get_y() + placement_area.get_scaled_height()

        # if mid points are in bounds of the card area, then check for valid placement
        if card_mid_x > left and card_mid_x < right and card_mid_y < bottom and card_mid_y > top:

            # card(s) moved to the location picked by the user
            if self._game.valid_move(card_area):
                self._game.move_selection_to_area(card_area)
                self.update_card_positions(card_area)
            # card(s) moved back to their previous location
            else:
                previous_area = self._game.get_previous_cards_area()
                self._game.move_selection_to_previous_area()
                self.update_card_positions(previous_area)
            return True  # returns True if cards were placed on the area (regardless of whether it was a valid move)
        
        # returns False if cards were not placed on the area
        return False

    def calculate_mid_points(self, card):
        """Returns a tuple in the form (mid_x, mid_y) which contains horizontal and vertical mid points for a card."""

        left = card.get_x()
        right = card.get_x() + card.get_scaled_width()
        mid_x = (left + right) / 2
        top = card.get_y()
        bottom = card.get_y() + card.get_scaled_height()
        mid_y = (top + bottom) / 2
        
        return (mid_x, mid_y)

    def update_card_positions(self, card_area):
        """Takes a CardArea as a parameter and updates the coordinates (x and y values)
         for all cards in the area."""
        
        x, y = card_area.get_x(), card_area.get_y()
        
        # cards in a suit cell are all stacked on top of each other
        if isinstance(card_area, SuitCell):
            for card in card_area.get_cards():
                card.set_pos(x, y)
        # cards in a column are staggered (free cells only contain one card so this doesn't need to
        # check for the free cell type)
        else:
            y_offset = self.get_stagger_value(card_area.get_cards())

            for card in card_area.get_cards():
                card.set_pos(x, y)
                y += y_offset

    def fill_background(self):
        """Makes background green."""

        self._surface.fill((75, 105, 47, 255))

    def draw_image(self, image, position):
        """Takes in an image and a position and draws the image onto the screen at that position."""

        self._surface.blit(image, position)

    def render(self):
        """Wipes the display and blits all drawable game objects."""

        # fill background with green
        self.fill_background()

        # draw all card areas as well as the cards within them
        self.render_card_areas()

        # wipe and update the screen
        pg.display.flip()

    def render_card_areas(self):
        """Draws card areas to the screen."""

        self.render_cells("free-cells")
        self.render_cells("suit-cells")
        self.render_cells("column-cells")
        self.render_selected_cards()

    def render_cells(self, area_type):
        """Takes in an area type string, which can be 'suit-cells', 'column-cells', or 'free-cells'.
         Draws all of the specified cells to the screen."""
        
        cells = self._game.get_card_areas()[area_type]

        # draw column/free-cell/suit-cell
        for cell in cells.values():
            self.draw_image(cell.get_image(), cell.get_pos())
            cards = cell.get_cards()

            # draw all cards in the column/free-cell/suit-cell
            for card in cards:
                self.draw_image(card.get_image(), card.get_pos())

    def render_selected_cards(self):
        """Draws any cards currently being dragged to the screen."""
        
        selected = self._game.get_selected_cards()

        for card in selected:
            self.draw_image(card.get_image(), card.get_pos())

