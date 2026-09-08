from board import Board, legal_moves, make_board, copy, move, white_plays, white, black, is_game_over
from move import Move, source, target
import random

def evaluate_state(m : Move, board_previous : Board, board_current : Board, depth : int, add_direction : int) -> int:
    """Evaluates the current state of the board, by computing the heuristics"""
    resulting_value = 0
    peice_taken_cost = 0
    total_pieces = len(white(board_current)) + len(black(board_current))
    total_pieces_parent = len(white(board_previous)) + len(black(board_previous))

    if add_direction == 1:
        peice_taken_cost = 2
    elif add_direction == -1:
        peice_taken_cost = -3
    
    if total_pieces < total_pieces_parent:
        if is_game_over(board_current):
            resulting_value += add_direction * 20 * (depth + 1)
        else:
            resulting_value += peice_taken_cost

    target_pos = target(m)

    if target_pos == 1 or target_pos == 5 or target_pos == 21 or target_pos == 25:
        resulting_value += peice_taken_cost + (-1 * add_direction)

    return resulting_value


def minimax(m : Move, board_previous : Board, depth : int, alpha : int, beta : int, maximizing : bool, value : int, add_direction : int) -> int:
    """Peforms the minimax algorithm"""
    board_current = copy(board_previous)
    move(m, board_current)
    all_moves = legal_moves(board_current)

    value += evaluate_state(m, board_previous, board_current, depth, add_direction)

    if depth == 0 or all_moves == []:
        return value

    resulting_value = 0
    iterate = True
    iteration = 0

    if maximizing:
        resulting_value = -1000000
        while iterate:
            score = minimax(all_moves[iteration], board_current, depth - 1, alpha, beta, not maximizing, value, add_direction * -1)
            if score > resulting_value:
                resulting_value = score
                alpha = resulting_value

            if beta <= alpha:
                iterate = False

            iteration += 1 
            if iteration == len(all_moves):
                iterate = False
    else:
        resulting_value = 1000000
        while iterate:
            score = minimax(all_moves[iteration], board_current, depth - 1, alpha, beta, not maximizing, value, add_direction * -1)
            if score < resulting_value:
                resulting_value = score
                beta = resulting_value

            if beta <= alpha:
                iterate = False

            iteration += 1 
            if iteration == len(all_moves):
                iterate = False

    return resulting_value


def next_move(b: Board, n: int = 3) -> Move:
    """Returns the next move for the autoplayer."""

    all_moves = legal_moves(b)

    score_final = 0
    all_scores = []
    final_moves = []
    first_time = True

    for a_move in all_moves:
        score = minimax(a_move, b, n, -1000000 , 1000000, False, 0, 1)
        all_scores.append(score)
        if score > score_final or first_time:
            score_final = score
            first_time = False

    for i in range(len(all_moves)):
        if all_scores[i] == score_final:
            final_moves.append(all_moves[i])

    random_index = random.randrange(0, len(final_moves))
    return final_moves[random_index]