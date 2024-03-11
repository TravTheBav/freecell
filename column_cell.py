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