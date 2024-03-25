from mappable_sprite import MappableSprite
from sprite_sheet import SpriteSheet
from constants import *


class ResetButton(MappableSprite):
    """A class representing a reset button."""

    def __init__(self, image=None):
        self._width = 48
        self._height = 32
        self._scale = SCALE
        self._images = {
            "up": None,
            "down": None
        }
        self.init_images()
        self.set_default_image()

    def get_scaled_width(self):
        """Returns the scaled width of the button."""

        return self._width * self._scale
    
    def get_scaled_height(self):
        """Returns the scaled height of the button."""

        return self._height * self._scale

    def init_images(self):
        """Fills the images dictionary with sprites."""

        sprites = SpriteSheet("images/reset_button.png")
        up_sprite = sprites.get_sprite(48, 0, self._width, self._height, self._scale)
        down_sprite = sprites.get_sprite(0, 0, self._width, self._height, self._scale)
        self._images["up"] = up_sprite
        self._images["down"] = down_sprite        

    def set_default_image(self):
        """Sets the starting sprite to the unpressed button image."""

        super().__init__(self._images["up"])

    def set_image_up(self):
        """Sets the sprite to the unpressed image."""

        self._image = self._images["up"]

    def set_image_down(self):
        """Sets the sprite to the pressed image."""

        self._image = self._images["down"]