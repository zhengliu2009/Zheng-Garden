#!/usr/bin/python3
import random

def main():
    # Basic game board initialization.
    game_board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    # Call to display_board. Comment this out once
    # you have it working.
    #display_board(game_board)
    
    # Initialize the game state by determining
    # who has what piece and whose turn it will
    # be to start the game.
    game_over = False
    
    if random.randint(0, 1) == 0:
        print('Computer has X and will go first...')
        user = 'O'
        computer = 'X'
        whose_turn = 'computer'
    else:
        print('User has X and will go first...')
        user = 'X'
        computer = 'O'
        whose_turn = 'user'
        
    # We'll stay in this loop until the game is over due to someone winning
    # or until it's declared a draw.
    while not game_over:
        if whose_turn == 'user':  # Human player's turn
            print('It\'s your turn...')
            get_user_move(game_board, user)
            display_board(game_board)
            if has_player_won(game_board, user):
                print('Congrats, you won!')
                game_over = True
            else:
                whose_turn = 'computer'
        else:  # Computer's turn
            print('Computer\'s turn...')
            get_computer_move(game_board, computer)
            display_board(game_board)
            if has_player_won(game_board, computer):
                print('Sorry, the computer won :-(')
                game_over = True
            else:
                whose_turn = 'user'
        
        # Check to see if the game is over without a winner
        if not game_over and is_draw(game_board):
            print('Lame, it\'s a draw :-\.')
            game_over = True
        print('===============================================================')
        
    print('Thanks for playing!')
   
 
def display_board(game_board):
    """This function prints the game board for the user to see its state."""
    for r in range(len(game_board)):
        for c in range(len(game_board[r])):
            # Use an empty space, or the player symbol in the placeholder.
            symbol = ' '
            if game_board[r][c]:
                symbol = game_board[r][c]
            print('_{}_'.format(symbol), end='')
            # Tuples and in are a quick way of checking
            # if a value is one of a possible set of
            # values.
            if c in (0, 1):
                print('|', end='')
            else:
                print('')
                
# for r in gb:
#      for c in r:
#          value = c
 #             if not value:
 #                 value=''
  #            print('_{}_'.format(value)
  
def get_user_move(game_board, symbol):
    """Ask the user for their row and column move and set the game_board with
       their symbol."""
    row = int(input('What row do you want to play? (0-2) '))
    col = int(input('What column do you want to play? (0-2) '))
    while not is_legal_move(game_board, row, col):
        print('{},{} is not a legal move'.format(row, col))
        row = int(input('What row do you want to play? (0-2) '))
        col = int(input('What column do you want to play? (0-2) '))
    game_board[row][col] = symbol
    
    
def get_computer_move(game_board, symbol):
    """Generate random number coordinates for the computer to place their
    symbol."""
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while not is_legal_move(game_board, row, col):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    game_board[row][col] = symbol
    

def is_legal_move(game_board, row, col):
    """Check to see if the row and col provided are within the boundaries of 
       the board and if the space is unoccupied."""
    if row < 0 or row > 2:
        return False
    if col < 0 or col > 2:
        return False
    # Remember, any non-empty string evaluates to True
    # in the context of an if statement
    if game_board[row][col]:
        return False
        
    return True
    
def is_draw(game_board):
    """Determine if a game is a draw by checking each space. Once we find at
       least one empty spot, we can return False since it's a playable spot."""
    for r in range(len(game_board)):
        for c in range(len(game_board[r])):
            # An empty string evaluates to False inside
            # the context of an if statement
            if not game_board[r][c]:
                return False
    return True

def has_player_won(game_board, symbol):
    """Check to see if the given symbol has won the game in any of the possible
       ways."""
    
    # Remember, with sequences the multiplication
    # operator repeats the value so 'X' * 3 == 'XXX'
    winner_sequence = symbol * 3 
    
    # Check for horizontal wins
    for r in range(len(game_board)):
        row_symbols = ''
        for c in range(len(game_board[r])):
            row_symbols += game_board[r][c]
        if row_symbols == winner_sequence:
            return True
        
    # Check for vertical wins
    for c in range(len(game_board[0])):
        col_symbols = ''
        for r in range(len(game_board)):
            col_symbols += game_board[r][c]
        if col_symbols == winner_sequence:
            return True
            
    # Check for the two diagonal wins
    # Note this will only work on a square board!
    diag_symbols = ''
    anti_diag_symbols = ''
    for rc in range(len(game_board)):
        diag_symbols += game_board[rc][rc]
        anti_diag_symbols += game_board[rc][len(game_board) - 1 - rc]
    if winner_sequence in (diag_symbols, anti_diag_symbols):
        return True
    
    # If we got here, nobody won yet
    return False
    
main()
