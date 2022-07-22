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


def generate_ship_loc(board):
    """
    4 ships populated onto the board via a while loop
    """
    ship_num = 0
    while ship_num < 4:
        ship_num = 0
        ship_col = random_number(board)
        ship_row = random_number(board)
        board[ship_row][ship_col] = " o "
        for row in board:
            ship_num += row.count(" o ")

