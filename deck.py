import random
from constants import *
from card import Card
from sprite_sheet import SpriteSheet


class Deck:
    """Represents a deck of playing cards. In free cell solitaire the deck is hidden, so 
    it is primarily used to initialize the cards before they are placed into their starting
    areas."""

    def __init__(self):
        self._cards = []
        self.init_cards()

    def init_cards(self):
        """Fills the deck with 52 cards."""

        sprites = SpriteSheet("images/cards.png")

        # clubs, spades, diamonds, hearts
        for suit in range(1, 5):
            x_coord = 0
            y_coord = CARD_HEIGHT * (suit - 1)

            # Ace, 2, 3, ... , Queen, King
            for value in range(1, 14):
                sprite = sprites.get_sprite(x_coord, y_coord, CARD_WIDTH, CARD_HEIGHT, SCALE)
                card = Card(suit, value, sprite)

                self.add_card(card)
                x_coord += CARD_WIDTH

    def add_card(self, card):
        """Adds a card to the top of the deck."""

        self._cards.append(card)

    def draw_card(self):
        """Pops a card from the cards list and returns it."""

        return self._cards.pop()
    
    def shuffle(self):
        """Shuffles the cards list."""

        random.shuffle(self._cards)
