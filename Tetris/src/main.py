from modules import node
from modules import shapes
import numpy as np

tetris = node.Node(4,5)
print(tetris.score)
tetris.grid = np.array([[1., 1., 0., 0., 1.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.]])

shape = shapes.Shape()
print(shape.validPositions(shape.O,tetris.grid))
shape.printGridStates(shape.O,tetris.grid)