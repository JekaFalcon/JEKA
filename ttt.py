import os
import random


board = [[' '], [' '], [' ']], [[' '], [' '], [' ']], [[' '], [' '], [' ']]
jeka = 'JEKA'
username = os.getlogin()


def check():
    # Победа игрока
    if board[0][0] == board[0][1] == board[0][2] == player or\
            board[1][0] == board[1][1] == board[1][2] == player or\
            board[2][0] == board[2][1] == board[2][2] == player or\
            board[0][0] == board[1][0] == board[2][0] == player or\
            board[0][1] == board[1][1] == board[1][2] == player or\
            board[0][2] == board[1][2] == board[2][2] == player or\
            board[0][0] == board[1][1] == board[2][2] == player or\
            board[2][0] == board[1][1] == board[0][2] == player:
        print(f'{jeka}: Ого, ты победил! Поздравляю!')
        return True
    # Победа Жеки
    elif board[0][0] == board[0][1] == board[0][2] == enemy or \
            board[1][0] == board[1][1] == board[1][2] == enemy or \
            board[2][0] == board[2][1] == board[2][2] == enemy or \
            board[0][0] == board[1][0] == board[2][0] == enemy or \
            board[0][1] == board[1][1] == board[1][2] == enemy or \
            board[0][2] == board[1][2] == board[2][2] == enemy or \
            board[0][0] == board[1][1] == board[2][2] == enemy or \
            board[2][0] == board[1][1] == board[0][2] == enemy:
        print(f'{jeka}: Ура, я победил! Но я думаю, в следующий раз победа будет за тобой.')
        return True
    elif [' '] not in board[0] and\
            [' '] not in board[1] and\
            [' '] not in board[2]:
        print(f'{jeka}: Хм... ничья.')
        return True


def tic_tac_toe(player, enemy):
    global_active = True
    if player == ['o']:
        print(f'\n{jeka}: Я хожу первым!')
        local_active = True
        while local_active:
            x, y = random.randrange(0, 3), random.randrange(0, 3)
            if board[x][y] == [' ']:
                board[x][y] = enemy
                local_active = False
            else:
                continue
        print(f'{jeka}: Готово!')
    while global_active:
        print(*board, sep='\n')
        if check():
            break
        local_active = True
        print(f'{jeka}: Ваш ход!\n(столбец, строка)')
        while local_active:
            x, y = list(map(int, input(f'{username}: ').split()))
            x -= 1
            y -= 1
            if board[x][y] == [' ']:
                board[x][y] = player
                local_active = False
            else:
                print(f'{jeka}: Нет, эта занята! Выберите другую клетку.')
        print(*board, sep='\n')
        if check():
            break
        print(f'\n{jeka}: Теперь мой ход...')
        local_active = True
        while local_active:
            x, y = random.randrange(0, 3), random.randrange(0, 3)
            if board[x][y] == [' ']:
                board[x][y] = enemy
                local_active = False
            else:
                continue
        print(f'{jeka}: Готово!')
        if check():
            break
