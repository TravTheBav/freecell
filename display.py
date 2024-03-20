import pygame as pg


class Display:
    """A class for linking up the display to the Game logic. Handles mouse movements
     and button clicks by the player."""
        
    def __init__(self, game):
        
        self._game = game
        self._surface = pg.display.set_mode((1280, 720))
        pg.display.set_caption("Free Cell")

    def get_width(self):
        """Returns the width of the screen"""

        return self._surface.get_size()[0]

    def check_event(self, event):
        """Checks the type of the event and calls the related event handlers."""

        pass

    def mouse_clicked(self):
        """Detects when the left mouse button is clicked and calls methods to handle
         the event."""
    
        pass

    def mouse_down(self):
        """Detects when the left mouse button is held down and calls methods to
         handle the event."""

        pass

    def mouse_released(self):
        """Detects when the left mouse button is released and calls methods to
         handle the event."""
        
        pass

    def check_card_click(self):
        """Checks if a card has been clicked and updates any game information related
         to a card click."""

        pass

    def check_card_dragging(self):
        """Checks if any cards are currently being dragged by the player and updates
         the positions for any selected cards."""
        
        pass

    def check_card_placement(self):
        """Checks where any selected cards are dropped and moves them to the correct
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

    def render_cells(self, area_type):
        """Takes in an area type string, which can be 'suit-cells', 'column-cells', or 'free-cells'.
         Draws all of the specified cells to the screen."""
        
        cells = self._game.get_card_areas()[area_type]

        # draw columns
        if area_type == "column-cells":
            for cell in cells.values():
                self.draw_image(cell.get_image(), cell.get_pos())  # right now this looks like code duplication, but this is necessary for when we add card drawing
        # draw free cells or suit cells
        else:
            for cell in cells.values():
                self.draw_image(cell.get_image(), cell.get_pos())
