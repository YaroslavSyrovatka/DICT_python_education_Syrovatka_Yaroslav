# print('X 0 X')
# print('0 X 0')
# print('X X 0')
# def stage2():
#
#     enter = input("Enter cells:")
#
#     print("---------")
#     print("| " + enter[0] + " " + enter[1] + " " + enter[2] + " |")
#     print("| " + enter[3] + " " + enter[4] + " " + enter[5] + " |")
#     print("| " + enter[6] + " " + enter[7] + " " + enter[8] + " |")
#     print("---------")
#
#
# stage2()
# def stage3():
#     enter = input("Enter cells:")
#     first = "X"
#     second = "0"
#
#
#
#     def board(enter):
#
#
#         print("---------")
#         print("| " + enter[0] + " " + enter[1] + " " + enter[2] + " |")
#         print("| " + enter[3] + " " + enter[4] + " " + enter[5] + " |")
#         print("| " + enter[6] + " " + enter[7] + " " + enter[8] + " |")
#         print("---------")
#
#
#     def chek(enter):
#         if enter[0] == enter[1] == enter[2] == first and enter[3] == enter[4] == enter[5] == second:
#             print("inposible")
#         elif enter[6] == enter[7] == enter[8] == first and enter[3] == enter[4] == enter[5] == second:
#             print("inposible")
#         elif enter[0] == enter[1] == enter[2] == second and enter[3] == enter[4] == enter[5] == first:
#             print("inposible")
#         elif enter[6] == enter[7] == enter[8] == second and enter[3] == enter[4] == enter[5] == first:
#             print("inposible")
#         elif enter[1] == enter[4] == enter[7] == first and enter[0] == enter[3] == enter[6] == second:
#             print("inposible")
#         elif enter[1] == enter[4] == enter[7] == first and enter[2] == enter[5] == enter[8] == second:
#             print("inposible")
#         elif enter[0] == enter[1] == enter[2] == second and enter[3] == enter[4] == enter[5] == first:
#             print("inposible")
#         elif enter[6] == enter[7] == enter[8] == second and enter[3] == enter[4] == enter[5] == first:
#             print("inposible")
#         elif enter[0] == "-":
#             print("Game not finished")
#         elif enter[1] == "-":
#             print("Game not finished")
#         elif enter[2] == "-":
#             print("Game not finished")
#         elif enter[3] == "-":
#             print("Game not finished")
#         elif enter[4] == "-":
#             print("Game not finished")
#         elif enter[5] == "-":
#             print("Game not finished")
#         elif enter[6] == "-":
#             print("Game not finished")
#         elif enter[7] == "-":
#             print("Game not finished")
#         elif enter[8] == "-":
#             print("Game not finished")
#         elif enter[0] == enter[1] == enter[2] == first:
#             print("X win")
#         elif enter[0] == enter[3] == enter[6] == first:
#             print("X win")
#         elif enter[3] == enter[4] == enter[5] == first:
#             print("X win")
#         elif enter[6] == enter[7] == enter[8] == first:
#             print("X win")
#         elif enter[1] == enter[4] == enter[7] == first:
#             print("X win")
#         elif enter[2] == enter[5] == enter[8] == first:
#             print("X win")
#         elif enter[0] == enter[4] == enter[8] == first:
#             print("X win")
#         elif enter[6] == enter[4] == enter[2] == first:
#             print("X win")
#         elif enter[0] == enter[1] == enter[2] == second:
#             print("0 win")
#         elif enter[0] == enter[3] == enter[6] == second:
#             print("0 win")
#         elif enter[3] == enter[4] == enter[5] == second:
#             print("0 win")
#         elif enter[6] == enter[7] == enter[8] == second:
#             print("0 win")
#         elif enter[1] == enter[4] == enter[7] == second:
#             print("0 win")
#         elif enter[2] == enter[5] == enter[8] == second:
#             print("0 win")
#         elif enter[0] == enter[4] == enter[8] == second:
#             print("0 win")
#         elif enter[6] == enter[4] == enter[2] == second:
#             print("0 win")
#         elif enter[0:8] != "-":
#             print("Draw")
#
#
#     board(enter)
#     chek(enter)
#
#
# stage3()
# stage4
one = "X"
two = "0"

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def screen():
    print("-----")
    print("|" + board[0] + board[1] + board[2] + "|")
    print("|" + board[3] + board[4] + board[5] + "|")
    print("|" + board[6] + board[7] + board[8] + "|")
    print("-----")


screen()


def plaer1():
    try:
        y, x = input("Enter the coordinates X:").split()
        y = int(y)
        x = int(x)
    except ValueError:
        print("You should enter numbers!")
        plaer1()
    else:
        if 0 < x < 4 and 0 < y < 4:
            if board[3 * (y - 1) + x - 1] != "-":
                print("This cell is occupied! Choose another one!")
                plaer1()
            else:
                board[3 * (y - 1) + x - 1] = one
                screen()
        else:
            print("Coordinates should be from 1 to 3!")
            plaer1()


def plaer2():
    try:
        y, x = input("Enter the coordinates 0:").split()
        y = int(y)
        x = int(x)
    except ValueError:
        print("You should enter numbers!")
        plaer2()
    else:
        if 0 < x < 4 and 0 < y < 4:
            if board[3 * (y - 1) + x - 1] != "-":
                print("This cell is occupied! Choose another one!")
                plaer2()
            else:
                board[3 * (y - 1) + x - 1] = two
                screen()
        else:
            print("Coordinates should be from 1 to 3!")
            plaer2()


def plaer1first():
    atempt = 0
    while atempt < 9:
        plaer1()
        atempt = atempt + 1
        if atempt < 9:
            plaer2()
            atempt = atempt + 1


def plaer2first():
    atempt = 0
    while atempt < 9:
        plaer2()
        atempt = atempt + 1
        if atempt < 9:
            plaer1()
            atempt = atempt + 1


def main():
    w = input("who start first X/0:")
    if w == "X":
        plaer1first()
    elif w == "0":
        plaer2first()


main()