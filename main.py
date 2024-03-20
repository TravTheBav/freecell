# Run this file to play a game of Free Cell solitaire
from game import *
from display import *
import pygame as pg


def main():
    """Main game loop function. Initializes Pygame, the game, and
     the display."""

    game = Game()
    display = Display(game)
    clock = pg.time.Clock()
    pg.init()
    pg.display.set_caption("Free Cell")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            else:
                display.check_event(event)

            display.render()
            clock.tick(60)


if __name__ == "__main__":
    main()