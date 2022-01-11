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
     pass
    
def main():
    pass
    
if __name__ == '__main__':
    main()
