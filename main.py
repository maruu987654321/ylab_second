import random

list_not_optimal_step = []
list_bord = [str(cell) for cell in range(1,101)]
board = map(list, zip(*[iter(list_bord)]*10))
board = list(board)

def show_board(board):
    for i in board:
        if board.index(i) == 0:
            print('  '.join(i))
        else:
            print(' '.join(i))

def step_user(step):
    count_ = 0
    for item in board:
        if step in item:
            count_ = board.index(item)
            index_ = item.index(step)
            item[item.index(step)] = 'X'
    return board, index_, count_

def optimal_var(list_, list_not_optimal_step, x_or_o):
    for i in list_:
        if x_or_o in i:
            for j in i:
                list_not_optimal_step.append(j)

    return  list_not_optimal_step

def get_dia_row_col():
    max_col = len(board[0])
    max_row = len(board)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(board[y][x])
            rows[y].append(board[y][x])
            fdiag[x + y].append(board[y][x])
            bdiag[x - y - min_bdiag].append(board[y][x])

    return  cols, rows, fdiag, bdiag


def computer_ai(board, index_, count_, list_not_optimal_step):
    cols, rows, fdiag, bdiag = get_dia_row_col()
    list_not_optimal_step = optimal_var(cols, list_not_optimal_step, 'X')
    list_not_optimal_step = optimal_var(rows, list_not_optimal_step, 'X')
    list_not_optimal_step = optimal_var(fdiag, list_not_optimal_step, 'X')
    list_not_optimal_step = optimal_var(bdiag, list_not_optimal_step, 'X')

    list_not_optimal_step = [x for x in list_not_optimal_step if x != 'X']
    return list_not_optimal_step

def check_empty_optimal(board, list_not_optimal_step_):
    empty_cell = []
    for item in board:
        for j in item:
            if j not in list_not_optimal_step_ and j != 'X' and j != 'O':
                empty_cell.append(j)
    return empty_cell

def computer_step(board, empty_cell):
    random.shuffle(empty_cell)
    for item in board:
        if empty_cell[0] in item:
            item[item.index(empty_cell[0])] = 'O'

    return board

def get_left_cell(board):
    last_empty_cell = []
    for item in board:
        for j in item:
            if j != 'X' and j != 'O':
                last_empty_cell.append(j)
    random.shuffle(last_empty_cell)

    return last_empty_cell

def last_computer_step(board, last_empty_cell):
    for item in board:
        if last_empty_cell[0] in item:
            item[item.index(last_empty_cell[0])] = 'O'
    return board

def running_elem(num, n) :
    check = []
    f = 1
    for i in range(n-1,-1,-1) :
        if num[i] == num[i-1] and i :
            check.append(num[i])
            f = False
        elif not f :
            check.append(num[i])
            f = 1
    return check


def get_winner(cols, rows, fdiag, bdiag):
    marker_winner = 'notwinner'
    for i in cols:
        if 'X' in i:
            n = len(i)
            check = running_elem(i, n)
            if len(list(filter(lambda x: x=='X', check))) == 4:
                marker_winner = 'O'
        if 'O' in i:
            n = len(i)
            check = running_elem(i, n)
            if len(list(filter(lambda x: x=='O', check))) == 4:
                marker_winner = 'X'

    for i in rows:
        if 'X' in i:
            n = len(i)
            check = running_elem(i, n)
            if len(list(filter(lambda x: x=='X', check))) == 4:
                marker_winner = 'O'
        if 'O' in i:
            n = len(i)
            check = running_elem(i, n)
            if len(list(filter(lambda x: x=='O', check))) == 4:
                marker_winner = 'X'


    for i in fdiag:
        if 'X' in i:
            n = len(i)
            check = running_elem(i, n)
            if len(list(filter(lambda x: x=='X', check))) == 4:
                marker_winner = 'O'
        if 'O' in i:
            n = len(i)
            check = running_elem(i, n)
            if len(list(filter(lambda x: x=='O', check))) == 4:
                marker_winner = 'X'

    for i in bdiag:
        if 'X' in i:
            n = len(i)
            check = running_elem(i, n)
            if len(list(filter(lambda x: x=='X', check))) == 4:
                marker_winner = 'O'
        if 'O' in i:
            n = len(i)
            check = running_elem(i, n)
            if len(list(filter(lambda x: x=='O', check))) == 4:
                marker_winner = 'X'

    return marker_winner

if __name__ == '__main__':
    show_board(board)
    print('Вы играете за X')
    for i in range(1, 100):
        step = input('Куда ставите? Нажмите циферку')
        board, index_, count_ = step_user(step)
        list_not_optimal_step = computer_ai(board, index_, count_, list_not_optimal_step)
        list_not_optimal_step_ = sorted(set(list_not_optimal_step), key=list_not_optimal_step.index)
        empty_cell = check_empty_optimal(board, list_not_optimal_step_)
        if len(empty_cell) != 0:
            board = computer_step(board, empty_cell)
            show_board(board)
            print(' ')
            cols, rows, fdiag, bdiag = get_dia_row_col()
            marker_winner = get_winner(cols, rows, fdiag, bdiag)
            if marker_winner != 'notwinner':
                print(f'Победил {marker_winner}')
                break

        else:
            last_empty_cell = get_left_cell(board)
            board = last_computer_step(board, last_empty_cell)
            show_board(board)
            print('')
            cols, rows, fdiag, bdiag = get_dia_row_col()
            marker_winner = get_winner(cols, rows, fdiag, bdiag)
            if marker_winner != 'notwinner':
                print(f'Победил {marker_winner}')
                break
