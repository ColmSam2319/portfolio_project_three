from random import randint

user = []
user_guesses = []
comp = []

def make_board(board):
    """
    Make an empty 5*5 board
    """
    for i in range(5):
        board.append([" O "]*5)
    return board

print("board")