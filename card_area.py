class CardArea:
    """Represents a generic area to place cards."""

    def __init__(self):
        self._cards = []

    def __repr__(self):
        """Formats the card area's string representation into is list contents"""

        return str(self._cards)

    def get_cards(self):
        """Returns the list of cards."""

        return self._cards
    
    def set_cards(self, cards=None):
        """Takes in a list of card objects and sets cards data attribute to the list."""

        if not cards:
            self._cards = []
        else:
            self._cards = cards
    
    def add_card(self, card):
        """Appends a card to the cards list."""

        self._cards.append(card)

    def cards_count(self):
        """Returns an integer representing the amount of cards in the cards list."""

        return len(self._cards)
    
    def is_empty(self):
        """Returns True if there are no cards, otherwise returns False."""

        if self.cards_count() == 0: return True

        return False
    
    def place_cards(self, cards):
        """Takes a list of Cards and appends them to the cards data attribute. The ordering of the newly added
        cards remains the same."""

        self._cards += cards
