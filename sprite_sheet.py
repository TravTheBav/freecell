import pygame as pg


class SpriteSheet:
    """A class for representing a sprite sheet. Allows specific sections of the
    sheet to be retrieved."""

    def __init__(self, img_file_path):
        self._full_sheet_image = pg.image.load(img_file_path).convert_alpha()

    def get_sprite(self, x_coord, y_coord, width, height, scale):
        """Returns a section of the sprite sheet image."""

        sprite = pg.Surface((width, height), pg.SRCALPHA)
        sprite.blit(self._full_sheet_image, (0, 0), (x_coord, y_coord, width, height))
        sprite = pg.transform.scale(sprite, (width * scale, height * scale))
        return sprite