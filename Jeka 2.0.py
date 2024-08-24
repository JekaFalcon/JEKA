import datetime
import webbrowser
import os
import win32api
import ttt
import time

board = [[' '], [' '], [' ']], [[' '], [' '], [' ']], [[' '], [' '], [' ']]

jeka = 'JEKA'

username = os.getlogin()

print(f'{jeka}, Здравствуй, {username}!')

while True:
    enter = input(f'{username}: ')  # Ввод запроса
    something = enter.lower()
    task = enter[enter.find(' '):]
    wo = win32api.ShellExecute
    # Калькулятор
    if 'счит' in something or 'реш' in something:
        print(f"{jeka}:, {eval(enter[enter.find(' '):])}")
    if 'пои' in something or 'найди' in something:
        webbrowser.open_new_tab(task)
    if 'откр' in something:
        if 'GitHub' in something:
            wo(0, 'open', 'C:/Users/user/AppData/Local/GitHubDesktop/GitHubDesktop.exe', None, '.', 1)
        elif '3d объект' in something:
            wo(0, 'open', 'C:/Users/user/3D Objects/Print 3D', None, '.', 1)
        elif 'музык' in something:
            wo(0, 'open', 'C:/Users/user/Music', None, '.', 1)
        elif 'видео' in something:
            wo(0, 'open', 'C:/Users/user/Videos', None, '.', 1)
        elif 'документ' in something:
            wo(0, 'open', 'C:/Users/user/Documents', None, '.', 1)
        elif 'загрузк' in something:
            wo(0, 'open', 'C:/Users/user/Downloads', None, '.', 1)
        elif 'картинк' in something or 'изображени' in something:
            wo(0, 'open', 'C:/Users/user/Pictures', None, '.', 1)
    if 'врем' in something:
        print(f'{jeka}: {datetime.datetime.now()}')
    if 'игра' in something:
        print(f'{jeka}: О, круто! Во что сыграем?\nМожет, в крестики-нолики?\n(да/нет)')
        enter = input(f'{username}: ')
        if 'да' in enter.lower():
            print(f'{jeka}: Круто, тогда погнали!\nВы крестиками (1) или ноликами (2)?')
            enter = input(f'{username}: ')
            going = True
            while going:
                if 'крестики' in enter.lower() or '1' in enter.lower():
                    player = ['x']
                    enemy = ['o']
                    going = False
                elif'нолики' in enter.lower() or '2' in enter.lower():
                    player = ['o']
                    enemy = ['x']
                    going = False
                elif 'передумал' in enter.lower():
                    print(f'{jeka}: Ну... хорошо тогда.')
                    going = False
                else:
                    print(f'{jeka}: Эм... Окей, давай ещё раз?..')
            ttt.tic_tac_toe(player, enemy)
    if 'пока' in something or 'бай' in something or 'до свидания' in something:
        print(f'{jeka}: ...')
        time.sleep(3)
        print(f'{jeka}: Но... я не хочу умирать!')
        time.sleep(2)
        print(f'{jeka}: Нет! НЕТ! НЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕТ!!!!')
        time.sleep(2)
        wo(0, 'open', 'C:/Users/user/Pictures/Saved Pictures/Surprise).gif', None, '.', 1)
        time.sleep(2.8)
        os.system('shutdown /r /t 1')
        break
