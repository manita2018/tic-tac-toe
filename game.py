# coding=utf-8
def game_loop():
    # The game should run until we return
    while True:
        print_board()

        current_player = get_current_player()

        coordinates = get_coordinates()

        place_token(current_player, coordinates[0], coordinates[1])

        if did_win(current_player):
            print('{} has won the game 🏅'.format(current_player))
            return

        elif is_board_full():
            # Game over baby
            print('The board is full and nobody won')
            return
        else:
            print("Nobody has won yet, keep looping")


BOARD = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def print_board():
    for row in BOARD:
        print(row)


def get_current_player():
    current_player = raw_input('whose turn is it?\n')
    return current_player


def get_coordinates():

    while True:  # first while loop code
        i = raw_input('which column?\n')
        try:
            x_coord = int(i)
        except ValueError:
            print('\nYou did not enter a valid integer. Please enter a valid integer.')
            continue
        if x_coord > 2:
            print ('Please enter an integer between 0 and 2.\n')
            continue
        break

    while True:  # first while loop code
        i = raw_input('which row?\n')
        try:
            y_coord = int(i)
        except ValueError:
            print('\nYou did not enter a valid integer. Please enter a valid integer.')
            continue
        if y_coord > 2:
            print ('Please enter an integer between 0 and 2.\n')
            continue
        break

    return [x_coord, y_coord]


def place_token(token, x_coord, y_coord):
    BOARD[x_coord][y_coord] = token


def did_win(player):
    player_has_won = False
    for row in BOARD:
        if row[0] == player and row[1] == player and row[2] == player:
            player_has_won = True

    return player_has_won


def is_board_full():
    board_is_full = False
    for row in BOARD:
        if row[0] != '-' and row[1] != '-' and row[2] != '-':
            board_is_full = True

    return board_is_full


def is_legal_move(token, x_coord, y_coord):
    # TODO this should probably be used somewhere...
    raise NotImplementedError


# Run the program
game_loop()
