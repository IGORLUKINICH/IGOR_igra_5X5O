import time  # импортируем модуль времени

print('''
                Добро пожаловать в игру 5 X 5 O !!! 
''')

time.sleep(3)              # Пауза перед словами

print("                     Ну что, начнем!")

print("\n" * 1)  # ширина пробела между строками

field = [1, 2, 3, 4, 5,     # Разметка игрового поля в виде списка позиций
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25]

def print_field():          # Функция вывода игрового поля на экран
    print(field[0], end=" ")
    print(field[1], end=" ")
    print(field[2], end=" ")
    print(field[3], end=" ")
    print(field[4])

    print(field[5], end=" ")
    print(field[6], end=" ")
    print(field[7], end=" ")
    print(field[8], end=" ")
    print(field[9])

    print(field[10], end=" ")
    print(field[11], end=" ")
    print(field[12], end=" ")
    print(field[13], end=" ")
    print(field[14])

    print(field[15], end=" ")
    print(field[16], end=" ")
    print(field[17], end=" ")
    print(field[18], end=" ")
    print(field[19])

    print(field[20], end=" ")
    print(field[21], end=" ")
    print(field[22], end=" ")
    print(field[23], end=" ")
    print(field[24])

def step_field(step, symbol): # Функция хода в ячейку поля будет рисовать X, O в зависимости то что в нее передали
    a = field.index(step)     # Вставка элемента по индексу 
    field[a] = symbol        

w_lines = [[0, 1, 2, 3, 4],    # Список выйгрышных комбинаций
           [5, 6, 7, 8, 9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24],
           [0, 5, 10, 15, 20],
           [1, 6, 11, 16, 21],
           [2, 7, 12, 17, 22],
           [3, 8, 13, 18, 23],
           [4, 9, 14, 19, 24],
           [1, 7, 13, 19, 25],
           [5, 9, 13, 17, 21]]


def winner_result():    # Функция проверки выйгрышных комбинаций в игре
    winner = ""

    for i in w_lines:     # для i из w_lines проверяем есть ли линии состоящие из 5 X 5 0  
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X" and field[i[3]] == "X" and field[i[4]] == "X":
            winner = "X"

        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O" and field[i[3]] == "O" and field[i[4]] == "O":
            winner = "O"

    return winner

#  Состав основной программы
game_over = False          # Называем глобальные переменные
player1 = True

while game_over == False:  # Цикл программы по заполнению списка значениями X, O вводимыми игроками

    # 1. Показываем игровое поле
    time.sleep(1)  # Пауза перед словами
    print(("Это игровое поле")* 1)

    print("\n" * 1)  # ширина пробела между строками
    time.sleep(1)    # Пауза перед словами

    print_field()    # Вывод игрового поля
    print("\n" * 1)  # ширина пробела между строками
    
    # 2. Игроки делают ходы с присвоением индексам списка значений X, O
    if player1 == True:
        symbol = "X"
        step = int(input("Ходит первый игрок: "))
    else:             
        symbol = "O"
        step = int(input("Ходит второй игрок: "))

    step_field(step, symbol)       # ставим шаг на указанную ячейку

    winner = winner_result()      # определим победителя
    if winner != "":
        game_over = True
    else:
        game_over = False

    player1 = not(player1)

print("\n" * 2)                # ширина пробела между строками
print(("Все - конец игры")* 1) # Конец игры.
time.sleep(2)                  # Пауза перед словами
print("\n" * 1)                # ширина пробела между строками
print_field()                  # Вывод итогового игрового поля
print("\n" * 1)                # ширина пробела между строками
print("Победил", winner)       # Вывод победителя игры
