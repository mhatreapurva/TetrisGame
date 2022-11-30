from modules import node
from modules import shapes
import numpy as np

tetris = node.Node(4,5)
print(tetris.score)
tetris.grid = np.array([[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[1., 0., 0., 0., 1.]])

shape = shapes.Shape()
print(shape.validPositions(shape.J,tetris.grid))
shape.printGridStates(shape.J,tetris.grid)