# Run this file to play a game of Free Cell solitaire
from game import *
from display import *
import pygame as pg


def main():
    """Main game loop function. Initializes Pygame and the game instance."""
    
    # pygame starting setup
    pg.init()
    clock = pg.time.Clock()

    # set game and display objects
    game = Game()
    display = game.get_display()
    
    # game loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            else:
                display.check_event(event)

            display.render()
            clock.tick(144)


if __name__ == "__main__":
    main()