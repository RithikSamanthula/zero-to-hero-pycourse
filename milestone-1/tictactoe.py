from IPython.display import clear_output
import random

COLOR_RESET = '\x1b[0m'
COLOR_BLUE = '\x1b[0;34;48m'
COLOR_BLUE_BG = '\x1b[7;34;48m'
COLOR_PURPLE = '\x1b[0;35;48m'
COLOR_RED = '\x1b[0;31;48m'
COLOR_RED_BG = '\x1b[7;31;48m'
COLOR_TEAL_BG = '\x1b[7;36;48m'
COLOR_GREEN = '\x1b[7;36;48m'
COLOR_YELLOW = '\x1b[7;33;48m'

COLOR_LENGTH = len(COLOR_RED)
COLOR_LENGTH2 = len(COLOR_BLUE)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def display_board(board):
    clear_output()

    print(COLOR_TEAL_BG + "~Tic Tac Toe~" + COLOR_RESET)
    print("")

    vertical_line = bcolors.OKCYAN + " | " + bcolors.ENDC
    horizontal_line = bcolors.OKCYAN + "- - - - -" + bcolors.ENDC

    print(board[1] + vertical_line + board[2] + vertical_line + board[3])
    print(horizontal_line)
    print(board[4] + vertical_line + board[5] + vertical_line + board[6])
    print(horizontal_line)
    print(board[7] + vertical_line + board[8] + vertical_line + board[9])

test_board = ['#',COLOR_RED+'X'+COLOR_RESET,COLOR_BLUE+'O'+COLOR_RESET,COLOR_RED+'X'+COLOR_RESET,COLOR_BLUE+'O'+COLOR_RESET,COLOR_RED+'X'+COLOR_RESET,COLOR_BLUE+'O'+COLOR_RESET,COLOR_RED+'X'+COLOR_RESET,COLOR_BLUE+'O'+COLOR_RESET,COLOR_RED+'X'+COLOR_RESET]

# display_board(test_board)


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input(bcolors.WARNING+"Player 1: Choose X or O: "+bcolors.ENDC).upper()

    if marker == 'X':

        return 'X', 'O'
    else:
        return 'O', 'X'


# player1_marker, player2_marker = player_input()

def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board,'$',8)
# display_board(test_board)

def win_check(board, mark):
    red = COLOR_LENGTH
    blue = COLOR_LENGTH2
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the middle
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right side
            (board[3] == mark and board[5] == mark and board[7] == mark) or  # diagonal
            (board[1] == mark and board[5] == mark and board[9] == mark))  # diagonal


# display_board(test_board)
# win_check(test_board, 'X')

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# choose_first()

def space_check(board,position):

    return board[position] == ' '

def full_board_check(board):
    for i in range (1,10):
        if space_check(board,i):
            return False

    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(bcolors.WARNING+"Choose a position: (1-9) "+bcolors.ENDC))

    return position

def replay():
    choice = input(bcolors.WARNING+"Would you like to play again? Enter Yes or No "+bcolors.ENDC)
    return choice == 'Yes'

# --------------------------------------------------------------

# WHILE LOOP TO KEEP RUNNING THE GAME

while True:

    UL = str(b'\xcc\xb2', 'utf-8')  # adds underline to the text : used in board[0] and board[1]

    # Play the game

    ## SET EVERYTHING UP (BOARD, FIRST PLAYER, CHOOSE MARKERS (X,O)

    def ascii_art():
        print(bcolors.OKBLUE +'___________.__             ___________                    ___________               '+bcolors.ENDC)
        print(bcolors.OKBLUE+'\__    ___/|__|  ____      \__    ___/_____     ____      \__    ___/____    ____   '+bcolors.ENDC)
        print(bcolors.OKBLUE+'  |    |   |  |_/ ___\       |    |   \__  \  _/ ___\       |    |  /  _ \ _/ __ \  '+bcolors.ENDC)
        print(bcolors.OKBLUE+'  |    |   |  |\  \___       |    |    / __ \_\  \___       |    | (  <_> )\  ___/  '+bcolors.ENDC)
        print(bcolors.OKBLUE+'  |____|   |__| \___  >      |____|   (____  / \___  >      |____|  \____/  \___  > '+bcolors.ENDC)
        print(bcolors.OKBLUE+'                    \/                     \/      \/                           \/  '+bcolors.ENDC)

    ascii_art()

    def player1_wins_ascii():
        print(bcolors.OKBLUE +'__________.__                               ____   __      __.__               '+bcolors.ENDC)
        print(bcolors.OKBLUE +'\______   \  | _____  ___.__. ___________  /_   | /  \    /  \__| ____   ______'+bcolors.ENDC)
        print(bcolors.OKBLUE +' |     ___/  | \__  \<   |  |/ __ \_  __ \  |   | \   \/\/   /  |/    \ /  ___/'+bcolors.ENDC)
        print(bcolors.OKBLUE +' |    |   |  |__/ __ \\___  \  ___/|  | \/  |   |  \        /|  |   |  \\___ \ '+bcolors.ENDC)
        print(bcolors.OKBLUE +' |____|   |____(____  / ____|\___  >__|     |___|   \__/\  / |__|___|  /____  >'+bcolors.ENDC)
        print(bcolors.OKBLUE +'                    \/\/         \/                      \/          \/     \/ '+bcolors.ENDC)

    def draw_ascii():
        print(bcolors.OKBLUE +'________                           '+bcolors.ENDC)
        print(bcolors.OKBLUE +'\______ \ _______ _____  __  _  __ '+bcolors.ENDC)
        print(bcolors.OKBLUE +' |    |  \\_  __ \\__  \ \ \/ \/ / '+bcolors.ENDC)
        print(bcolors.OKBLUE +' |    `   \|  | \/ / __ \_\     /  '+bcolors.ENDC)
        print(bcolors.OKBLUE +'/_______  /|__|   (____  / \/\_/   '+bcolors.ENDC)
        print(bcolors.OKBLUE +'        \/             \/          '+bcolors.ENDC)

    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(bcolors.OKBLUE+turn + ' will go first.'+bcolors.ENDC)

        play_game = input(bcolors.WARNING+'Are you ready to play? Enter Yes or No. '+bcolors.ENDC)

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print(player1_wins_ascii())
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print(draw_ascii())
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print(draw_ascii())
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            break


#