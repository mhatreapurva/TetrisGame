import sys
sys.path.append("..")
from modules import expectimax
from modules import shape
from modules import sysvariables
from modules import grid
import matplotlib.pyplot as plt
import numpy as np





def baseAI(tetris):
    s = shape.Shape()
    SCORE = 0
    playable = True
    argBig = tuple((0,0))
    while(playable):
        actualShape = expectimax.randomShapeGenerator()
        print(f"Incoming shape:\n {actualShape}")
        input("Press Enter to continue...")
        moves = [] #reset moves
        children, _ = expectimax.generateChildren(shape = actualShape,state = tetris.grid)
        if children is None or not len(children):
            playable = False
            break
        

        best = (0,float('-inf'))
        for grid in children:
            score = expectimax.baseAI(grid[0].grid)
            if score > best[1]:
                best = (grid[0].grid, score)
        tetris.grid = best[0]
        print(f"Grid state:\n {tetris.grid}")
        SCORE += 1
    print(f"Basline AI final score: {SCORE}")
    return SCORE


if __name__ == "__main__":
    print("Enter Row and Col size with spaces ex. 6 6")
    R,C = input().split()
    tetris = grid.Grid(int(R),int(C)) #Set grid size.
   
    valid = [float('inf')]
    print(tetris.grid)

    print(baseAI(tetris))