import numpy as np
import pandas as pd
import random

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    def __init__(self,size=(3,4)):
        self.p1 = Player()
        self.p2 = Player()
        self.turn = random.choice([self.p1,self.p2])

    def __repr__(self):
        pass

    def game_over(self):
        pass
        # if ___ == ___
        # print("GAME OVER")
        # again = input("Play again? [Y]/n:").lower()
        # if again == "n":
        # break
        # Courtesy of Petra. :) <3


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
        
        ==========================================================
        """
        col_idx = range(self.cols)
        row_idx = [chr(letter) for letter in range(65, 65+self.rows)]
        board_emoji = np.array([[EMOJI[val] for val in row] for row in self.state])
        board_df = pd.DataFrame(data=board_emoji, index=row_idx, columns=col_idx)
        return str(board_df)

    def take(self, row, col):
        
        for r in range(row+1):
            self.state[r][col:] = 0
    
class Player:
    def __init__(self,score=0,name=None):
        self.score = score
        self.name = input("Enter your name: ")
        
    def __repr__(self):
        return f'Player(score={self.score},name={self.name})'
