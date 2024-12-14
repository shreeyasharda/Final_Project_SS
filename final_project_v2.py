import numpy as np
import itertools

# THESE ARE THE MAIN GLOBAL VARIABLES I USED
game_over = False
rows_global = 6
columns_global = 7
myCol_list_global = list(range(0, columns_global))
myRow_list_global = list(range(0, rows_global))
player = itertools.cycle([1, 2])
connect_value_global = 4
max_depth = 3  # This is the depth limit for the algorithm (we can test out different multiple max depths )

# FIRST - get a game board created 
def make_board(rows: int, columns: int):
    return np.full((rows, columns), 'X') # instead of np.full, you can use np.shape()

# Look for a win within the game board which can happen in 4 different ways: 

def find_win(connect_val: int, board, player_val):
    
    # With (columns_global - connect_val + 1), you want to find the number of  entry points 
    myNewRange = range(columns_global - connect_val + 1)
    
    # For this section: I used the following video to help with my understanding: 
        # https://www.youtube.com/watch?v=UYgyRArKDEs&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&index=2
    
    # HORIZONTAL CHECK
    for row in range(rows_global):
        for col in myNewRange:
            window = board[row, col: col + connect_val]
            if all(cell == player_val for cell in window):
                return True

    # VERTICAL CHECK
    for col in range(columns_global):
        for row in range(rows_global - connect_val + 1):
            window = board[row:row + connect_val, col]
            if all(cell == player_val for cell in window):
                return True

    # RIGHT LEANING DIAGONAL
    for row in range(rows_global - connect_val + 1):
        for col in myNewRange:
            window = [board[row + i][col + i] for i in range(connect_val)]
            if all(cell == player_val for cell in window):
                return True

    # LEFT LEANING DIAGONAL
    for row in range(connect_val - 1, rows_global):
        for col in myNewRange:
            window = [board[row - i][col + i] for i in range(connect_val)]
            if all(cell == player_val for cell in window):
                return True

    return False

# WHAT IS THE NEXT AVAILABLE ROW THAT IS NOT ALREADY MARKED (this needs to be the immediate next row and not user input 
# because that will invalidate the rules of the connect 4 game

def get_next_row(columnVal, board):
    for row in range(rows_global):
        if board[row][columnVal] == 'X':
            return row
    return None

# MAKE SURE THE chosen column is a valid location (it is within the boundaries of the rows) 
def location_check(board, columnVal):
    return board[rows_global - 1][columnVal] == 'X'

# Mark the board with the pieces as they are selected 
def mark_board_me_me(player_pos, board, rowVal, colVal):
    board[rowVal][colVal] = player_pos


def evaluate_board(board, player_val):
    opponent_val = 2 if player_val == 1 else 1
    score = 0

    myNewRange = range(columns_global - connect_value_global + 1)
    myNewRange_row = range(rows_global - connect_value_global + 1)

    for row in range(rows_global):
        for col in myNewRange:
            window = board[row, col:col + connect_value_global]
            score += evaluate_window(window, player_val, opponent_val)

    for col in range(columns_global):
        for row in myNewRange_row:
            window = board[row:row + connect_value_global, col]
            score = score + evaluate_window(window, player_val, opponent_val)

    for row in myNewRange_row:
        for col in myNewRange:
            window = [board[row + i][col + i] for i in range(connect_value_global)]
            score = score + evaluate_window(window, player_val, opponent_val)

    for row in range(connect_value_global - 1, rows_global):
        for col in myNewRange:
            window = [board[row - i][col + i] for i in range(connect_value_global)]
            score = score + evaluate_window(window, player_val, opponent_val)

    return score

def evaluate_window(window, player_val, opponent_val):
    score = 0
    player_count = list(window).count(player_val)
    opponent_count = list(window).count(opponent_val)
    empty_count = list(window).count('X')

    if player_count == len(window):  
        score = score + 100
    elif player_count == len(window) - 1 and empty_count == 1:  
        score = score + 10
    elif player_count == len(window) - 2 and empty_count == 2:  
        score = score + 5

    if opponent_count == len(window) - 1 and empty_count == 1:  
        score = score - 8

    return score

