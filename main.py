# Игра Крестики-нолики на Python

# Определяем переменные
board = [" " for i in range(9)]

# Функция для отображения игрового поля
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Функция для проверки победы
def winner(char):
    return (
        (board[0] == char and board[1] == char and board[2] == char) or
        (board[3] == char and board[4] == char and board[5] == char) or
        (board[6] == char and board[7] == char and board[8] == char) or
        (board[0] == char and board[3] == char and board[6] == char) or
        (board[1] == char and board[4] == char and board[7] == char) or
        (board[2] == char and board[5] == char and board[8] == char) or
        (board[0] == char and board[4] == char and board[8] == char) or
        (board[2] == char and board[4] == char and board[6] == char))

# Основной цикл игры
while True:
    print_board()
    choice = int(input("Куда поставить крестик? (1-9): "))
    if board[choice - 1] == " ":
        board[choice - 1] = "X"
    else:
        print()
        print("Это поле уже занято!")
        continue

    if winner("X"):
        print_board()
        print("Вы победили!")
        break

    # Компьютер делает ход
    computer_choice = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if winner("O"):
                computer_choice = i
                break
            else:
                board[i] = " "

    if computer_choice != -1:
        board[computer_choice] = "O"
        print_board()
        print("Компьютер победил!")
        break

    if " " not in board:
        print("Ничья!")
        break