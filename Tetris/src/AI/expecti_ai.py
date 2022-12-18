import sys
sys.path.append("..")
from modules import expectimax
from modules import shape
from modules import sysvariables
from modules import grid
import matplotlib.pyplot as plt
import numpy as np

def expectiAI(tetris):
    SCORE = 0
    playable = True
    
    s = shape.Shape() #Initialize shape object.
    while(playable):
        actualShape = expectimax.randomShapeGenerator()
        print(f"Incoming shape:\n {actualShape}")
        input("Press Enter to continue...")
        moves = [] #reset moves
        moves = expectimax.expectimax(1,tetris,actualShape)
        if not len(moves):
            break
        chosenMove,_ = zip(*moves)
        chosenMove = chosenMove[0]
        for move,_ in moves:
            #print(move.grid)
            #print(move.score)
            #print("\n")
            if move.score > chosenMove.score:
                chosenMove = move

        print(f"Chosen move: {chosenMove.grid}")
        tetris = chosenMove
        #tetris.grid[tetris.grid == 2] = 1
        #print(f"Grid state:\n {tetris.grid}")
        SCORE += 1
    print(f"Expectimax AI final score: {SCORE}")
    return SCORE


if __name__ == "__main__":
    print("Enter Row and Col size with spaces ex. 6 6")
    R,C = input().split()
    tetris = grid.Grid(int(R),int(C)) #Set grid size.
    
    valid = [float('inf')]
    print(tetris.grid)

    expectiAI(tetris)