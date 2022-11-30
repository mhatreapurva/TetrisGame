from modules import node
from modules import shape
from modules import expectimax
import numpy as np

tetris = node.Node(4,5)
print(tetris.score)
tetris.grid = np.array([[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[1., 0., 0., 0., 1.]])

shape = shape.Shape()
# print(shape.validPositions(shape.J,tetris.grid))
# shape.printGridStates(shape.J,tetris.grid)

for i in range(10):
    print(expectimax.Expectimax.randomShapeGenerator())