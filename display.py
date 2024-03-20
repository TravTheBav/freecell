class Display:

    def __init__(self):
        """A class for linking up the display to the Game logic. Handles mouse movements
         and button clicks by the player."""
        
        pass

    def check_events(self):
        """Calls all event handlers."""

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

    def render(self):
        """Wipes the display and blits all drawable game objects."""

        pass
