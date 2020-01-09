# TicTacToe
import os

move_possibility = list('qweasdzxc')
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
move_info = 'Please input your move using the letters QWEASDZXC. For example Q is the left upper corner. \n'
os.system('clear')
exit_list = ['exit', 'wyjscie', "wyjście", 'quit']
player = False


def init_board(player):
    os.system('clear')
    current_player = changing_player(player)
    print('player 1' if current_player is True else 'player 2')
    for field in range(len(board)):
        print(' ' + board[field][0] + '|' + board[field][1] + '|' + board[field][2] + ' ')
        if field < 2:
            print('-------')

def correctness_move():
    current_move = get_move()
    if current_move in move_possibility:
        mark(current_move, player)
    elif current_move in exit_list:
        exit()
    else:
        print('Pleas add correct answer')
        get_move()


def get_move():
    move = input(move_info).lower()
    # print(move)
    return move


def calculate_empty_field(board):
    list_field_in_row = []
    for row in board:
        list_field_in_row.append(row.count(' '))

    empty_field = sum(list_field_in_row)

    return empty_field


def mark(move, player):
    current_player = changing_player(player)
    type_mark = 'X' if current_player is True else 'O'
    if move == 'q':
        board[0][0] = type_mark
    elif move == 'w':
        board[0][1] = type_mark
    elif move == 'e':
        board[0][2] = type_mark
    elif move == 'a':
        board[1][0] = type_mark
    elif move == 's':
        board[1][1] = type_mark
    elif move == 'd':
        board[1][2] = type_mark
    elif move == 'z':
        board[2][0] = type_mark
    elif move == 'x':
        board[2][1] = type_mark
    elif move == 'c':
        board[2][2] = type_mark
    else:
        print('Please add correct answer')

def changing_player(player = True):
    player = not player
    return player


def win(board):
    # horizontal
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            finish_gamge = row[0]
            return finish_gamge
    # vertical
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            finish_gamge = check[0]
            return finish_gamge

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(board)))):
        diags.append(board[idx][reverse_idx])

    if diags.count(diags[0]) == len(diags) and diags[0] != ' ':
        finish_gamge = diags[0]
        return finish_gamge
    # \ diagonal
    diags = []
    for ix in range(len(board)):
        diags.append(board[ix][ix])

    if diags.count(diags[0]) == len(diags) and diags[0] != ' ':
        finish_gamge = diags[0]
        return finish_gamge



empty_field = calculate_empty_field(board)


while empty_field > 0:

    #print(empty_field)
    #empty_field = board.count(' ')
    #print(empty_field)
    init_board(player)
    correctness_move()
    player = changing_player(player)
    #empty_field -= 1
    winner = win(board)
    if winner == 'X' or winner == 'O':
        print(f'Player {winner} has won!')
        break
    empty_field = calculate_empty_field(board)
    if empty_field == 0:
        print("It's a tie!")
        break
