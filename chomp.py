import numpy as np
import pandas as pd
import random
import itertools

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    """Contains the control flow for the game"""
    def __init__(self, n_players=2, size=(3, 4)):
        self.n_players = n_players
        self.size = size
        self.board = Board(*size)
        self.game_over = False
        self.players = []
        self.current_player = None

    def __repr__(self):
        return f'ChompGame({self.n_players}, {self.size})'

    def play(self):
        self.setup()
        while not self.game_over:
            print(f'{self.current_player}, it\'s your turn!\n')
            print(self.board)
            self.move()
            if self.board.state[-1][0] == 0:
                self.game_over = True
                self.current_player.wins -= 1
                # just change to opposite
                
            elif self.board.state[-1][0] == 0:
                print(f'{self.current_player[1]}, it\'s your turn!\n')
                print(self.board)
                self.move()
                if self.board.state[-1][0] == 0:
                    self.game_over = True
                    self.current_player.wins -= 1
                # just change to opposite for 2nd player

    def setup(self):
        for i in range(1, self.n_players + 2):
            print(f'***Player {i}***')
            self.players.append(Player())

        self.current_player = self.player_select_generator()
        # self.current_player = self.player_select_generator()

# probably an unneeded function
    def player_select_generator(self): pass
        i = 0
        for player in itertools.cycle(self.players):
            i += 1
            if i == 10:
                break
            return i, player

    def move(self):
        coord_str = input("Enter the coordinates for your move. (e.g. A3)")
        row_str, col_str = coord_str[0].upper(), coord_str[1]
        row = ord(row_str) - 65
        col = int(col_str)
        self.board.take(row, col)


class Board:
    def __init__(self, rows, cols):
        # Use a 2d array to store board state
        # ones for chocolate, zeros for eaten squares, and -1 for poison
        self.rows = rows
        self.cols = cols
        self.state = np.ones((rows, cols), dtype=int)
        self.state[-1][0] = -1

    def __repr__(self):
        return f'Board({self.rows}, {self.cols})'

    def __str__(self):
        col_idx = range(self.cols)
        row_idx = [chr(letter) for letter in range(65, 65+self.rows)]
        board_emoji = np.array([[EMOJI[val] for val in row] for row in self.state])
        board_df = pd.DataFrame(data=board_emoji, index=row_idx, columns=col_idx)
        return str(board_df)

    def take(self, row, col):
        # self.state[:row+1, col:] = 0
        for r in range(row+1):
            self.state[r][col:] = 0


class Player:
    def __init__(self):
        self.name = input("\tEnter your name: ")
        self.wins = 0

    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return self.name

"""
Does two things:
==========================================================
        
Initially, you have arrays that have
a specific value to them, like 1 and
-1. We can assign these numbers a different
value. In this case, an emoji.
        
chr() essentially makes you input a
number and then spits out a character.
Maps this to the rows of the game, battle-ship
style. (dictionary translation)
        
Process goes to:
array -> dictionary -> data-frame
        
Data-frame helps with the
visual aspect of the game, because
you do not need to manually change
the spacing every time it doesn't match.
It's neatly monospaced.
       
The 65 represents the the letter a in the
alphabet. Looping over this means you can
include the entire alphabet when playing
the game.

----------------------------------------------------------

**** Yield Docs ****

Yield expressions and statements are only used
when defining a generator function, and are only
used in the body of the generator function.
Using yield in a function definition is sufficient
to cause that definition to create a generator
function instead of a normal function.

----------------------------------------------------------

**** itertools.cycle() Docs ****

Make an iterator returning elements from the iterable 
and saving a copy of each. When the iterable is 
exhausted, return elements from the saved copy. 
Repeats indefinitely.

==========================================================
"""
