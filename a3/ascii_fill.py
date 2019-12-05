# COMP 1405 Assignment 5
# Name: John Appleseed
# Student number: 1010XXXXX

def main():
    board = readLevel(1)
    displayBoard(board)
    input = getUserAction(len(board), len(board[0]))
    print(str(input[1]))
    print(str(input[2]))
    fill(board, board[int(input[1])][int(input[2])], input[0], input[1], input[2])



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
    count = 0
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
    return [symbol, row, col]

def fill(board, strT, strS, intR, intC):
    print("lmao")



main()