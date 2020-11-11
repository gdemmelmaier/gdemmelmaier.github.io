
import sequence as s
import delete_opponent as d
import win_condition as w
import moving as m
import rules as r
import json
import GameEngineGroupA as ge
import moving_third_phase as mtp
import projectse.game_manager as game_manager
game_still_going = True

start_moving = False
#board = gp.board
count_W = 9
count_B = 9
comm_part = None

def init(gm):
    global comm_part
    comm_part = gm

def playGameAI(setup=True, human="B ", bn = '',wn='', diff='1'):
    global comm_part
    global count_W
    global count_B
    global start_moving
    global game_still_going

    if setup:
        #filename = "board1.json"
        global start_moving
        global current_player
        print ("Hello human!\n I am AI bot who can play the game with you. \n I will be W in the game and you would be B and will start the game.\n")

        bName = input("What is your name human? :")

        difficulty_AI = input("Please input the difficulty level "+bName+": ")
        while (difficulty_AI not in ["0","1","2"]):
            difficulty_AI = moveOrAction_difficulty(difficulty_AI)

        wName = "AI Level " + difficulty_AI

        difficulty_AI = int(difficulty_AI)
        game_still_going = True
        start_moving = False
        count_W = 9
        count_B = 9
    else:
        bName = bn
        wName = wn
        if diff == "low":
            difficulty_AI = 0
        elif diff == "med":
            difficulty_AI = 1
        else:
            difficulty_AI = 2
        #difficulty_AI = int(diff)
    game_still_going = True
    start_moving = False
    count_W = 9
    count_B = 9

    #print (type(difficulty_AI))
    normalPlayer = human
    if human == "B ":
        AIPlayer = "W "
    else:
        AIPlayer = "B "
    turn = 0
    current_player = "B "

    board = [
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**",
    "**", "**", "**"]

    display_board(board,count_B)

    while game_still_going:

        if (current_player == AIPlayer):
          print ("\nAI is making the move")

          board_copy = board

          board,turn = moveAI(board_copy,AIPlayer,difficulty_AI,turn)

          if AIPlayer == "W ":
            if (turn < 19 and count_W > 0):
                count_W = count_W - 1
          else:
            if (turn < 19 and count_B > 0):
                count_B = count_B - 1

          display_board(board,count_W)




        if (current_player == normalPlayer):
          three_sequence = False

          position_place = handle_player(current_player, normalPlayer=="B ", wName, bName,board)
          display_board(board,count_W)
          three_sequence, curr_sequence = s.check_sequence(
              current_player, position_place, board)

          if (three_sequence == True):
              d.delete_opp_stone(current_player, board, position_place)
              display_board(board,count_W)
          turn = turn +1

        start_moving = check_remainingWB(count_W)

        flip_player()

        while start_moving:

            if (current_player == AIPlayer):
              print ("\nAI is making the move")
              board_copy = board

              board,turn = moveAI(board_copy,AIPlayer,difficulty_AI,turn)

              display_board(board,count_W)




            if (current_player == normalPlayer):

              display_board(board,count_W)
              count_current_player = 0

              for i in board:
                if (i == current_player):
                  count_current_player = count_current_player+1

              if (count_current_player < 4):
                position_move = mtp.move_stone_third_phase(current_player,board)
                three_sequence, curr_sequence = s.check_sequence(current_player, position_move, board)
                if (three_sequence == True):
                  d.delete_opp_stone(current_player, board, position_move)
                  display_board(board,count_W)
                turn = turn+1

              else:
                position_move = m.move_stone(current_player, board)

                three_sequence, curr_sequence = s.check_sequence(
                    current_player, position_move, board)

                if (three_sequence == True):
                    d.delete_opp_stone(current_player, board, position_move)
                    display_board(board,count_W)
                turn = turn +1


            winner = w.check_winning_condition(board)
            start_moving = winner is None
            #start_moving = w.check_winning_condition(board)

            flip_player()

            if(start_moving == False):

                game_still_going = False
                return winner

'''while start_moving:

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


            start_moving = w.check_winning_condition(board)

            flip_player()

            if(start_moving == False):

                game_still_going = False
                return False
'''


def moveAI(board,player,difficulty,turn):
  boardAI = [None]*24
  player = player
  difficulty = difficulty

  spiral_sequence = [0,1,2,8,9,10,16,17,18,7,15,23,19,11,3,22,21,20,14,13,12,6,5,4]
  board = board

  for i in range(len(board)):
    boardAI[spiral_sequence[i]] = board[i]

  #print (boardAI)
  for i in range(len(boardAI)):
    if (boardAI[i] == "**"):
      boardAI[i] = -1
    if (boardAI[i] == "W "):
      boardAI[i] = 1
    if (boardAI[i] == "B "):
      boardAI[i] = 0

  if (player == "W "):
    player = 1
  if (player == "B "):
    player = 0

  ##### Communication component part
  global comm_part
  board_state = game_manager.BoardState()
  board_state.set(boardAI, player, turn, difficulty)
  #boardAI, turn = comm_part.make_move_test(board_state).get()
  boardAI = comm_part.make_move_test(boardAI, player, turn, difficulty)
  turn = turn + 1
  #writeOutputFile(filename, boardAI, 1 - player, turn, difficulty)

  #ge.runUUGame(filename)

  #boardAI,turn = readInputFile(filename)
