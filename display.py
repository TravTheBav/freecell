import pygame as pg


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
        
        pass

    def update_card_positions(self, card_area):
        """Takes a CardArea as a parameter and updates the coordinates (x and y values)
         for all cards in the area."""
        
        pass

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

