import sys
import random
#from prof_minimax import minimax
sys.dont_write_bytecode = True #Don't maintain cache.
from modules.Shape import *
import numpy as np
from modules.Grid import *
from modules.minimax import *

if __name__ == "__main__":

    state = Grid(6,4).GRID
    T = Shape() #initialize shape object
    #print(T.validPositions(shape = T.T,GRID = state))
    #print(T.validGridStates(shape = T.T, GRID = state))
    #x = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[3,3,3,0],[0,3,0,0]])
    #T.plotState(GRID = np.flipud(x))
    #print(state.shape)
    while state is not None:
        shape = random.choice([T.O,T.I,T.T,T.J,T.L,T.S,T.Z])
        print(f"shape:\n{shape}")
        
        #print(state)
        state, u = maxFunc(state,shape)
        print(f"state: {state}") 
        T.plotState(state)
        print(f"New state:\n {state}")
        print("\n\n\n NEW ITER")
    

    

    
    

    