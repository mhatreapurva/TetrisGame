import numpy as np
from modules import shape as s
from modules import grid
from modules import sysvariables

# Pass state into expectimax and it should be able to return the best moves for all the shapes.

def baseAI(state): # Keeps blocks as low as possible!
    if state is None: return -1
    if np.isin(state,[0]).all(): return state.shape[0] #Max height
    return np.min(np.nonzero(state)[0])


def score(state): #Computing the heuristic for each state.
    # if state is None: return -1
    # if np.isin(state,[0]).all(): return state.shape[0] #Max height
    # return np.min(np.nonzero(state)[0])
    if state is None: return - 10
    R,C = state.shape
    r,c = [],[]
    r,c = np.nonzero(state)
    height = {}
    tot = 0
    if len(c):
        for idx in range(len(c)):
            if idx not in height:
                height[idx] = R - r[idx]
                tot += height[idx]
    return -0.5 * tot # penalize for more aggregate height!.    

def randomShapeGenerator():
    generateShape = s.Shape()
    prob = []
    for k,v in generateShape.shapeProb.items():
       prob.append(v)
    return np.random.choice(generateShape.shapearr,1,p=prob)[0]

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


def expectimax(depth,grid,shape):
    t = s.Shape()
    if depth == 0: #Leaf node! (inherited parent score + self score)
        grid.score += score(grid.grid)
        return
    children, sco = (generateChildren(shape = shape,state = grid.grid))
    grid.children.extend(children)
    grid.score += sco
    #print(f"depth: {depth}") 
    for currChild,_ in grid.children:
        currChild.maxP = not grid.maxP # Alternating chance and max player!
        currChild.score = grid.score #Children inherit the parents score.
        for i in t.shapearr:
            expectimax(depth - 1,currChild,i)
            sysvariables.NODES += 1
    
    #Bottom up.
    if grid.maxP: #MaxPlayer
        maxScore = grid.score
        #datasetShape = np.array([])
        for g,currShape in grid.children:
            #print(currShape)
            if g.score > maxScore:
                maxScore = g.score
            sysvariables.DATASET.append((g.grid,currShape,g.score))
            #print(len(sysvariables.DATASET))
        grid.score += maxScore
        
        #print(len(sysvariables.DATASET))

    elif not grid.maxP: #Chance player (M + C)
        N = len(grid.children)
        tot = 0
        shapeDict = {}
        if N:
            for g,shape in grid.children:
                if str(shape) not in shapeDict:
                    shapeDict[str(shape)] = g.score
                else:
                    shapeDict[str(shape)] = max(g.score, shapeDict[str(shape)])
            t = s.Shape()
            for k,v in shapeDict.items():
                tot += shapeDict[k] * t.shapeProb[k] #Score based on probabilities. (accounting probabilities!)
            grid.score = tot
        else: grid.score = 0
    return children


                




