from minimax import next_move
from board import *
from move import *

def input_yes_no(question : str) -> str:
    """Returns output, when the input is y or n, """
    output = ""
    while output != "y" and output != "n":
        output = input(question)

    return output

def input_numeric_in_range(question : str, start : int, end : int) -> str:
    """Returns the numeric output, when the input is in range"""
    output = start - 1
    while output < start or output > end:
        output = int(input(question))
    
    return output

def get_ascii_indexes(b_ascii: str) -> list[int]:
  """Returns the list of indexes where the character @ appears in b_ascii"""
  b_ascii_indexes = []
  for i in range(len(b_ascii)):
      if b_ascii[i] == '@':
          b_ascii_indexes.append(i)
  return b_ascii_indexes

def draw_board(b : Board, b_ascii : str, b_ascii_indexes : list[int]) -> None:
    """Draws the ascii board"""
    for i in range(25):
        b_ascii = b_ascii[0:b_ascii_indexes[i]] + "_" + b_ascii[b_ascii_indexes[i] + 1 : len(b_ascii)]
    for i in black(b):
        b_ascii = b_ascii[0:b_ascii_indexes[i - 1]] + "B" + b_ascii[b_ascii_indexes[i - 1] + 1 : len(b_ascii)]
    for i in white(b):
        b_ascii = b_ascii[0:b_ascii_indexes[i - 1]] + "W" + b_ascii[b_ascii_indexes[i - 1] + 1 : len(b_ascii)]

    print(b_ascii)


def turn(b : Board, difficulty : int, all_moves : list[Move]) -> Move:
    """Handles the current players turn, for humans and the computer"""
    move_index = -1
    move_choice = None 

    is_white_playing = white_plays(b)

    if (is_white_playing and is_player_white_human == "n") or (is_white_playing == False and is_player_black_human == "n"):
        move_choice = next_move(b, difficulty)
    else:
        move_index = input_numeric_in_range("\nChoose your move : ", 0, len(all_moves) - 1)
        move_choice = all_moves[move_index]
    
    move(move_choice,b)
    return move_choice


def print_game_result(b : Board) -> None:
    """Prints the final game result"""

    print(" ")
    if white_plays(b) and white(b) == []:
        print("The game is over","Black is the winner")
    elif not white_plays(b) and black(b) == []:
        print('The game is over','White is the winner')
    else:
        print('This game is a draw')


def configure_game() -> Board:
    """Configures initialization variables for the game"""
    print("\n-------------------------")
    print("Welcome to alquerque")
    print("W is White")
    print("B is Black\n")

    global is_player_white_human, is_player_black_human, difficulty

    is_player_white_human = input_yes_no("Is player white human? (y/n) : ")
    is_player_black_human = input_yes_no("Is player black human? (y/n) : ")

    if is_player_white_human == "n" or is_player_black_human == "n":
        difficulty = input_numeric_in_range("Choose difficulty between 1-7 : ", 1, 7)


def finalize_game(b: Board, b_ascii : str, b_ascii_indexes : list[int]) -> bool:
    """Prints the final state of the game, and asks of the player wants to play again."""
    print("\n-------------------------")
    print("\nFinal Board")
    draw_board(b, b_ascii, b_ascii_indexes)

    print_game_result(b)

    if(input("\nDo you want to play again? (y/n) : ") == "n"):
        return False

    return True

def game_loop(b : Board, b_ascii : str, b_ascii_indexes : list[int]) -> None:
    """Loops trough each state of the game, until the game is over."""
    while (is_game_over(b) == False):

      print("\n-------------------------")

      draw_board(b, b_ascii, b_ascii_indexes)

      if white_plays(b):
          print("\nWhites Turn!\n")
      else:
          print("\nBlacks Turn!\n")

      all_moves = legal_moves(b)

      print("Available moves")
      index = 0
      for choice in all_moves:
          print("Move",index,": from",source(choice),"to", target(choice))
          index += 1
      
      move_choice = turn(b, difficulty, all_moves)

      if not white_plays(b):
          print("\nWhite moved from", source(move_choice), "to", target(move_choice))
      else:
          print("\nBlack moved from", source(move_choice), "to", target(move_choice))


def main(b_ascii : str, b_ascii_indexes : list[int]) -> None:
    """The main entry point of the program."""
    play_again = True
    board : Board

    while play_again == True:
        
        configure_game()
        board = make_board()
        draw_board(board, b_ascii, b_ascii_indexes)
        game_loop(board, b_ascii, b_ascii_indexes)
        play_again = finalize_game(board, b_ascii, b_ascii_indexes)

    print("Thanks for playing!")

board_ascii = """
 _____     _____     _____     _____     _____ 
|  1  |___|  2  |___|  3  |___|  4  |___|  5  |
|__@__|   |__@__|   |__@__|   |__@__|   |__@__|
   |   \     |     /   |   \     |     /   |   
 __|__   \ __|__ /   __|__   \ __|__ /   __|__ 
|  6  |___|  7  |___|  8  |___|  9  |___| 10  |
|__@__|   |__@__|   |__@__|   |__@__|   |__@__|
   |     /   |   \     |     /   |   \     |   
 __|__ /   __|__   \ __|__ /   __|__   \ __|__ 
| 11  |___| 12  |___| 13  |___| 14  |___| 15  |
|__@__|   |__@__|   |__@__|   |__@__|   |__@__|
   |   \     |     /   |   \     |     /   |   
 __|__   \ __|__ /   __|__   \ __|__ /   __|__ 
| 16  |___| 17  |___| 18  |___| 19  |___| 20  |
|__@__|   |__@__|   |__@__|   |__@__|   |__@__|
   |     /   |   \     |     /   |   \     |   
 __|__ /   __|__   \ __|__ /   __|__   \ __|__ 
| 21  |___| 22  |___| 23  |___| 24  |___| 25  |
|__@__|   |__@__|   |__@__|   |__@__|   |__@__|"""
board_ascii_indexes = get_ascii_indexes(board_ascii)
is_player_white_human = "" 
is_player_black_human = "" 
difficulty = -1

main(board_ascii, board_ascii_indexes)