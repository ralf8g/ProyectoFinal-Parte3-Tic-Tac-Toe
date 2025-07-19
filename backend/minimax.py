from backend.board import board, mark_square, is_empty, check_win, is_full
from config import BOARD_ROWS, BOARD_COLS

def minimax(current_board, depth, is_maximizing, alpha, beta):
    if check_win(2):
        return float('inf') - depth
    elif check_win(1):
        return float('-inf') + depth
    elif is_full():
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if current_board[row][col] == 0:
                    current_board[row][col] = 2
                    eval = minimax(current_board, depth + 1, False, alpha, beta)
                    current_board[row][col] = 0
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if current_board[row][col] == 0:
                    current_board[row][col] = 1
                    eval = minimax(current_board, depth + 1, True, alpha, beta)
                    current_board[row][col] = 0
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return min_eval

def best_move_for_ai():
    best_score = float('-inf')
    move = None
    alpha = float('-inf')
    beta = float('inf')

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False, alpha, beta)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
                alpha = max(alpha, best_score)

    if move:
        mark_square(move[0], move[1], 2)
        return True
    return False
