import random

board = [str(cell) for cell in range(1, 101)]

remain_cells = [str(cell) for cell in range(1, 101)]


def print_board(board):
    for i in range(100):
        print(board[i], end='\t')
        if (i + 1) % 10 == 0:
            print('\n')


def check_cell(index, mark, board):
    if board[index] in ('X', 'O'):
        return True


def put_mark_remove_cell(index, mark, remain_cells, board):
    remain_cells.remove(board[index])
    board[index] = mark


def select_mark():
    player_mark = ''
    while player_mark not in ('X', 'O'):
        player_mark = input('Выберете, за кого вы будете играть - Х или О? ').upper()
        if player_mark == 'X':
            computer_mark = 'O'
        else:
            computer_mark = 'X'
    return player_mark, computer_mark


def check_diagonal_line(index, mark, board):
    count = 1
    step = 0
    for i in range(9 - index // 10):
        if (index + step + 1) % 10 != 0 and (
                index + step) // 10 != 9:
            step += 11
            if board[index + step] == mark:
                count += 1
            else:
                break
        else:
            break
    step = 0
    for i in range(index // 10):
        if (index + step + 1) % 10 != 1 and (
                index + step) // 10 != 0:
            step -= 11
            if board[index + step] == mark:
                count += 1
            else:
                break
        else:
            break
    if count >= 5:
        return True
    count = 1
    step = 0
    for i in range(9 - index // 10):
        if (index + step + 1) % 10 != 1 and (
                index + step) // 10 != 9:
            step += 9
            if board[index + step] == mark:
                count += 1
            else:
                break
        else:
            break
    step = 0
    for i in range(index // 10):
        if (index + step + 1) % 10 != 0 and (
                index + step) // 10 != 0:
            step -= 9
            if board[index + step] == mark:
                count += 1
            else:
                break
        else:
            break
    if count >= 5:
        return True


def check_gorizontal_line(index, mark, board):
    count = 1
    step = 1
    while True:
        if (index + 1) % 10 != 0:
            for i in range(9 - index % 10):
                if board[index + step] == mark:
                    count += 1
                    step += 1
                else:
                    break
        step = -1
        if (index + 1) % 10 != 1:
            for i in range(index % 10):
                if board[index + step] == mark:
                    count += 1
                    step -= 1
                else:
                    break
        break
    if count >= 5:
        return True


def check_vertical_line(index, mark, board):
    count = 1
    step = 10
    while True:
        if index // 10 != 9:
            for i in range(9 - index // 10):
                if board[index + step] == mark:
                    count += 1
                    step += 10
                else:
                    break
        step = -10
        if index // 10 != 0:
            for i in range(index // 10):
                if board[index + step] == mark:
                    count += 1
                    step -= 10
                else:
                    break
        break
    if count >= 5:
        return True


def check_game_finish(index, mark, board):
    if check_gorizontal_line(index, mark, board) or check_vertical_line(index, mark, board) or check_diagonal_line(
            index, mark, board):
        return True


def replay():
    decision = ""
    while decision not in ('да', 'нет'):
        decision = input(
            'Хотите сыграть еще разок? Напишите да или нет'
        ).lower()

    return decision == 'да'


def clear_screen():
    print('\n' * 100)


def computer_loose_check(computer_mark, remain_cells, board):
    remain_cells_in_cycle = remain_cells.copy()
    for i in range(len(remain_cells)):
        index = int(random.choice(remain_cells_in_cycle)) - 1
        remain_cells_in_cycle.remove(board[index])
        tmp = board[index]
        put_mark_remove_cell(index, computer_mark, remain_cells, board)
        if check_game_finish(index, computer_mark, board) and i != len(remain_cells):
            remain_cells.append(tmp)
            board[index] = tmp
            continue
        elif not check_game_finish(index, computer_mark, board):
            return True
        else:
            return False


def start_new_game():
    board = [str(cell) for cell in range(1, 101)]
    remain_cells = [str(cell) for cell in range(1, 101)]
    player_mark, computer_mark = select_mark()

    return board, remain_cells, player_mark, computer_mark


player_mark, computer_mark = select_mark()


def main_loop(player_mark, computer_mark, board, remain_cells):
    print_board(board)
    print('\n\n')
    while True:
        if len(remain_cells) > 0:
            try:  # Ход игрока
                index = int(input('Укажите номер ячейки : ')) - 1
                print()
                assert index in range(100)
                if check_cell(index, player_mark, board):
                    print('К сожалению, ячейка уже занята')
                    continue
                put_mark_remove_cell(index, player_mark, remain_cells, board)
                if check_game_finish(index, player_mark, board):
                    print_board(board)
                    print('Вы проиграли')
                    if replay():
                        board, remain_cells, player_mark, computer_mark = start_new_game()
                        print_board(board)
                        print('\n\n')
                        continue
                    else:
                        return
            except ValueError:
                print('Вы должны ввести число')
                continue
            except AssertionError:
                print('Введите число строго в диапазоне от 1 до 100')
                continue

            if computer_loose_check(computer_mark, remain_cells, board):  # Ход компьютера
                print_board(board)
                continue
            else:
                print_board(board)
                print('Комп проиграл')
                if replay():
                    board, remain_cells, player_mark, computer_mark = start_new_game()
                    print_board(board)
                    print('\n\n')
                    continue
                else:
                    return
            print_board(board)
        else:
            print('Ничья! Ура!')
            if replay():
                board, remain_cells, player_mark, computer_mark = start_new_game()
                print_board(board)
                print('\n\n')
                continue
            else:
                return


if __name__ == '__main__':
    main_loop(player_mark, computer_mark, board, remain_cells)