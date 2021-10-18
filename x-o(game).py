
def title_text():
    print("""
    =======================
    |    Здравствуйте!    |
    Добро пожаловать в игру
    |   крестики-нолики   |
    =======================
    |    Правила игры:    |
    |     Ставим X Y      |
    |  х - номер строки   |
    |  y - номер столбца  |
    =======================""")


def play_field():
    print("       Игровое поле: ")
    print()
    print("         | 0 | 1 | 2 | ")
    print("       --------------- ")
    for i, row in enumerate(field):
        row_str = f"       {i} | {' | '.join(map(str, row))} | "
        print(row_str)
        print("       --------------- ")
    print()


def coordinate():
    while True:
        cords = input("              Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Вводите только числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Введенные координаты не в диапазоне ")
            continue

        if field[x][y] != " ":
            print(" Клетка уже занята! ")
            continue

        return x, y


def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]

    for point in win_cord:
        symbols = []
        for c in point:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(" Выиграл игрок Х! ")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Выиграл игрок 0! ")
            return True
    return False


title_text()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    play_field()

    if check_win():
        break

    if count % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")

    x, y = coordinate()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if count == 9:
        print("Победила дружба!")
        break














