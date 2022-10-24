import numpy as np

class Grid(object):
    ROW = 0
    COL = 0
    GRID = [ROW][COL] #default.
    def __init__(self,row,col):
        self.ROW = row
        self.COL = col
        self.GRID = np.zeros((self.ROW,self.COL),dtype=int)
    
    def printGrid(self):
        print(self.GRID)

        