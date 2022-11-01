import imp
from unittest import result
import numpy as np
from modules.Shape import Shape

def score(state):
    # state == grid
    magnitude = max(state.shape[0],state.shape[1])
    #magnitude = state.shape[0]
    MAX_ROW,MAX_COL = np.nonzero(state) 
    if np.count_nonzero == 0 or len(MAX_ROW) == 0: MAX_ROW = [0]
    print(f"MAX_ROW: {MAX_ROW} --> {min(MAX_ROW)}")
    magnitude += min(MAX_ROW) #push as below as possible!
    print(f"magnitude:{magnitude}")
    return state,magnitude

def children_of(state,shape):
    T = Shape()
    children = T.validGridStates(shape = shape,GRID = state)
    return children

def maxFunc(state,shape):
    children = children_of(state,shape) # returns all valid children of current state.
    #value = score(state)

    #if value == 0 or len(children) == 0: return None, value
    if len(children) == 0: return None, 0

    #results = list(map(maxFunc(children,shape),children))
    #results = [maxFunc(child,shape) for child in children]
    #print(f"results:\n{results}")
    # _,utilities = zip(*results)
    # action_index = np.argmax(utilities)
    # return children[action_index],utilities[action_index]

    results = [score(child) for child in children] # non-recursive.
    print(f"results: {results}")
    _,utilities = zip(*results)
    print(f"_:{_} \n utilities:{utilities}")
    action_index = np.argmax(utilities)
    return children[action_index],utilities[action_index]


    

