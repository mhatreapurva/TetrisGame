# Shape generation package
from ast import List
from collections import defaultdict
from email.policy import default
from secrets import token_bytes
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
        self.I = np.array([[2,2,2,2]]) # --> Tested
        self.T = np.array([[3,3,3],[0,3,0]]) # --> Tested
        #self.T = np.array([[0,3,0],[3,3,3]]) # --> Tested
        self.J = np.array([[0,4],[0,4],[4,4]]) # --> Tested
        #self.J = np.array([[4,4],[0,4],[0,4]])
        self.L = np.array([[5,0],[5,0],[5,5]]) # --> Tested
        #self.L = np.array([[5,5],[5,0],[5,0]]) # --> Tested
        self.S = np.array([[0,6,6],[6,6,0]]) # --> Tested
        #self.S = np.array([[6,6,0],[0,6,6]])
        self.Z = np.array([[7,7,0],[0,7,7]])
        #self.Z = np.array([[0,7,7],[7,7,0]])


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
    
    def validGridStates(self,shape,GRID):
        res = []
        print(GRID)
        ROW, COL = GRID.shape
        a,b = np.nonzero(shape)
        pos = np.array(list(zip(a,b)))
        valid = self.validPositions(shape,GRID)
        for row, col in valid: # Assume only valid actions are returned.
            cache = GRID.copy() #deep copy
            for a,b in pos:
                cache[row + a][col + b] = np.amax(shape)
            res.append(cache)
        return np.array(res)
        

    def shapeColorMap(self,maxNum) -> str:

        colorMap = {
            1 : '#f2ef21',
            2 : '#21f2f2',
            3 : '#f221ec',
            4 : '#212ef2',
            5 : '#f29321',
            6 : '#64f221',
            7 : '#f23a21',
        } #redundant
        return colorMap[maxNum]
    
    def plotState(self,GRID):
        if type(GRID) == None: return
        import matplotlib.pyplot as plt
        from matplotlib import colors
        currGRID = GRID.copy()
        currGRID = np.flipud(currGRID) 
        row,col = currGRID.shape
        #cmap = colors.ListedColormap(['#fcf9f9',self.shapeColorMap(shape)]) # blue -> 0 red -> 1 black -> already present.
        cmap = colors.ListedColormap(['#fcf9f9','#f2ef21','#21f2f2','#f221ec','#212ef2','#f29321','#64f221','#f23a21']) 
        plt.figure(figsize=(col,row)) #non-classic division.
        plt.pcolor(currGRID,cmap=cmap,edgecolors='k', linewidths=2,vmin=0,vmax=7)
        #plt.show(block = False)
        #plt.pause(2)
        #plt.close()
        plt.show()
        






        
        
        



        
        
        


        


