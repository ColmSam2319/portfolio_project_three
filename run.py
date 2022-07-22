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


def welcome_message():
    """
    Opening message & enter player username
    """
    print("_" * 35)
    print("Welcome to BATTLESHIP")
    print(f"Board size: 5*5, Number of Ships: 4")
    name = input(f"Please enter your name: ")
    print(f"Welcome {name}, Generating boards!")


def generate_boards():
    """
    Creates the necessary boards for the game
    """
    make_board(user)
    make_board(comp)
    make_board(user_guesses)
    generate_ship_loc(user)
    generate_ship_loc(comp)


def user_guess():
    """
    Get user input on battleship guess
    """
    print("Opponent's board")
    print(f"_" * 35)
    print_board(user_guesses)
    repeat = True
    while repeat:
        while True:
            guess_col = input("Enter a column number to fire at: \n")
            if validation(guess_row):
                break

        guess_col = int(guess_col)-1
        guess_row = int(guess_row)-1

        if (user_guesses[guess_row][guess_col] == " * " or
                user_guesses[guess_row][guess_col] == "X"):
            print("Already guessed, make another choice")
        else:
            repeat = False
    if comp[guess_row][guess_col] == "o":
        user_guesses[guess_row][guess_col] = " X "
        print(f"\n{guess_col+1},{guess_row+1}: HIT!")
    else:
        user_guesses[guess_row][guess_col] = " * "
        print(f"\n{guess_col+1},{guess_row+1}: MISS!")




