from modules import node
from modules import shape
from modules import grid
from modules import expectimax
from modules import sysvariables

import numpy as np

import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

tetris = grid.Grid(5,5)

tetris.grid = np.array([
    [0., 0., 0., 0., 0.],
    [0., 1., 0., 0., 0.],
    [0., 1., 0., 0., 0.],
    [1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 0.]]) #Overriding to provide randomness.


shape = shape.Shape()
#print(shape.validPositions(shape.J,tetris.grid))
#shape.printGridStates(shape.J,tetris.grid)

# for i in range(10):


#tetris.children = expectimax.generateChildren(shape=shape.I,state=tetris.grid)
#tetris.children.extend(expectimax.expectimax(2,tetris,shape.O))
expectimax.expectimax(1,tetris,shape.T)
#tetris.children.extend(expectimax.expectimax(float('inf'),tetris,shape.I))

#expectimax.expectimax(4,tetris,shape.O) #P.S note actual depth is one more, since we skip root node while passing the parameter.

#expectimax.expectimax(2,tetris,shape.I)
# print(tetris.score)
# print(type(tetris.children))
# print(type(tetris.children[0]))
# print(type(tetris.children[1]))
# g,_ = tetris.children
# print(type(tetris.children))
# for gr,sco in g:
#     print(f"Grid:\n {gr.grid} \tscore:{gr.score}")

g,_ = zip(*tetris.children)

print(tetris.score)
print("************************DEBUG************************")
for i in g:
    print(i.grid)
    print(i.score)
print("******INDIVIDUAL EXPERIMENT*******")
FIRST = g[0]
print("PARENT")
print(FIRST.grid)
print(FIRST.score)
print(f"Am I max player: {FIRST.maxP}")

print("Children")
for g,_ in FIRST.children:
     print(f"Grid:\n {g.grid} \tscore:{g.score}")
     print(f"Am I max player: {g.maxP}")

# print(f"Total exploration index: {sysvariables.NODES}")

# # Find the best for the s0
# #print(expectimax.score())

# print(shape.validPositions(shape = shape.O,GRID = np.array([[0,0,0,1,1],[0,0,0,1,1]])))

# print("Playing the game.....\n")
# print(f"Initial Grid:\n {tetris.grid} ")
# playable = True

# argmax = (0,0)
# while(playable):
#     actualShape = expectimax.randomShapeGenerator()
#     moves = [] #reset moves
#     moves = expectimax.expectimax(1,tetris,actualShape)
#     if not len(moves):
#         playable = False
#         break
#     ctx = 0
#     for move,_ in moves:
#         if move.score > argmax[1]:
#             argmax = (ctx,move.score)
#         ctx += 1
#     chosenMove,_ = moves[argmax[0]]
#     tetris = chosenMove
#     tetris.grid[tetris.grid == 2] = 1
#     print(f"Incoming shape:\n {actualShape}")
#     print(f"New state after playing move: \n")
#     print(tetris.grid)
#     print("\n")
#     #shape.plotState(shape = None, GRID = tetris.grid)

# print(shape.shapearr)