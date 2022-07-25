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
    Opening message & enter player's username
    """
    print("_" * 35)
    print("Welcome to Battleship")
    print(f"Board Size: 5*5, Number of Ships: 4")
    name = input(f"Please enter your name: ")
    print(f"Welcome {name}, Generating boards!")


def generate_boards():
    """
    Creates the nessecary boards for the game
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
            if validation(guess_col):
                break
        while True:
            guess_row = input("Enter a row number to fire at: \n")
            if validation(guess_row):
                break

        guess_col = int(guess_col)-1
        guess_row = int(guess_row)-1

        if (user_guesses[guess_row][guess_col] == " * " or
                user_guesses[guess_row][guess_col] == " X "):
            print("Already guessed, make another choice")
        else:
            repeat = False
    if comp[guess_row][guess_col] == " o ":
        user_guesses[guess_row][guess_col] = " X "
        print(f"\n{guess_col+1}, {guess_row+1}: HIT!")
    else:
        user_guesses[guess_row][guess_col] = " * "
        print(f"\n{guess_col+1}, {guess_row+1}: MISS!")


def comp_guess():
    """
    Computer guess at user board using randomly generate co-ordinates
    """
    print("\n\nComputers turn:")
    repeat = True

    guess_col = random_number(comp)
    guess_row = random_number(comp)

    while repeat:
        if (user[guess_row][guess_col] == " * " or
                user[guess_row][guess_col] == " X "):
            guess_col = random_number(comp)
            guess_row = random_number(comp)
        else:
            repeat = False
    print(f"Computer guessed: {guess_col + 1}, {guess_row + 1}")
    if user[guess_row][guess_col] == " o ":
        user[guess_row][guess_col] = " X "
        print("HIT")
    else:
        user[guess_row][guess_col] = " * "
        print("MISS")


def validation(value):
    """
    Check inputs are only numbers between 1 and 5
    """
    try:
        if int(value) > 5 or int(value) < 1:
            raise ValueError(
                "Your shot is out of bounds! Choose a number between 1 and 5"
            )
    except ValueError as e:
        print(f"Invalid {e}, Make another guess")
        print("Enter a number between 1 and 5")
        return False
    return True


def game_play():
    """
    Start the game from here
    """
    generate_boards()
    welcome_message()
    i = 0
    while i < 10:
        print(f"\nThis is turn {i +1}/10 \n")
        user_guess()
        print_board(user_guesses)
        #input("\nPress Enter to continue...")
        comp_guess()
        print("\nHere's your board: ")
        print_board(user)
        #input("\nPress Enter to continue...")
        i += 1
        if check_winner(user) == 4:
            i = 10
        elif check_winner(user_guesses) == 4:
            i = 10
    check_winner_final()

def check_winner(board):
    """
    Checks how many hit battleships in the board
    """
    total = 0
    for list in board:
        total += list.count(" X ")
    return total


def check_winner_final():
    """
    Check for a winner after ten turns and report the result to the user
    """
    user_result = check_winner(user_guesses)
    comp_result = check_winner(user)
    if user_result > comp_result:
        print("You win!")
    elif user_result < comp_result:
        print("Computer wins")
    else:
        print("It was a draw!")


# Call the main function
game_play()