from card_area import CardArea

class ColumnCell(CardArea):
    """Inherits from the CardArea class. Represents a cell where cards are stacked on top of each other.
    At the beginning of the game, the cards in a column cell have no order. However, whenever new card(s)
    are added to a column by the player, the bottom card in the column and the new cards must:
    1.) alternate colors
    2.) be in a strictly descending order (each card value decrements by 1)
    If the column is empty, then only the cards being added to the column need to follow these rules."""

    def __init__(self):
        super().__init__()

    def valid_selection(self, card):
        """Returns True if the card is considered a valid selection, otherwise False."""

        # guards against an attempt to select a card that isn't in the column
        if card not in self._cards: return False

        color = card.get_color()
        value = card.get_value()
        # comparisons start one card after the selected card; if the selected card is the last card, method returns True
        card_idx = self._cards.index(card) + 1  

        # card color must alternate and value of current card must be one less than the previous card
        while card_idx < len(self._cards):
            current = self._cards[card_idx]
            if current.get_color() == color or current.get_value() != (value - 1):
                return False
            
            color = current.get_color()
            value = current.get_value()
            card_idx += 1

        return True

    def valid_move(self, cards):
        """Takes in a list of cards. Returns True if moving the card(s) to the column would be a valid move,
          otherwise False."""

        # if column is empty, then return True regardless of how many cards are being moved
        if self.is_empty(): return True

        # else if column is not empty, the last card in the column must:
        # 1.) be one value higher than the first card in the cards list
        # 2.) be a different color than the first card in the cards list
        last_card_in_column = self._cards[-1]
        first_card_in_selection = cards[0]

        if last_card_in_column.get_value() == first_card_in_selection.get_value() + 1 and \
           last_card_in_column.get_color() != first_card_in_selection.get_color():
            return True
        
        return False
