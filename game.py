"""
CSE210
Solo Code Submission
TIC-TAC-TOE Prove Assignment
Wilson Romero
BYU-I 2022
"""

def print_board(board):
    print(f"\033[1;37m{'|'.join(list(board[:3])):>10}")
    print(f"{'-'*5:>10}")
    print(f"{'|'.join(list(board[3:6])):>10}")
    print(f"{'-'*5:>10}")
    print(f"{'|'.join(list(board[6:9])):>10}\n")

def update_board(player_symbol, selection, board):
    sub_board = list(board)
    sub_board[selection-1] = player_symbol
    return "".join(sub_board)
     
def check_win(player, board):
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
    pass
    
if __name__ == '__main__':
    main()
