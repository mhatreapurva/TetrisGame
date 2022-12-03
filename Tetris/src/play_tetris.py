from modules import grid
from modules import shape
from modules import expectimax #contains random shape generator. P.S.: all shapes have equal probability.

tetris = grid.Grid(10,10) #Set grid size.
s = shape.Shape() #Initialize shape object.
valid = [float('inf')]
print(tetris.grid)

SCORE = 0
while (True):
    currShape = expectimax.randomShapeGenerator()
    print(f"Incoming shape:\n {currShape}\n")
    valmoves = s.validPositions(shape = currShape, GRID=tetris.grid)
    if not len(valmoves):
        print("Game over")
        break
    print("Choose a move(start index 0)")
    print(valmoves)
    idx = int(input())
    print(f"Chosen move: {valmoves[idx]}")
    tetris.grid = s.playerMove(currShape,tetris.grid,[valmoves[idx]])
    print(f"Current grid:\n {tetris.grid} \n")
    SCORE+= 1

print(f"Final score: {SCORE}")
