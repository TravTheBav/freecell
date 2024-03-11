class Card:
    """Represents a standard playing card."""

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

        if self._suit == 1 or self._suit == 2:
            self._color = "black"
        else:
            self._color = "red"

    def get_suit(self):
        """Returns the card's suit, which is an integer in range [1, 4]."""

        return self._suit
    
    def get_value(self):
        """Returns the card's value, which is an integer in range [1, 13]."""

        return self._value
    
    def get_color(self):
        """Returns the card's color, which is either red or black depending on the suit."""

        return self._color
    
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

        return f"{value} of {suits[self._suit]}"