# tic tac toe the game
# enter numbers from 1 to 3 with space inbetween
# gameplan:
# ---------------
#|(1 3)(2 3)(3 3)|
#|(1 2)(2 2)(3 2)|
#|(1 1)(2 1)(3 1)|
# ---------------


matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
i = 0
winvar = 0

print("---------")
print("| " + matrix[0][2] + " " + matrix[1][2] + " " + matrix[2][2] + " |")
print("| " + matrix[0][1] + " " + matrix[1][1] + " " + matrix[2][1] + " |")
print("| " + matrix[0][0] + " " + matrix[1][0] + " " + matrix[2][0] + " |")
print("---------")

for i in range(9):

    if winvar == 1:
        break

    def useraction():
        try:
            x, y = input("Enter the coordinates: ").split()

            if x.isalpha() or y.isalpha():
                print("You should enter numbers!")
                useraction()
            elif int(x) > 3 or int(y) > 3:
                print("Coordinates should be from 1 to 3!")
                useraction()
            elif matrix[int(x) - 1][int(y) - 1] == " " and i % 2 == 0:
                matrix[int(x) - 1][int(y) - 1] = 'X'
            elif matrix[int(x) - 1][int(y) - 1] == " " and i % 2 != 0:
                matrix[int(x) - 1][int(y) - 1] = 'O'
            else:
                print("This cell is occupied! Choose another one!")
                useraction()
        except:
            print("You should enter numbers")

    useraction()

    print("---------")
    print("| " + matrix[0][2] + " " + matrix[1][2] + " " + matrix[2][2] + " |")
    print("| " + matrix[0][1] + " " + matrix[1][1] + " " + matrix[2][1] + " |")
    print("| " + matrix[0][0] + " " + matrix[1][0] + " " + matrix[2][0] + " |")
    print("---------")

    row0 = [matrix[0][0], matrix[1][0], matrix[2][0]]
    row1 = [matrix[0][1], matrix[1][1], matrix[2][1]]
    row2 = [matrix[0][2], matrix[1][2], matrix[2][2]]
    colum0 = [matrix[0][0], matrix[0][1], matrix[0][2]]
    colum1 = [matrix[1][0], matrix[1][1], matrix[1][2]]
    colum2 = [matrix[2][0], matrix[2][1], matrix[2][2]]
    diagonal1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    diagonal2 = [matrix[0][2], matrix[1][1], matrix[2][0]]

    if row0[0] == 'X' and row0[1] == 'X' and row0[2] == 'X':
        print("X wins")
        winvar = 1
    elif row0[0] == 'O' and row0[1] == 'O' and row0[2] == 'O':
        print("O wins")
        winvar = 1

    if row1[0] == 'X' and row1[1] == 'X' and row1[2] == 'X':
        print("X wins")
        winvar = 1
    elif row1[0] == 'O' and row1[1] == 'O' and row1[2] == 'O':
        print("O wins")
        winvar = 1

    if row2[0] == 'X' and row2[1] == 'X' and row2[2] == 'X':
        print("X wins")
        winvar = 1
    elif row2[0] == 'O' and row2[1] == 'O' and row2[2] == 'O':
        print("O wins")
        winvar = 1

    if colum0[0] == 'X' and colum0[1] == 'X' and colum0[2] == 'X':
        print("X wins")
        winvar = 1
    elif colum0[0] == 'O' and colum0[1] == 'O' and colum0[2] == 'O':
        print("O wins")
        winvar = 1

    if colum1[0] == 'X' and colum1[1] == 'X' and colum1[2] == 'X':
        print("X wins")
        winvar = 1
    elif colum1[0] == 'O' and colum1[1] == 'O' and colum1[2] == 'O':
        print("O wins")
        winvar = 1

    if colum2[0] == 'X' and colum2[1] == 'X' and colum2[2] == 'X':
        print("X wins")
        winvar = 1
    elif colum2[0] == 'O' and colum2[1] == 'O' and colum2[2] == 'O':
        print("O wins")
        winvar = 1

    if diagonal1[0] == 'X' and diagonal1[1] == 'X' and diagonal1[2] == 'X':
        print("X wins")
        winvar = 1
    elif diagonal1[0] == 'O' and diagonal1[1] == 'O' and diagonal1[2] == 'O':
        print("O wins")
        winvar = 1

    if diagonal2[0] == 'X' and diagonal2[1] == 'X' and diagonal2[2] == 'X':
        print("X wins")
        winvar = 1
    elif diagonal2[0] == 'O' and diagonal2[1] == 'O' and diagonal2[2] == 'O':
        print("O wins")
        winvar = 1

    i += 1

if winvar == 0:
    print("Draw")
