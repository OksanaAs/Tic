map = [1, 2, 3,
       4, 5, 6,
       7, 8, 9]

good = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]]


def print_maps():
    print(map[0], end=" ")
    print(map[1], end=" ")
    print(map[2])

    print(map[3], end=" ")
    print(map[4], end=" ")
    print(map[5])

    print(map[6], end=" ")
    print(map[7], end=" ")
    print(map[8])


def maps(step, symbol):
    ind = map.index(step)
    map[ind] = symbol
def valid(i):
    if i >9 or i<1:
        return True
    else:
        return False


def result():
    win = ""

    for i in good:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            win = "X"
        if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
            win = "O"

    return win


end = False
user = True
count = 0
while end == False:
    if (count > 8):
        break

    print_maps()

    if user == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
        while valid(step):
            print("Не правильный ход, повторите")
            step = int(input("Игрок 1, ваш ход: "))

    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))
        while valid(step):
            print("Не правильный ход, повторите")
            step = int(input("Игрок 2, ваш ход: "))

    maps(step, symbol)
    win = result()
    if win != "":
        end = True
    else:
        end = False
    count += 1

    user = not (user)
print_maps()
print("Победил", win or "ничья")
