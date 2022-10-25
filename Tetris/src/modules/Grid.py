import numpy as np

class Grid:
    def __init__(self,row = 5,col = 5):
        self.ROW = row
        self.COL = col
        self.GRID = np.zeros((self.ROW,self.COL),dtype=int)
        self.SHAPE = (self.ROW, self.COL)
    
    def printGrid(self):
        print(self.GRID)
        

        