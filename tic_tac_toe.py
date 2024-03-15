# Выводим приветствие
print('КРЕСТИКИ НОЛИКИ v 1.1')

# Создаем игоровое поле
print('''Это игровое поле.
Для хода введите номер строки и номер столбца, через пробел''')

playing_field = [
    [' ', ' ', ' ']
    , [' ', ' ', ' ']
    , [' ', ' ', ' ']
]

def show():
    print()
    print(f'  0  1  2')
    for i in range(3):
        print(f' ----------')
        print(f"{i}| {playing_field[i] [0]}| {playing_field[i] [1]}| {playing_field[i] [2]}|")

# Создаем условия хода

def motion():

    while True:
        cordinates = input('Ваш ход: ').split()
        if len(cordinates) != 2:
            print('Введите два значенияю')
            continue
        x, y = cordinates
        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа')
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or  0 > y or  y > 2:
            print('Клетка вне игрового поля')
            continue
        if playing_field[x][y] != ' ':
            print('Клетка занята')
            continue
        return x, y

# Создаем условия выйгрыша

def win():
    win_cordinates = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cordinates in win_cordinates:
        symbols = []
        for c in cordinates:
            symbols.append(playing_field[c[0]][c[1]])
        if symbols == ['x', 'x', 'x']:
            print('Выиграл x!')
            return True
        if symbols == ['o', 'o', 'o']:
            print('Выиграл o!')
            return True
    return False

# Создаем условия игры

num = 0
while True:
    num += 1
    show()
    win()
    if num % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')
    x, y = motion()
    if num % 2 == 1:
        playing_field[x][y] = 'x'
    else:
        playing_field[x][y] = 'o'
    if win():
        break
    if num == 9:
        print('Ничья')
        break