# THIS IS THE Minimax algorithm with alpha-beta pruning and depth limit

def minimax(board, depth, alpha, beta, maximizing_player, player_val):
    
    # STEP 1 - Make sure you have valid locations
    valid_locations = [col for col in range(columns_global) if location_check(board, col)]
    
    is_terminal = True if find_win(connect_value_global, board, 1) else False
    is_terminal = True if find_win(connect_value_global, board, 2) else False
    is_terminal = True if len(valid_locations) == 0 else False

    if depth == 0 or is_terminal == True:
        
        if is_terminal == True:
            if find_win(connect_value_global, board, player_val):
                return (None, 100000)
            elif find_win(connect_value_global, board, 2 if player_val == 1 else 1):
                return (None, -1) # I set a negative value because the player has not won yet
            else:
                return (None, 0)
        else:
            return (None, evaluate_board(board, player_val))

    if maximizing_player:
        value = -np.inf
        column = np.random.choice(valid_locations) 
        
        for col in valid_locations:
            
            if col != 0:
                
                row = get_next_row(col, board)
                
                temp_board = board.copy() # This is creating a shallow copy og the game board to use in mark board
                
                mark_board_me(player_val, temp_board, row, col) # This is getting a new 
                
                new_score = minimax(temp_board, depth - 1, alpha, beta, False, player_val)[1]
                
                if new_score > value:
                    
                    value = new_score
                    
                    column = col
                    
                alpha = max(alpha, value)
                
                if alpha >= beta: # Make sure to check if alpha >= beta before breaking (in order to break)
                    
                    break
                
        return column, value
    
    else:
        value = np.inf
        
        column = np.random.choice(valid_locations)
        
        for col in valid_locations:
                
            row = get_next_row(col, board)
            temp_board = board.copy() # This makes a shallow copy of the board
            mark_board_me(2 if player_val == 1 else 1, temp_board, row, col)
            
            new_score = minimax(temp_board, depth - 1, alpha, beta, True, player_val)[1]
            
            if new_score < value:
                
                value = new_score
                column = col
                
            beta = min(beta, value)
            
            if alpha >= beta:
                break
        return column, value

# This is the game loop to conduct the game 
game_board = make_board(rows_global, columns_global)
output_logs = [] # This is an empty list that I will append to towards the bottom of the program

for output in player:
    valid_columns = [c for c in range(columns_global) if location_check(game_board, c)]
    if not valid_columns:
        output_logs.append("There are no more left. It's better to restart the game as this is a tie!")
        game_over = True
        break

    if output == 1:
        col, _ = minimax(game_board, max_depth, -np.inf, np.inf, True, 1)
        
        if location_check(game_board, col):
            
            myRow = get_next_row(col, game_board)
            
            mark_board_me(output, game_board, myRow, col)
            
            if find_win(connect_value_global, game_board, output):
                
                output_logs.append(f"This Player : {output} wins!")
                
                game_over = True
                
                break
            else:
                output_logs.append(f"Player {output} does not win.")
    elif output == 2:
        
        col = np.random.choice(valid_columns)
        
        if location_check(game_board, col):
            
            myRow = get_next_row(col, game_board)
            
            mark_board_me(output, game_board, myRow, col)
            
            if find_win(connect_value_global, game_board, output):
                
                output_logs.append(f"Player {output} wins!")
                
                game_over = True
                
                break
            
            else:
                
                output_logs.append(f"Player {output} does not win.")
                
    output_logs.append(np.flip(game_board, 0).tolist())

# NOTE - I am writing to a file so that we can track the results of each trial game (so I can plug them to the repo)
# Make sure the file path variable works here 
log_file_path = '/Users/shreeyasharda/Documents/CS6511_AI/Final_Project/new_file.txt'

with open(log_file_path, "w") as log_file:
    
    #log_file.write(connect_value_global + "\n")
    
    for index, x in enumerate(output_logs):
        
        if isinstance(x, list):  
            
            log_file.write("\n".join(["".join(map(str, row)) for row in x]))

            log_file.write("\n\n")  
        else:  
            log_file.write(x + "\n")


print(f"Results are in the following file {log_file_path}")

