from move import *

Board = list[int]

empty_space = 0
white_piece = 1
black_piece = 2

def make_board() -> Board:
    """ Creates a new board, with the pieces at their starting positions. """

    board = [x for x in range(26)]

    for i in range(26):
        if i == 0:
            board[i] = white_piece
        elif i < 13:
            board[i] = black_piece
        elif i == 13:
            board[i] = empty_space
        else:
            board[i] = white_piece

    return board


def white_plays(b : Board) -> bool:
    """ Returns whether it's whites turn or not. """

    if b[0] == white_piece:
        return True
    
    return False


def white(b : Board) -> list[int]:
    """ Return a list with the indexes of whites pieces. """

    white_list = []

    for i in range(1,26):
        if b[i] == white_piece:
            white_list.append(i)
  
    return white_list


def black(b : Board) -> list[int]:
    """ Return a list with the indexes of blacks pieces. """

    black_list = []
    for i in range(1,26):
        if b[i] == black_piece:
            black_list.append(i)

    return black_list



def is_legal(m : Move, b : Board) -> bool:
    """ Checks if the Move m, on the Board b, is a legal move. """

    move_src = source(m)
    move_trg = target(m)

    if b[move_trg] != empty_space:
        return False

    delta = move_trg - move_src

    player_piece = white_piece
    opponent_piece = black_piece

    if white_plays(b) == False:
        player_piece = black_piece
        opponent_piece  = white_piece

    if b[move_src] != player_piece:
        return False

    surrounding_moves = get_surrounding_moves(move_src)

    for i in surrounding_moves:

        if i == move_src + delta / 2 and is_space_occupied(b, m) == False:
            if b[i] == opponent_piece:
                return True

        if move_trg == i and is_space_occupied(b, m) == False:
            if white_plays(b) and delta < -1:
                return True
            elif white_plays(b) == False and delta > 1:
                return True

    return False


def is_space_occupied(b : Board, m : Move) -> bool:
    """ Checks if the targeted space is occupied. """
    if b[m.trg] != empty_space:
        return True

    return False  


def get_surrounding_moves(src : int) -> list[int]:
    """ Returns a list with the surrounding 1 space moves.

    >>> get_surrounding_moves(13)
    [8, 18, 7, 17, 12, 9, 19, 14]
    >>> get_surrounding_moves(12)
    [7, 17, 11, 13]
    """

    moves_result = []

    row = (src - 1) // 5
    col = (src - 1) % 5

    # Diagonals only exist on squares where row + col is even
    has_diagonals = (row + col) % 2 == 0

    if row > 0:
        moves_result.append(src - 5)

    if row < 4:
        moves_result.append(src + 5)

    if col > 0:
        if has_diagonals:
            if row > 0:
                moves_result.append(src - 6)
            if row < 4:
                moves_result.append(src + 4)
        moves_result.append(src - 1)

    if col < 4:
        if has_diagonals:
            if row > 0:
                moves_result.append(src - 4)
            if row < 4:
                moves_result.append(src + 6)
        moves_result.append(src + 1)

    return moves_result

def legal_moves(b : Board) -> list[Move]:
    """Returns a list with all the legal moves."""

    moves_result = []
    list_pieces = []

    if white_plays(b):
        list_pieces = white(b)
    else:
        list_pieces = black(b)

    for i in list_pieces:

        src_y = int((i - 1) / 5)
        src_x = i - 1 - src_y * 5

        for y in range(src_y - 2, src_y + 3):
            for x in range(src_x - 2, src_x + 3):

                if y >= 0 and x >= 0 and y <= 4 and x <= 4:
                    index = x + y * 5 + 1
                    new_move = make_move(i,index)
                    if is_legal(new_move, b):
                        moves_result.append(new_move)

    return moves_result


def move(m : Move, b : Board) -> None:
    """ Executes the current players move, and simulates the board accordingly. """

    if is_legal(m, b):
        b[m.trg] = b[m.src]
        b[m.src] = empty_space

        delta = m.trg - m.src

        if delta == -12 or delta == -8 or delta == 2 or delta == -2 or delta == 12 or delta == 8 or delta == 10 or delta == -10:
            b[m.src + int(delta / 2)] = 0

        if white_plays(b):
            b[0] = black_piece
        elif white_plays(b) == False:
            b[0] = white_piece

def is_game_over(b : Board) -> bool:
    """ Checks if the game is over. """
    if white(b) == [] or black(b) == [] or legal_moves(b) == []:
        return True

    return False


def copy(b : Board) -> Board:
    """ Makes and returns a copy of the given board. """
    return [x for x in b]    