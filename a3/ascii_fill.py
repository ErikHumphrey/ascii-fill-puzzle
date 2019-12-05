# COMP 1405 Assignment 5
# Name: John Appleseed
# Student number: 1010XXXXX

def main():
    for i in range(1, 6):
        print(i)
        board = readLevel(i)
        displayBoard(board)
        complete = 0
        while complete == 0:
            input = getUserAction(len(board), len(board[0]))
            fill(board, board[int(input[1])][int(input[2])], input[0], input[1], input[2])



    displayBoard(board)

def readLevel(num) -> list:
    with open("levels/ascii_fill_level" + str(num) + ".txt", "r") as file:
        array = [list(line.strip()) for line in file]
        return(array)

def displayBoard(lst):
    count = -1
    print("   ", end="")
    for char in lst[0]:
        count = (count + 1) % 10
        print(count, end="")
    print("\n   ---------")
    count = -1
    for line in lst:
        count = count + 1
        print("{0:0=2d}".format(count) + "|", end="")
        for char in line:
            print(char, end="")
        print()

def getUserAction(h, w) -> list:
    symbol = input("Enter a symbol: ")
    row = input("Select a row [0," + str(h) + "]: ")
    col = input("Select a col [0," + str(w) + "]: ")
    return [symbol, int(row), int(col)]

def fill(board, strT, strS, intR, intC):
    # print("DEBUG: Trying to replace '" + strT + "'s near [" + str(intR) + "," + str(intC) + "] with '" + strS + "'...")
    if (intR < len(board) and intC < len(board[0]) and strT == board[intR][intC] and strT != strS):
        print(str(intR) + " < height: " + str(len(board)) + ", " + str(intC) + " < length:" + str(len(board[0])))
        board[intR][intC] = strS
        fill(board, strT, strS, intR + 1, intC)
        fill(board, strT, strS, intR - 1, intC)
        fill(board, strT, strS, intR, intC + 1)
        fill(board, strT, strS, intR, intC - 1)



main()