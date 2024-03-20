import pygame as pg


class MappableSprite(pg.sprite.Sprite):
    """A parent class for any mappable game sprite. Mappable sprites are defined as regular pygame sprites
    with coordinates attached to them."""

    def __init__(self, image):
        pg.sprite.Sprite.__init__(self)

        self._image = image
        self._rect = self._image.get_rect()
        self._rect.x = 0
        self._rect.y = 0

    def get_image(self):
        """Returns an image of the surface of the mappable object."""
        return self._image
    
    def get_rect(self):
        """Returns the rectangle attribute."""
        return self._rect
    
    def get_x(self):
        """Returns the x coordinate."""
        return self._rect.x

    def get_y(self):
        """Returns the y coordinate."""
        return self._rect.y
    
    def get_pos(self):
        """Returns a tuple in the form (x-coordinate, y-coordinate)."""
        return self._rect.x, self._rect.y
    
    def set_pos(self, x, y):
        """Sets the mappable sprite's coordinates."""
        self._rect.x = x
        self._rect.y = y
