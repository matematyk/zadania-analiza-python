"""
Suggest a data structure to represent the checkers game board
(stones are of two colors, they stand only on black squares, some are queens). 
Write a function that generates all possible moves for the player playing stones of the color given by the function parameter.

What data structure will you use to represent the board and the result?
"""

def board():
    rows = 8
    cols = 8
    board = {}

    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 1:
                board[(i+1,j+1)] = 'black'
            else:
                board[(i+1,j+1)] = 'white'
    return board


print(board()) 