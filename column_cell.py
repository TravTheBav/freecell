from card_area import CardArea

class ColumnCell(CardArea):
    """Inherits from the CardArea class. Represents a cell where cards are stacked on top of each other.
    At the beginning of the game, the cards in a column cell have no order. However, whenever new card(s)
    are added to a column by the player, they must be:
    1.) placed on top of the 'bottom' card in the stack
    2.) alternate colors
    3.) be in a strictly descending order (each card value decrements by 1)
    If there is no card in a cell, then only rules #2 and #3 are relevant."""

    def __init__(self):
        super().__init__()

    def valid_selection(self, card):
        """Returns True if:
        1.) card is in list
        2.) all cards below the attempted selection alternate color and decrement by 1 for each card
        Otherwise returns False"""

        # guards against an attempt to select a card that isn't in the column
        if card not in self._cards: return False

        color = card.get_color()
        value = card.get_value()
        # comparisons start one card after the selected card; if the selected card is the last card, method returns True
        card_idx = self._cards.index(card) + 1  

        while card_idx < len(self._cards):
            current = self._cards[card_idx]
            if current.get_color() == color or current.get_value() != (value - 1):
                return False
            
            color = current.get_color()
            value = current.get_value()
            card_idx += 1

        return True

