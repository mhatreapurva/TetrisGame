import sys
sys.path.append("..")
from modules import expectimax
from modules import shape
from modules import sysvariables
from modules import grid
import matplotlib.pyplot as plt
import numpy as np


def human(tetris):
    SCORE = 0
    s = shape.Shape() #Initialize shape object.
    while (True):
        currShape = expectimax.randomShapeGenerator()
        print(f"Incoming shape:\n {currShape}\n")
        input("Press Enter to continue...")
        valmoves = s.validPositions(shape = currShape, GRID=tetris.grid)
        if not len(valmoves):
            print("Game over")
            break
        print("Choose a move(eg. An index postion from the below array (0,1,2,3...etc..))")
        print(valmoves)
        idx = int(input())
        print(f"Chosen move: {valmoves[idx]}")
        tetris.grid = s.playerMove(currShape,tetris.grid,[valmoves[idx]])
        print(f"Current grid:\n {tetris.grid} \n")
        SCORE+= 1

    print(f"Final score: {SCORE}")

if __name__ == "__main__":

    print("Enter Row and Col size with spaces ex. 6 6")
    R,C = input().split()
    tetris = grid.Grid(int(R),int(C)) #Set grid size.
    valid = [float('inf')]
    print(tetris.grid)
    human(tetris)
