# Shape generation package
from ast import List
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from modules import expectimax
from scipy import signal
from collections import defaultdict
#Tetris/src/grid/Grid.py
#pygame



#Definition for Tetris shapes:
#https://en.wikipedia.org/wiki/Tetromino


class Shape:
    def __init__(self):
        self.O = np.array([[1,1],[1,1]]) # --> Tested
        self.I = np.array([[1,1,1,1]]) # --> Tested
        self.T = np.array([[1,1,1],[0,1,0]]) # --> Tested
        self.J = np.array([[0,1],[0,1],[1,1]]) # --> Tested
        self.L = np.array([[1,0],[1,0],[1,1]]) # --> Tested
        self.S = np.array([[0,1,1],[1,1,0]]) # --> Tested
        self.Z = np.array([[1,1,0],[0,1,1]])
        self.shapearr = np.array([self.O,self.I,self.T,self.J],dtype=object)


        self.shapeProb = {
        str(self.O) : 0.25,
        str(self.I) : 0.25,
        str(self.T) : 0.25,
        str(self.J) : 0.25,
        } 

    def validPositions(self, shape, GRID): #No of children's
        # Code inspiration and credits: Professor Garrett Katz.
        if GRID is None: return []
        pos = signal.convolve2d(in1 = (1-GRID), in2= shape[::-1, ::-1],mode="valid")
        pos = np.where(pos == np.sum(shape))
        val = defaultdict(int)
        for row,col in zip(pos[0],pos[1]):
            val[col] = row
        valid = []
        for col,row in val.items():
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
            print(cache)
            print(f"\n")

    def plotState(self,shape,GRID):
        row,col = GRID.shape
        print(GRID)
        cmap = colors.ListedColormap(['white','black']) # blue -> 0 red -> 1 black -> already present.
        plt.figure(figsize=(col,row)) 
        plt.pcolor(np.fliplr(np.flip(GRID)),cmap = cmap,edgecolors='black', linewidths=1)
        plt.show()
        plt.close()
    
    def playerMove(self,shape,GRID,valid):
        ROW, COL = GRID.shape
        a,b = np.nonzero(shape)
        pos = np.array(list(zip(a,b)))
        for row, col in valid:
            cache = GRID.copy()
            for a,b in pos:
                cache[row + a][col + b] = 1
            print(f"\n")
        return cache #Return the updated grid position.