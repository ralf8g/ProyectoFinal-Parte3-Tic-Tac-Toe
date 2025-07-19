import numpy as np
from config import BOARD_ROWS, BOARD_COLS

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def mark_square(row, col, player):
    board[row][col] = player

def is_empty(row, col):
    return board[row][col] == 0

def is_full():
    return not np.any(board == 0)

def check_win(player):
    for i in range(BOARD_ROWS):
        if all(board[i, :] == player) or all(board[:, i] == player):
            return True
    if board[0, 0] == board[1, 1] == board[2, 2] == player:
        return True
    if board[0, 2] == board[1, 1] == board[2, 0] == player:
        return True
    return False

def reset_board():
    board[:] = 0