#######
  for i in range(len(boardAI)):
    board[i] = boardAI[spiral_sequence[i]]

  for i in range(len(board)):
    if (board[i] == -1):
      board[i] = "**"
    if (board[i] == 1):
      board[i] = "W "
    if (board[i] == 0):
      board[i] = "B "

  return board,turn




def readInputFile(filename):
    with open(filename) as f:
        data = json.load(f)
    # check keys in board
    #count = 0
    keys = list(data['Board'].keys())
    if len(keys) != 24:
        raise ValueError('Board must have 24 keys')
    #for x in keys:
        #if int(x) != count:
            #raise ValueError('Keys in board must have values 0 to 23 in ascending order')
    return (list(data['Board'].values()), data['Turn'])


def writeOutputFile(filename, board, player, turn, difficulty):

    data = {}
    data['Board'] = {x:y for x,y in enumerate(board,0)}
    data['Player'] = player
    data['Turn'] = turn
    data['Difficulty'] = difficulty

    b = list(map(readablePlayer, board))
    data['Visual'] = []
    data['Visual'].append({
        'A':b[0]+'-----'+b[1]+'-----'+b[2],
        'B':'|;    |    /|',
        'C':'| '+b[8]+'---'+b[9]+'---'+b[10]+' |',
        'D':'| |;  |  /| |',
        'E':'| | '+b[16]+'-'+b[17]+'-'+b[18]+' | |',
        'F':'| | |   | | |',
        'G':b[7]+'-'+b[15]+'-'+b[23]+'   '+b[19]+'-'+b[11]+'-'+b[3],
        'H':'| | |   | | |',
        'I':'| | '+b[22]+'-'+b[21]+'-'+b[20]+' | |',
        'J':'| |/  |  ;| |',
        'K':'| '+b[14]+'---'+b[13]+'---'+b[12]+' |',
        'L':'|/    |    ;|',
        'M':b[6]+'-----'+b[5]+'-----'+b[4]
    })
    data['Index map'] = []
    data['Index map'].append({
        'A':' 0------- 1------- 2',
        'B':' | ;      |      / |',
        'C':' |  8---- 9----10  |',
        'D':' |  |;    |    /|  |',
        'E':' |  | 16-17-18  |  |',
        'F':' |  | |      |  |  |',
        'G':' 7-15-23    19-11- 3',
        'H':' |  | |      |  |  |',
        'I':' |  | 22-21-20  |  |',
        'J':' |  |/    |   ; |  |',
        'K':' | 14----13----12  |',
        'L':' |/       |      ; |',
        'M':' 6------- 5------- 4'
    })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2,sort_keys=True)



def readablePlayer(player):
    dict = {
        1: 'W',
        0: 'B'

    }
    return dict.get(player, ' ')




def display_board(board,count_W):
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

    print ("W stolen: ",(9-(count_W_board+count_W)))
    print ("B stolen: ",(9-(count_B_board+count_B)))


def moveOrAction_difficulty(difficulty_AI):
    difficulty_AI = difficulty_AI
    while(difficulty_AI in ["q", "Q", "r", "R"] or
          difficulty_AI not in ["0", "1", "2"]):

        if (difficulty_AI in ["q", "Q"]):
            quit = quit_game()
            if (quit == True):
                print("AI won the match!")
                exit()

        if (difficulty_AI in ["r", "R"]):
            r.gameRules()
            difficulty_AI = input(
                "Choose between 0 to 2, or press [R] to see the rules: : ")
            continue

        if(difficulty_AI in ["q", "Q"]):
            difficulty_AI = input("Choose between 0 to 2, or press [R] to see the rules: ")

        if (difficulty_AI not in ["q", "Q", "r", "R"] and
            difficulty_AI not in [0, 1, 2]):
            difficulty_AI = input(
                "Invalid input!\n \
                Choose between 0 to 2, or press [R] to see the rules: : ")
        else:
            difficulty_AI = input("Choose between 0 to 2, or press [R] to see the rules: : ")


    return difficulty_AI

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
                "\nInvalid input!\nChoose a position from 1-24, or press [R] to see the rules: : ")
        else:
            position = input("Choose a position from 1-24, or press [R] to see the rules: : ")


    return position

# Description: Handling the inputs from the player


def handle_player(player, isBlack, wName, bName,board):
    if (player == "W "):
        print(player+"("+wName+")" + "'s turn.")
    if (player == "B "):
        print(player+"("+bName+")" + "'s turn.")


    valid = False
    while not valid:

        position = input(
            "Choose a position from 1-24, or press [R] to see the rules: ")
        global count_B, count_W, count_W_board, count_B_board

        position = moveOrAction(position, player, wName, bName)

        position = int(position) - 1

        if board[position] == "**":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player
    #if board[position] == "W ":
        #count_W = count_W - 1
        # count_W_board = count_W_board+1
    #else:
    if isBlack:
        count_B = count_B - 1
    else:
        count_W = count_W - 1
        # count_B_board = count_B_board+1

    #display_board(board)
    return position+1

def quit_game():
    areYouSure = input("Are you sure you want to quit?\n[Y]es or [N]o?\n")

    if (areYouSure == ('y' or 'Y')):
        return True
    if(areYouSure == ('n' or 'N')):
        return False


def flip_player():
    global current_player

    if current_player == "W ":
        current_player = "B "

    elif current_player == "B ":
        current_player = "W "




def check_remainingWB(count_W):
    if count_B == 0 and count_W == 0:
        return True
    else:
        return False
