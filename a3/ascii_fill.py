# COMP 1405 Assignment 5
# Name: John Appleseed
# Student number: 101000000

def main():
    displayBoard(readLevel(1))

def readLevel(num) -> list:
    with open("levels/ascii_fill_level" + str(num) + ".txt", "r") as file:
        array = [list(line.strip()) for line in file]
        return(array)

def displayBoard(lst):
    print("   012345678", end="\n   ---------\n")
    count = 0
    for line in lst:
        count = count + 1
        print("0" + str(count) + "|", end="")
        for letter in line:
            print(letter, end="")
        print()

main()