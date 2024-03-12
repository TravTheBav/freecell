import random
from card import Card

class Deck:
    """Represents a deck of playing cards. In free cell solitaire the deck is hidden, so 
    it is primarily used to initialize the cards before they are placed into their starting
    areas."""

    def __init__(self):
        self._cards = []
        self.init_cards()

    def init_cards(self):
        """Fills the deck with 52 cards."""

        # clubs, spades, diamonds, hearts
        for suit in range(1, 5):
            # Ace, 2, 3, ... , Queen, King
            for value in range(1, 14):
                card = Card(suit, value)

                self.add_card(card)

    def add_card(self, card):
        """Adds a card to the top of the deck."""

        self._cards.append(card)

    def draw_card(self):
        """Pops a card from the cards list and returns it."""

        return self._cards.pop()
    
    def shuffle(self):
        """Shuffles the cards list."""

        random.shuffle(self._cards)
