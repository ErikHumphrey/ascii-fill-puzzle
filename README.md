# ascii-fill-puzzle

Simple interactive text-based game in Python.

The rules and sample levels are borrowed from a specification for a programming assignment found on [Dr. Andrew Runka's website](https://web.archive.org/web/20191205024932/http://people.scs.carleton.ca/~arunka/courses/comp1405/assignments/a5/) on December 4, 2019.

## Prerequisites

* [Python 3](https://www.python.org/downloads/)

## To play

Clone the repository and run `cd ascii-fill-puzzle/a3 && python ascii_fill.py`, then follow the prompts.

The game currently goes through levels named "ascii_fill_levelX.txt" in the "levels" folder, where X is the level number from 1 to 5.

After each level, the number of moves to solve that level are displayed and the next level will begin. After Level 5 is completed, the total number of moves they used for the whole game is displayed, and you'll be prompted to play again.

> #### Game rules
> 
> The game progresses in 5 levels, each with a unique game board loaded from file. The game board is a 2D list of symbols (strings) from the set {'&', '@', '#', '%'}. The goal of the game is to make all of the symbols on the board the same in the fewest possible moves.
> 
> The player's moves consist of picking a symbol and a location on the board. Then, that location and all contiguous symbols (ie matching symbols in adjacent locations) are changed to the user's selected symbol. For an example, see the sample runs below. The player will keep making moves of this sort until the entire gameboard is all the same symbol.
