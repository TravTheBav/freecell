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
    
    def set_cards(self, cards_list):
        """Takes in a list of card objects and sets cards data attribute to the list."""

        self._cards = cards_list
    
    def add_card(self, card):
        """Appends a card to the cards list."""

        self._cards.append(card)

    def cards_count(self):
        """Returns an integer representing the amount of cards in the cards list."""

        return len(self._cards)
