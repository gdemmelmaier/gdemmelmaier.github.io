
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

# Description: Function for checking the sequence or triplet


def check_sequence(player, position, board):
    if (player == "W "):
        for i in three_insequence:
            if position in three_insequence[i]:
                if (board[three_insequence[i][0] - 1] == player and board[three_insequence[i][1] - 1] == player and
                        board[three_insequence[i][2] - 1] == player):
                    return True, [three_insequence[i][0] - 1, three_insequence[i][1] - 1, three_insequence[i][2] - 1]

        return False, [-1, -1, -1]

    if (player == "B "):
        for i in three_insequence:
            if position in three_insequence[i]:
                if (board[three_insequence[i][0] - 1] == player and board[three_insequence[i][1] - 1] == player and
                        board[three_insequence[i][2] - 1] == player):
                    return True, [three_insequence[i][0] - 1, three_insequence[i][1] - 1, three_insequence[i][2] - 1]

        return False, [-1, -1, -1]
