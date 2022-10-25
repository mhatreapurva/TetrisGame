import sys
sys.dont_write_bytecode = True
from modules.Shape import *
import numpy as np
from modules.Grid import *

if __name__ == "__main__":
    Tetris = Grid(5,5)
    Tetris.printGrid()
    

    T = Shape()
    #T.shapeDetails(T.I)
    #T.printGridStates(T.I,Tetris.GRID)

    #Tetromino.validPositions(Tetromino.J,Tetris.GRID)
    #T.shapeDetails(T.O)
    #T.validPositions(T.O,Tetris.GRID)
    Tetris.GRID = np.array([[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]])
    T.printGridStates(T.I,Tetris.GRID)
    #T.plotState(Tetris.GRID)
    

    
    

    