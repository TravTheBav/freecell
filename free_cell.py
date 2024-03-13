from card_area import CardArea

class FreeCell(CardArea):
    """Inherits from the CardArea class. Represents a free cell. Free cells can only contain one
    card at a time. Any card can be placed into an empty free cell."""

    def __init__(self):
        super().__init__()

    def valid_selection(self, card):
        """Returns True if the card is the card in the cards list and returns
        False if it is not."""

        if len(self._cards) == 0:  # cannot select a card if free cell is empty
            return False

        if card == self._cards[0]:
            return True
        
        return False