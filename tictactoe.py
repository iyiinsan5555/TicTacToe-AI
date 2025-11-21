"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x_count = 0
    o_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                    o_count += 1

    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_actions.add((i,j))

    return possible_actions

def result(board, action):
    if board[action[0]][action[1]] is not None:
        raise Exception("Invalid action!")

    new_board = [row[:] for row in board]  # deep copy
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    lines = []

    # rows
    for i in range(3):
        lines.append(board[i])

    # columns
    for j in range(3):
        lines.append([board[i][j] for i in range(3)])

    # diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])

    for line in lines:
        if line[0] is not None and line[0] == line[1] == line[2]:
            return line[0]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win_or_no = winner(board) #if not None there is no winner --> tie or continuity
    possible_actions = actions(board) #if its items count is 0 then its tie otherwise continuity

    if win_or_no is not None:
        return True
    elif len(possible_actions) == 0:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if not terminal(board):
        raise "Only call utility when terminal is True"

    winner_condition = winner(board)
    if winner_condition == X:
        return 1
    elif winner_condition == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None

    turn = player(board)

    # MAX player (X)
    if turn == X:
        best_value = -math.inf
        best_move = None

        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action

        return best_move

    # MIN player (O)
    else:
        best_value = math.inf
        best_move = None

        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action

        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
