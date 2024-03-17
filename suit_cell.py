from card_area import CardArea

class SuitCell(CardArea):
    """Inherits from the CardArea class. Represents a cell where cards are placed in ascending order
    (from Ace to King) by suit. When a suit cell is empty, any Ace can be placed into it. Thereafter,
    all cards added to that cell must be of the same suit. Once a card is placed in a suit cell, it
    cannot be removed."""

    def __init__(self):
        super().__init__()

    def valid_move(self, cards):
        """Takes in a list of cards. If there is only one card in the list, then returns True
        if placing that card in the suit cell is considered valid, otherwise returns False."""

        if len(cards) != 1: return False  # only one card can be moved at a time to a suit cell
        
        card = cards[0]

        if self.is_empty() and card.get_value() == 1:  # cell is empty and card is an Ace
            return True
        elif self.is_empty() and card.get_value() != 1:  # cell is empty and card is not an Ace
            return False
        else:  # check if card being placed is same suit and one value higher than top of stack
            top_card = self._cards[-1]
            if card.get_suit() == top_card.get_suit() and \
               card.get_value() - top_card.get_value() == 1:
                return True
            
        return False