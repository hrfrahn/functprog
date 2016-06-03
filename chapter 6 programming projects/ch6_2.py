# harrison frahn
# period 2
# chapter 6.2
# expected input: the number of rows/columns to draw(an int)
from math import floor
def drawPlusrow(n):
        for i in range(n):
                print("+ - - - - ",end="")
        print("+")
def drawOtherRow(n):
        for i in range(n):
                print("|         ",end="")
        print("|")
def drawGrid(n):
        for i in range(n):
                drawPlusrow(n)
                for i in range(4):
                        drawOtherRow(n)
        drawPlusrow(n)
def main():
        print("This program draws grids.")
        drawGrid(2)
        n = eval(input("How many rows/columns should the next grid have? Enter one integer: "))
        drawGrid(n)
main()
