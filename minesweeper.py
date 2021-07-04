#Start of minesweeper code
def minesweeper(n):
    arr = [[0 for row in range(n)] for column in range(n)]
    for row in arr:
        print(" ".join(str(cell) for cell in row))
        print("")


grid_size = input("Size of grid")

minesweeper(int(grid_size))

import random

