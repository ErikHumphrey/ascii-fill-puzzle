# COMP 1405 Assignment 5
# Name: John Appleseed
# Student number: 1010XXXXX

def main():
    totalMoves = 0
    for i in range(1, 6):
        board = readLevel(i)
        displayBoard(board)
        complete = 0
        moves = 0
        while complete == 0:
            moves = moves + 1
            action = getUserAction(len(board), len(board[0]))
            fill(board, board[int(action[1])][int(action[2])], action[0], action[1], action[2])
            displayBoard(board)
            complete = 1
            for line in board:
                for char in line:
                    if char != action[0]:
                        complete = 0
        totalMoves = totalMoves + moves
        print("Level " + str(i) + " Completed in " + str(moves) + " moves!")
    print("You Win! Thanks for playing!")
    print("Total moves: " + str(totalMoves))
    playAgain = input("Would you like to play again? (y/n): ")
    if (playAgain == "y" or playAgain == "yes"):
        main()

def readLevel(num) -> list:
    try:
        with open("levels/ascii_fill_level" + str(num) + ".txt", "r") as file:
            array = [list(line.strip()) for line in file]
            return(array)
    except:
        print("Error reading file levels/ascii_fill_level" + str(num) + ".txt")
        exit()

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
        board[intR][intC] = strS
        fill(board, strT, strS, intR + 1, intC)
        fill(board, strT, strS, intR - 1, intC)
        fill(board, strT, strS, intR, intC + 1)
        fill(board, strT, strS, intR, intC - 1)



main()