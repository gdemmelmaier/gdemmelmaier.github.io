import sequence as s
import delete_opponent as d
import win_condition as w
import moving as m
import rules as r
import playAIGame as ai
import moving_third_phase as mtp
board = [
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**"
]

# Description: All possible ways to get three in a row
three_insequence = {1: [1, 2, 3],
                    2: [4, 5, 6],
                    3: [7, 8, 9],
                    4: [10, 11, 12],
                    5: [13, 14, 15],
                    6: [16, 17, 18],
                    7: [19, 20, 21],
                    8: [22, 23, 24],
                    9: [1, 10, 22], 10: [4, 11, 19],
                    11: [7, 12, 16], 12: [2, 5, 8],
                    13: [17, 20, 23], 14: [9, 13, 18],
                    15: [6, 14, 21], 16: [3, 15, 24],
                    17: [1, 4, 7], 18: [3, 6, 9],
                    19: [22, 19, 16], 20: [24, 21, 18]}


linked_nodes = {1: [2, 10, 4], 2: [3, 5], 3: [2, 15, 6], 4: [5, 11, 7, 1], 5: [2, 4, 6, 8],
                6: [5, 14, 3, 9], 7: [8, 12, 4], 8: [5, 7, 9], 9: [8, 13, 6], 10: [1, 11, 22],
                11: [4, 10, 12, 19], 12: [7, 11, 16], 13: [9, 14, 18],
                14: [6, 13, 15, 21], 15: [3, 14, 24], 16: [12, 17, 19],
                17: [16, 18, 20], 18: [13, 17, 21], 19: [11, 20, 22, 16],
                20: [17, 19, 21, 23], 21: [14, 20, 18, 24], 22: [10, 23, 19], 23: [20, 22, 24],
                24: [15, 23, 21]}

welcomeMsg = "Welcome to the UU-game\n"


game_still_going = True

start_moving = False

count_W = 9
count_B = 9

count_W_board = 0
count_B_board = 0
winner = None

used_sequenceW = []
used_sequenceB = []

current_player = "W "

def initialize():
    global board, game_still_going, start_moving, count_B, count_W, count_W_board, count_B_board,winner, used_sequenceB, used_sequenceW, current_player
    board = [
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**"
    ]
    game_still_going = True
    start_moving = False
    count_W = 9
    count_B = 9
    count_W_board = 0
    count_B_board = 0
    winner = None
    used_sequenceW = []
    used_sequenceB = []
    current_player = "B "


# Description: Controls the flow of the game
# Play game is only Human Vs Human
def play_game(config, wN='', bN='', start=''):
    global start_moving
    global current_player
    if (config == False):
        wName, bName, whoStart = start_game()
    else:
        wName = wN
        bName = bN
        whoStart = start
    if (whoStart == "B" or whoStart == "o"):
        current_player = "B "
    if(wName == 0 and bName == 0):
        return None

    display_board()
    global game_still_going
    while game_still_going:
        three_sequence = False
        position_place = handle_player(current_player, wName, bName)

        three_sequence, curr_sequence = s.check_sequence(
            current_player, position_place, board)

        if (three_sequence == True):
            d.delete_opp_stone(current_player, board, position_place)
            display_board()

        start_moving = check_remainingWB()

        flip_player()

        while start_moving:

            display_board()

            count_current_player = 0

            for i in board:
              if (i == current_player):
                count_current_player = count_current_player+1


            if (count_current_player < 4):
              position_move = mtp.move_stone_third_phase(current_player,board)
              three_sequence, curr_sequence = s.check_sequence(current_player, position_move, board)
              if (three_sequence == True):
                d.delete_opp_stone(current_player, board, position_move)
                display_board()


            else:

              position_move = m.move_stone(current_player, board)

              three_sequence, curr_sequence = s.check_sequence(current_player, position_move, board)

              if (three_sequence == True):
                  d.delete_opp_stone(current_player, board, position_move)
                  display_board()

            winner = w.check_winning_condition(board)
            start_moving = winner is None
            #start_moving = w.check_winning_condition(board)

            flip_player()

            if(start_moving == False):

                game_still_going = False
                return winner


