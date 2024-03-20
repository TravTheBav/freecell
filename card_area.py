from mappable_sprite import *
from sprite_sheet import SpriteSheet


class CardArea(MappableSprite):
    """Represents a generic area to place cards."""


    def __init__(self, image=None):

        self._width = 48
        self._height = 64
        self._scale = 1.8
        self._cards = []

        # image can either be set on init by passing in a sprite
        # or will default to a black bordered box
        if image:
            super().__init__(image)
        else:
            self.set_default_image()

    def set_default_image(self):
        """Called on initialization, sets up the card area's sprite."""

        # set sprite to a solid bordered box
        sprites = SpriteSheet("images/cards.png")
        image = sprites.get_sprite(96, 256, self._width, self._height, self._scale)

        super().__init__(image)

    def __repr__(self):
        """Formats the card area's string representation into is list contents"""

        return str(self._cards)
    
    def get_scaled_width(self):
        """Returns the scaled width of the card area."""

        return self._width * self._scale
    
    def get_scaled_height(self):
        """Returns the scaled height of the card area."""

        return self._height * self._scale

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
