# Shape generation package
from ast import List
from typing import Tuple
import numpy as np



#Tetris/src/grid/Grid.py
#pygame


"""
Definition for Tetris shapes:
https://en.wikipedia.org/wiki/Tetromino
"""
class Shape:
    def __init__(self):
        self.O = np.array([[1,1],[1,1]]) # --> Tested
        self.I = np.array([[1,1,1,1]]) # --> Tested
        self.T = np.array([[1,1,1],[0,1,0]]) # --> Tested
        self.J = np.array([[0,1],[0,1],[1,1]]) # --> Tested
        self.L = np.array([[1,0],[1,0],[1,1]]) # --> Tested
        self.S = np.array([[0,1,1],[1,1,0]]) # --> Tested
        self.Z = np.array([[1,1,0],[0,1,1]])


    def shapeDetails(self, currShape) -> None:
        print(f"shape size: {currShape.shape}")
        print(f"shape:\n{currShape}")

    def validPositions(self, shape, GRID) -> List:
        # returns set of positions where the block can be fixed
        ROW, COL = GRID.shape
        a,b = np.nonzero(shape) # a -> row | b-> col indices.
        #returns positions that need to be 0.
        pos = np.array(list(zip(a,b))) #tuple of arrays --> array of tuples.
        valid = []
        for row in range(ROW):
            for col in range(COL): #Traverse through the grid.
                if all([a+row < ROW for a,_ in pos]) and all([b+col < COL for _,b in pos]) and all([GRID[a + row][b + col] == 0 for a,b in pos]):
                    valid.append((row,col))
        return valid

    def printGridStates(self,shape,GRID):
        #Prints all the valid sets.
        ROW, COL = GRID.shape
        a,b = np.nonzero(shape)
        pos = np.array(list(zip(a,b)))
        valid = self.validPositions(shape,GRID)
        for row, col in valid: # Assume only valid actions are returned.
            cache = GRID.copy()
            for a,b in pos:
                cache[row + a][col + b] = 1
            print(f"GRID:\n{cache}")
            






        
        
        



        
        
        


        