# Description: Writes the game board to standard output
def display_board():
    count_W_board = 0
    count_B_board = 0
    print("\n")
    print(board[0] + " -- -- " + board[1] + " -- -- " +
          board[2]+"     "+"01 -- -- 02 -- -- 03")
    print("| \       |      / |"+"     "+"| \       |      / |")
    print("|  " + board[3] + " -- " + board[4] + " -- " +
          board[5] + "  | "+"    "+"|  04 -- 05 -- 06  |")
    print("|  | \    |   / |  |"+"     "+"|  | \    |   / |  |")
    print("|  |  " + board[6] + "-" + board[7] + "-" +
          board[8] + "  |  |"+"     "+"|  |  07-08-09  |  |")
    print("|  |  |      |  |  |"+"     "+"|  |  |      |  |  |")
    print(board[9] + "-" + board[10] + "-" + board[11] + "    " + board[12] +
          "-" + board[13] + "-" + board[14]+"     "+"10-11-12    13-14-15")
    print("|  |  |      |  |  |"+"     "+"|  |  |      |  |  |")
    print("|  |  " + board[15] + "-" + board[16] + "-" +
          board[17] + "  |  |"+"     "+"|  |  16-17-18  |  |")
    print("|  | /    |   \ |  |"+"     "+"|  | /    |   \ |  |")
    print("|  " + board[18] + " -- " + board[19] + " -- " +
          board[20] + "  | "+"    "+"|  19 -- 20 -- 21  |")
    print("| /       |      \ |"+"     "+"| /       |      \ |")
    print(board[21] + " -- -- " + board[22] + " -- -- " +
          board[23]+"     "+"22 -- -- 23 -- -- 24")
    print("\n")

    print("Remaining W: ", count_W)

    print("Remaining B: ", count_B)

    for i in board:
        if (i == "W "):
            count_W_board = count_W_board + 1
        if (i == "B "):
            count_B_board = count_B_board + 1

    print("W on board: ", count_W_board)
    print("B on board: ", count_B_board)
    print("W stolen: ", (9 - (count_W_board + count_W)))
    print("B stolen: ", (9 - (count_B_board + count_B)))


# Checks if input is a valid move or an action (quit/rules)
def moveOrAction(position, player, wName, bName):
    while(position in ["q", "Q", "r", "R"] or
          position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                          "17", "18", "19", "20", "21", "22", "23", "24"]):

        if (position in ["q", "Q"]):
            quit = quit_game()
            if (quit == True):
                if (player == "W "):
                    print("B "+"("+bName+")"+" won the match!")
                    exit()
                else:
                    print("W "+"("+wName+")"+" won the match!")
                    exit()

        if (position in ["r", "R"]):
            r.gameRules()
            position = input(
                "Choose a position from 1-24, or press [R] to see the rules: : ")
            continue

        if(position in ["q", "Q"]):
            position = input("Choose a position from 1-24, or press [R] to see the rules: ")

        if (position not in ["q", "Q", "r", "R"] and
            position not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                           17, 18, 19, 20, 21, 22, 23, 24]):
            position = input(
                "Invalid input!\n \
                Choose a position from 1-24, or press [R] to see the rules: : ")
        else:
            position = input("Choose a position from 1-24, or press [R] to see the rules: : ")


    return position

# Description: Handling the inputs from the player


def handle_player(player, wName, bName):
    if (player == "W "):
        print(player+"("+wName+")" + "'s turn.")
    if (player == "B "):
        print(player+"("+bName+")" + "'s turn.")

    position = input(
        "Choose a position from 1-24, or press [R] to see the rules: ")
    global count_W, count_B, count_W_board, count_B_board

    valid = False
    while not valid:

        position = moveOrAction(position, player, wName, bName)

        position = int(position) - 1

        if board[position] == "**":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player
    if board[position] == "W ":
        count_W = count_W - 1
        # count_W_board = count_W_board+1
    else:
        count_B = count_B - 1
        # count_B_board = count_B_board+1

    display_board()
    return position+1


# Description: checking the number of W or B outside the board. Decides for starting the moving phase
def check_remainingWB():
    if count_B == 0 and count_W == 0:
        return True
    else:
        return False

# Description: Flips who's turn it is


def flip_player():
    global current_player

    if current_player == "W ":
        current_player = "B "

    elif current_player == "B ":
        current_player = "W "

# Description: Writes 1 vs 1 menu to standard output
# and starts picked mode


def start_game():
    print("Modes for 1 vs 1 game:")
    print("Modes:\n[A] AI vs Player\n[P] Player vs Player\n[E] Exit")
    print("Press [R] to see the rules")
    while(True):
        choice_game = input("Please select mode: ")
        if(choice_game in ["r", "R"]):
            r.gameRules()
        if (choice_game == "A" or choice_game == "a"):
            print("AI")
            ai.playGameAI()
        if (choice_game == "P" or choice_game == "p"):
            print(welcomeMsg)
            wName = input("Name of player W: ")
            bName = input("Name of player B: ")
            while (True):
                whoStart = input("Who is the starting player? [W]/[B]")
                if (whoStart == "W" or whoStart == "w" or whoStart == "B" or whoStart == "b"):
                    break
            return wName, bName, whoStart
        if(choice_game == "E" or choice_game == "e"):
            # main.main_menu_func()
            return 0, 0, 0
        #print("Invalid input!")
        print('\n')
        print("Modes for 1 vs 1 game:")
        print("Modes:\n[A] AI vs Player\n[P] Player vs Player\n[E] Exit")
        print("Press [R] to see the rules")

# Description: Checks if you really want to quit
def quit_game():
    areYouSure = input("Are you sure you want to quit?\n[Y]es or [N]o?\n")

    if (areYouSure == ('y' or 'Y')):
        return True
    if(areYouSure == ('n' or 'N')):
        return False
