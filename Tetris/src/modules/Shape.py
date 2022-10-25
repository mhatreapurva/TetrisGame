# Shape generation package
from ast import List
from collections import defaultdict
from email.policy import default
from secrets import token_bytes
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors



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
            self.plotState(shape,cache)

    def shapeColorMap(self,shape) -> str:

        colorMap = {
            self.O.tobytes() : '#f2ef21',
            self.I.tobytes() : '#21f2f2',
            self.T.tobytes() : '#f221ec',
            self.J.tobytes() : '#212ef2',
            self.L.tobytes() : '#f29321',
            self.S.tobytes() : '#64f221',
            self.Z.tobytes() : '#f23a21',
        }
        return colorMap[shape.tobytes()]
    
    def plotState(self,shape,GRID):
        row,col = GRID.shape
        cmap = colors.ListedColormap(['#fcf9f9',self.shapeColorMap(shape)]) # blue -> 0 red -> 1 black -> already present.
        plt.figure(figsize=(col,row)) #non-classic division.
        plt.pcolor(GRID,cmap=cmap,edgecolors='k', linewidths=1)
        plt.show(block = False)
        plt.pause(1)
        plt.close()
        






        
        
        



        
        
        


        


