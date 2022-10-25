import sys
sys.dont_write_bytecode = True
from modules.Shape import *
import numpy as np
from modules.Grid import *

if __name__ == "__main__":
    Tetris = Grid(2,4)
    Tetris.printGrid()
    

    T = Shape()
    #T.shapeDetails(T.I)
    #T.printGridStates(T.I,Tetris.GRID)

    #Tetromino.validPositions(Tetromino.J,Tetris.GRID)
    T.shapeDetails(T.O)
    #T.validPositions(T.O,Tetris.GRID)
    T.printGridStates(T.O,Tetris.GRID)
    

    
    

    