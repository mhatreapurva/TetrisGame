import numpy as np
import random
from modules import shape

# Pass state into expectimax and it should be able to return the best moves for all the shapes.

"""
Rough notes:
For expectimax, we need to keep doing max->chance->max->chance.

we also need a scoring function
"""

class Expectimax:
    _ = ""

    def score(self,state):
        if state is None: return -1
        R,C = state.shape
        r,c = np.nonzero(state)
        print(f"r:{r} c:{c}")
        score = min(r) #Keep the blocks as low as possible
        return score
    
    def expectimax(self,state,depth = 1):
        return None
    
    def randomShapeGenerator():
        generateShape = shape.Shape()
        shapes = [generateShape.O,generateShape.I]
        return np.random.choice(shapes,1,p=[0.5,0.5])[0]




