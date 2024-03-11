# What is Free Cell?

Free cell is a version of solitaire where all cards are shown face up on the table at 
the beginning of the game, and each card is placed in one of eight columns. In order to win, the player must stack all cards into four piles, separated by suit, each in ascending order (Ace to King).

## How to play

The game starts off with four free cells. The player can place any card into a free cell. However,in order to remove a card from a free cell, the card must be placed onto another card that fits the following criteria:
1. is the opposite color (if the card being placed is red, than the card it is being placed
on must be black)
2. has a value 1 higher than the card being placed (if the card being placed is a 9 of hearts,  than the card it is being placed on must be a 10 of spades/clubs)

Multiple cards may be moved around at the same time following the same rules as above (must be in strictly descending order and alternate in color), with the following caveat: **the player can only move n+1 cards around at a given time, where n = *number of empty spaces, not including areas to stack cards by suit*.** For example, if there are 3 open free cells and 1 column with no cards in it, then the player can move up to 5 cards at a time (3 + 1 + 1 = 5). As well, if there are no empty spaces, then the player can only move 1 card at a time until more spaces open up.

## Is it possible to lose?
Yes, but the game does not detect a loss. It is up to the player to understand when they have reached a point where it is impossible to win.