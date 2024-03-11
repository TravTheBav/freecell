from card_area import CardArea

class SuitCell(CardArea):
    """Inherits from the CardArea class. Represents a cell where cards are placed in ascending order
    (from Ace to King) by suit. When a suit cell is empty, any Ace can be placed into it. Thereafter,
    all cards added to that cell must be of the same suit. Once a card is placed in a suit cell, it
    cannot be removed."""

    def __init__(self):
        super().__init__()