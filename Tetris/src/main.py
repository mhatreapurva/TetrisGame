from modules import node
from modules import shape
from modules import grid
from modules import expectimax
from modules import sysvariables

import numpy as np

tetris = grid.Grid(10,10)

#tetris.grid = np.array([[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.]]) #Overriding to provide randomness.


shape = shape.Shape()
# print(shape.validPositions(shape.J,tetris.grid))
# shape.printGridStates(shape.J,tetris.grid)

# for i in range(10):


#tetris.children = expectimax.generateChildren(shape=shape.I,state=tetris.grid)
#tetris.children.extend(expectimax.expectimax(float('inf'),tetris,shape.O))

#tetris.children.extend(expectimax.expectimax(float('inf'),tetris,shape.I))

#expectimax.expectimax(4,tetris,shape.O) #P.S note actual depth is one more, since we skip root node while passing the parameter.

#expectimax.expectimax(2,tetris,shape.I)

# for g,_ in tetris.children:
#      print(f"Grid:\n {g.grid} \tscore:{g.score}")

# g,_ = zip(*tetris.children)

# print(tetris.score)
# print("************************DEBUG************************")
# # # for i in g:
# # #     print(i.grid)

# FIRST = g[0]
# print("PARENT")
# print(FIRST.grid)
# print(FIRST.score)
# print(f"Am I max player: {FIRST.maxP}")

# print("Children")
# for g,_ in FIRST.children:
#      print(f"Grid:\n {g.grid} \tscore:{g.score}")
#      print(f"Am I max player: {g.maxP}")

# print(f"Total exploration index: {sysvariables.NODES}")

# # Find the best for the s0
# #print(expectimax.score())

# print(shape.validPositions(shape = shape.O,GRID = np.array([[0,0,0,1,1],[0,0,0,1,1]])))

print("Playing the game.....")
playable = True

argmax = (0,0)
while(playable):
    actualShape = expectimax.randomShapeGenerator()
    moves = [] #reset moves
    moves = expectimax.expectimax(2,tetris,actualShape)
    if not len(moves):
        playable = False
        break
    ctx = 0
    for move,_ in moves:
        if move.score > argmax[1]:
            argmax = (ctx,move.score)
        ctx += 1
    chosenMove,_ = moves[argmax[0]]
    tetris = chosenMove
    tetris.grid[tetris.grid == 2] = 1
    print(tetris.grid)
    shape.plotState(shape = None, GRID = tetris.grid)

print(shape.shapearr)