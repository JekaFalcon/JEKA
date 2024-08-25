import datetime
import webbrowser
import os
import win32api
import time

board = [[' '], [' '], [' ']], [[' '], [' '], [' ']], [[' '], [' '], [' ']]

jeka = 'JEKA'

username = os.getlogin()

print(f'{jeka}, Здравствуй, {username}! Чем могу помочь?')

counter = 0
fd, sd = 0, 0
drunk = False

while True:
    if fd - sd >= counter:
        drunk = False
    enter = input(f'{username}: ')  # Ввод запроса
    something = enter.lower()
    task = enter[enter.find(' '):]
    wo = win32api.ShellExecute
    if something == '*напоить Jeka*':
        drunk = True
        sd = time.perf_counter()
        counter += 15
    if 'счит' in something or 'реш' in something:  # Решение алгебраических примеров
        if drunk:
            print(f'{jeka}: Ща-ща...')
            time.sleep(7)
            print(f"{jeka}: На те... Ответ: {eval(enter[enter.find(' '):])}")
        else:
            print(f"{jeka}: Считаю/решаю...")
            time.sleep(3)
            print(f"{jeka}: Готово! Ответ: {eval(enter[enter.find(' '):])}")
    if 'пои' in something or 'найди' in something:  # Поиск информации в интернете
        if drunk:
            print(f'{jeka}: Щас...')
            time.sleep(10)
            print(f'{jeka}: Воп... Нашёл...')
        else:
            print(f'{jeka}: Ищу-ищу...')
            time.sleep(3)
            print(f'{jeka}: Что-то нашёл!')
        webbrowser.open_new_tab(task)
    if 'откр' in something:
        print(f'{jeka}: Открываю...')
        time.sleep(1)
        if 'GitHub' in something:
            print(f'{jeka}: Вот, прошу!')
            wo(0, 'open', 'C:/Users/user/AppData/Local/GitHubDesktop/GitHubDesktop.exe', None, '.', 1)
        elif '3d объект' in something:
            print(f'{jeka}: Вот, прошу!')
            wo(0, 'open', 'C:/Users/user/3D Objects/Print 3D', None, '.', 1)
        elif 'музык' in something:
            print(f'{jeka}: Вот, прошу!')
            wo(0, 'open', 'C:/Users/user/Music', None, '.', 1)
        elif 'видео' in something:
            print(f'{jeka}: Вот, прошу!')
            wo(0, 'open', 'C:/Users/user/Videos', None, '.', 1)
        elif 'документ' in something:
            print(f'{jeka}: Вот, прошу!')
            wo(0, 'open', 'C:/Users/user/Documents', None, '.', 1)
        elif 'загрузк' in something:
            print(f'{jeka}: Вот, прошу!')
            wo(0, 'open', 'C:/Users/user/Downloads', None, '.', 1)
        elif 'картинк' in something or 'изображени' in something:
            print(f'{jeka}: Вот, прошу!')
            wo(0, 'open', 'C:/Users/user/Pictures', None, '.', 1)
        else:
            if drunk:
                print(f'{jeka}: Не-не... не могу.')
            print(f'{jeka}: Извините, но я не могу найти то, что Вам нужно, или я просто не могу из-за программы.')
    if 'врем' in something:
        if drunk:
            print(f'{jeka}: Мгм... Сейчас у нас', end=' ')
        else:
            print(f'{jeka}: Сейчас... Вот, нынешние дата и время:', end=' ')
        print(datetime.datetime.now())
    if 'игра' in something:
        print(f'{jeka}: О, круто! Во что сыграем?\nМожет, в крестики-нолики?\n(да/нет)')
        enter = input(f'{username}: ')
        if 'да' in enter.lower():
            print(f'{jeka}: Круто, тогда погнали!')
            webbrowser.open_new_tab('https://tictactoefree.com')
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
    fd = time.perf_counter()
