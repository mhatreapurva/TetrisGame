import numpy as np
import sys
sys.path.append("..")
from modules import shape as s
from modules import grid
from scipy import signal
from modules import expectimax


TETRIS = np.array([
    [0,0,0,0,0],
    [0,0,1,0,0],
    [1,0,0,0,1]
])

currShape = np.array([[1,1,1],[0,1,0]])
#print(expectimax.randomShapeGenerator())
print(hash(currShape.tobytes()))

generateShape = s.Shape()
#shapes = [generateShape.O,generateShape.I]
#return np.random.choice(shapes,1,p=[0.5,0.5])[0]
prob = []
print(len(generateShape.shapeProb))
for k,v in generateShape.shapeProb.items():
    prob.append(v)
#print("C1")
print(prob)
print(np.random.choice(generateShape.shapearr,4,p=prob))
