# Shape generation package
from ast import List
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from modules import expectimax

#Tetris/src/grid/Grid.py
#pygame



#Definition for Tetris shapes:
#https://en.wikipedia.org/wiki/Tetromino


class Shape:
    def __init__(self):
        self.O = np.array([[1,1],[2,2]]) # --> Tested
        self.I = np.array([[2,2,2,2]]) # --> Tested
        self.T = np.array([[2,1,2],[0,2,0]]) # --> Tested
        self.J = np.array([[0,1],[0,1],[2,2]]) # --> Tested
        self.L = np.array([[1,0],[1,0],[2,2]]) # --> Tested
        self.S = np.array([[0,1,2],[2,2,0]]) # --> Tested
        self.Z = np.array([[2,1,0],[0,2,2]])
        self.shapearr = [self.O,self.I,self.T,self.J, self.L, self.S, self.Z]    

    def validPositions(self, shape, GRID): #No of children's
        # returns set of positions where the block can be fixed
        ROW, COL = GRID.shape
        #print(f"Shape: {GRID.shape}")
        a,b = np.nonzero(shape) # a -> row | b-> col indices.
        #returns positions that need to be 0.
        pos = np.array(list(zip(a,b))) #tuple of arrays --> array of tuples.
        valid = []
        for row in range(ROW-1,-1,-1):
            for col in range(COL-1,-1,-1): #Traverse through the grid.
                if all([a+row < ROW for a,_ in pos]) and all([b+col < COL for _,b in pos]) and all([GRID[a + row][b + col] == 0 for a,b in pos]):

                    baseBlocks = np.argwhere(shape > 1)
                    #print(f"ROW:{row} COL:{col} baseBlocks:{baseBlocks}")
                    check = True
                    for a,_ in baseBlocks:
                        if a + row + 1 == ROW:
                            valid.append((row,col))
                            check = False
                            break

                    if check:
                        if any([GRID[a + row + 1][b + col] == 1 for a,b in baseBlocks]):
                            valid.append((row,col))
        return valid

    def printGridStates(self,shape,GRID):
        #Prints all the valid sets.
        ROW, COL = GRID.shape
        a,b = np.nonzero(shape)
        pos = np.array(list(zip(a,b)))
        valid = self.validPositions(shape,GRID)
        ctx = 1
        for row, col in valid: # Assume only valid actions are returned.
            cache = GRID.copy()
            for a,b in pos:
                #cache[row + a][col + b] = shape[a,b]
                cache[row + a][col + b] = 1
            #print(f"Valid move: {ctx}\n")
            #print(f"State score: {expectimax.score(state = cache)}") #Each grid is a state.
            self.plotState(shape,cache)
            print(f"\n")
            ctx += 1

    def plotState(self,shape,GRID):
        row,col = GRID.shape
        print(GRID)
        cmap = colors.ListedColormap(['white','black']) # blue -> 0 red -> 1 black -> already present.
        plt.figure(figsize=(col,row)) 
        plt.pcolor(np.fliplr(np.flip(GRID)),cmap = cmap,edgecolors='black', linewidths=1)
        plt.show()
        plt.close()