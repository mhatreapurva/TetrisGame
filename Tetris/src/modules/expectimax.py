import numpy as np
import random
from modules import shape as s
from modules import grid
from modules import sysvariables

# Pass state into expectimax and it should be able to return the best moves for all the shapes.

"""
Rough notes:
For expectimax, we need to keep doing max->chance->max->chance.

we also need a scoring function
"""


def baseAI(state):
    if state is None: return -1
    R,C = state.shape
    r,c = [],[]
    r,c = np.nonzero(state)
    score = 0
    score = r
    if len(r):
        score = min(r) #Keep the blocks as low as possible
    else:
        score = r
    return score

def score(state): #Computing the heuristic for each state.
    if state is None: return -1
    R,C = state.shape
    r,c = [],[]
    r,c = np.nonzero(state)
    score = 0
    #score = r
    # if len(r):
    #     score = min(r) #Keep the blocks as low as possible
    # else:
    #     score = r
    
    #print(f"State: {state}")
    # t = s.Shape()
    # for currShape in t.shapearr:
    #     score += len(t.validPositions(shape = currShape,GRID = state))
    # return score

    #Compute aggregate height.
    height = {}
    tot = 0
    #print(state)
    #print(r,c)
    if len(c):
        for idx in range(len(c)):
            if idx not in height:
                height[idx] = R - r[idx]
                tot += height[idx]
    return -0.5 * tot # penalize for more aggregate height!.



def randomShapeGenerator():
    generateShape = s.Shape()
    #shapes = [generateShape.O,generateShape.I]
    #return np.random.choice(shapes,1,p=[0.5,0.5])[0]
    return np.random.choice(generateShape.shapearr,1,p=[0.3,0.2,0.1,0.4])[0]

def generateChildren(shape,state):
    ROW, COL = state.shape
    a,b = np.nonzero(shape)
    pos = np.array(list(zip(a,b)))
    t = s.Shape()
    valid = t.validPositions(shape,state)
    children = []
    
    for row, col in valid: # Assume only valid actions are returned.
        cache = state.copy()
        for a,b in pos:
            cache[row + a][col + b] = shape[a,b]
        currGrid = grid.Grid(ROW,COL)
        currGrid.grid = cache
        children.append((currGrid,shape))
    
    return children, len(valid) 

def helper(grid,shape): #helper to generate children.
    if grid is None: return
    return generateChildren(shape,grid.grid)
    

def expectimax(depth,grid,shape):
    t = s.Shape()
    if depth == 0:
        grid.score += score(grid.grid)
        return
    children, sco = (generateChildren(shape = shape,state = grid.grid))
    grid.children.extend(children)
    grid.score += score(grid.grid)
    #print(f"depth: {depth}") 
    for currChild,_ in grid.children:
        currChild.maxP = not grid.maxP
        currChild.score = grid.score #Children inherit the parents score.
        for i in t.shapearr:
            expectimax(depth - 1,currChild,i)
            sysvariables.NODES += 1
    
    #Bottom up.
    if grid.maxP: #MaxPlayer
        maxScore = grid.score
        for g,_ in grid.children:
            maxScore = max(g.score,maxScore)
        grid.score = maxScore

    elif not grid.maxP: #Chance player (M + C)
        N = len(grid.children)
        tot = 0
        shapeDict = {}
        if N:
            for g,shape in grid.children:
                if shape.tobytes() not in shapeDict:
                    shapeDict[shape.tobytes()] = g.score
                else:
                    shapeDict[shape.tobytes()] = max(g.score, shapeDict[shape.tobytes()])
            t = s.Shape()
            for k,v in shapeDict.items():
                tot += shapeDict[k] * t.shapeProb[k] #Score based on probabilities.
            grid.score = tot
        else: grid.score = 0
    return children


                




