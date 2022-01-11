"""
CSE210
Solo Code Submission
TIC-TAC-TOE Prove Assignment
Wilson Romero
BYU-I 2022
"""

def print_board(board):
    """takes the board string, convert it into 3 list
    sections and then joins with a separator"""
    
    print(f"\033[1;37m{'|'.join(list(board[:3])):>10}")
    print(f"{'-'*5:>10}")
    print(f"{'|'.join(list(board[3:6])):>10}")
    print(f"{'-'*5:>10}")
    print(f"{'|'.join(list(board[6:9])):>10}\n")


def update_board(player_symbol, board, selection):
    """This function will take the current board, 
    the user input and the user symbol and will 
    update the board"""
    sub_board = list(board)
    sub_board[selection-1] = player_symbol
    return "".join(sub_board)
     
def check_win(player, board):
    """There are 9 posible ways to win, this function
    evaluates if any of the win options is in the
    player's seletions and if so it will return true"""
    wins = [
            [1,2,3], 
            [4,5,6],
            [7,8,9],
            [1,4,7],
            [2,5,8],
            [3,6,9],
            [1,5,9],
            [7,5,3],
        ]

    for win in wins:
        if(all(x in player for x in win)):
            return True

    return False
    
def main():

    """This is the main function here is the rest
    of the logic of the game"""
    players = {
        "player1": {"name": "Player1", "symbol": "X", "selection": [], "color": "\033[1;33m"},
        "player2": {"name": "Player2", "symbol": "O", "selection": [], "color": "\033[1;36m"}
    }
    
    player_turn = True #keep track of the player turn
    board = "123456789" #this is the board
    winner = False #hold the value if there is a winner
    current_player = "" #holds the current player name
    i = 0
        
    print("Welcome to TIC-TAC-TOE game\n")

	
    while i <= 8:
        i += 1
				
        print_board(board) #prints the board
        
        #check whose player turn is
        if player_turn:
            current_player = "player1"
        else:
            current_player = "player2"

	#takes the selection from the current player
        selection = int(input(f"{players[current_player]['color']}Player {players[current_player]['name']} ({players[current_player]['symbol']}) please enter your selection: "))
        
        #add the selection to the current user selection list
        players[current_player]["selection"].append(selection)

	#update the board
        board = update_board(players[current_player]["symbol"], board, selection)
        
        #change the player turn to the next player
        player_turn = not player_turn
   
   	#check if there is a winner
        winner = check_win(players[current_player]["selection"], board)
        if winner:
            print("\n")
            print_board(board)
            print(f"\033[1;32mCongratulations {players[current_player]['name']} you have won! \nAnd it only took you {i} turns!")
            break

    
    #if a winner is not found then print that it is a tie
    if winner == False:
        print_board(board)
        print("\033[3;34mGreat game but it was a tie!")
    
if __name__ == '__main__':
    main()
