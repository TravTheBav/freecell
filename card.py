from mappable_sprite import MappableSprite
from constants import *


class Card(MappableSprite):
    """Represents a standard playing card."""

    def __init__(self, suit, value, image):
        super().__init__(image)

        self._width = CARD_WIDTH
        self._height = CARD_HEIGHT
        self._scale = SCALE
        self._suit = suit
        self._value = value

        if self._suit == 1 or self._suit == 2:
            self._color = "black"
        else:
            self._color = "red"

    def __repr__(self):
        """Formats the card's string representation into 'VALUE of SUIT'."""

        suits = {
            1: 'Clubs',
            2: 'Spades',
            3: 'Diamonds',
            4: 'Hearts'
        }

        vals = {
            1: 'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }

        if self._value in vals.keys():
            value = vals[self._value]
        else:
            value = str(self._value)

        # set text color for the console output based on the card's color
        if self._color == "red":
            ansi_color_code = "\033[0;31m"
        else:
            ansi_color_code = "\033[0;30m"
        ansi_end_code = "\033[0m"

        return ansi_color_code + f"{value} of {suits[self._suit]}" + ansi_end_code
    
    def get_string_length(self):
        """Returns the length of the card's string representation."""

        card_string = self.__repr__()
        return len(card_string) - 11  # subtracts the length of ansi color codes

    def get_suit(self):
        """Returns the card's suit, which is an integer in range [1, 4]."""

        return self._suit
    
    def get_value(self):
        """Returns the card's value, which is an integer in range [1, 13]."""

        return self._value
    
    def get_color(self):
        """Returns the card's color, which is either red or black depending on the suit."""

        return self._color
    
    def get_scaled_width(self):
        """Returns the scaled width of the card."""

        return self._width * self._scale
    
    def get_scaled_height(self):
        """Returns the scaled height of the card."""

        return self._height * self._scale
