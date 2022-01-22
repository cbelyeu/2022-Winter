'''
W02 Prove: Developer-Solo Code Submission
Author: Cassandra Belyeu
'''

def main():
    player = next_player("")
    board = create_board()
    while not (has_a_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    player = next_player(player)
    if has_a_winner(board):
        print(f"{player} is the winner!")
    elif is_a_draw(board):
        print("We'll call it a draw!")
    print("Good game, thanks for playing")


def make_move(player, board):
    players_choice = input(f"{player}'s turn to choose a square (1-9): ")
    square = int(players_choice)
    board[square - 1] = player

def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    print("We'll call it a draw!")
    return True

def has_a_winner(board):
    '''This handles the three cases of horizontal win'''
    did_we_win_by_horizontal = board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]
    '''This handles the three cases of winning by filling the verticals'''
    did_we_win_by_vertical = board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]
    '''This handles the two cases of winning by diagonals'''
    did_we_win_by_diagonal = board[0] == board[4] == board[8] or board[6] == board[4] == board[2]
    return did_we_win_by_horizontal or did_we_win_by_vertical or did_we_win_by_diagonal

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def next_player(current_player):
    if current_player == "x":
        return "o"
    else: return "x"

if __name__ == "__main__":
    main()