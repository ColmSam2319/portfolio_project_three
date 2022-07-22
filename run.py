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


def print_board(board):
    """
    Print the board
    """
    for ind in board:
        print(" ".join(ind))


def random_number(r):
    """
    Generate a random number between 0 and the length of the board minus one.
    """
    return randint(0, len(r)-1)
