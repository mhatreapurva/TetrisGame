from modules import grid
from modules import shape
from modules import expectimax #contains random shape generator. P.S.: all shapes have equal probability.




def expectiAI(tetris):
    SCORE = 0
    playable = True
    argBig = tuple((0,0))
    s = shape.Shape() #Initialize shape object.
    while(playable):
        actualShape = expectimax.randomShapeGenerator()
        print(f"Incoming shape:\n {actualShape}")
        input("Press Enter to continue...")
        moves = [] #reset moves
        moves = expectimax.expectimax(1,tetris,actualShape)
        if moves is None or not len(moves):
            playable = False
            break
        ctx = 0
        for move,_ in moves:
            if move.score > argBig[1]:
                argmax = (ctx,move.score)
            ctx += 1
        chosenMove,_ = moves[argBig[0]]
        tetris = chosenMove
        tetris.grid[tetris.grid == 2] = 1
        print(f"Grid state:\n {tetris.grid}")
        SCORE += 1
    print(f"Expectimax AI final score: {SCORE}")
    return SCORE


if __name__ == "__main__":
    print("Enter Row and Col size with spaces ex. 6 6")
    R,C = input().split()
    tetris = grid.Grid(int(R),int(C)) #Set grid size.
    
    valid = [float('inf')]
    print(tetris.grid)

    expectiAI(tetris)