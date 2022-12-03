from modules import node
from modules import shape
from modules import grid
from modules import expectimax
from modules import sysvariables

import numpy as np



def expectiAI(tetris):
    SCORE = 0
    playable = True
    argBig = tuple((0,0))
    while(playable):
        actualShape = expectimax.randomShapeGenerator()
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
        SCORE += 1
    return SCORE

def baseAI(tetris):
    s = shape.Shape()
    SCORE = 0
    playable = True
    argBig = tuple((0,0))
    while(playable):
        actualShape = expectimax.randomShapeGenerator()
        moves = [] #reset moves
        children, _ = expectimax.generateChildren(shape = actualShape,state = tetris.grid)
        if children is None or not len(children):
            playable = False
            break
        

        best = (0,float('-inf'))
        for grid in children:
            score = expectimax.baseAI(grid[0].grid)
            if score > best[1]:
                best = (grid[0].grid, score)
        tetris.grid = best[0]
        SCORE += 1
    return SCORE


if __name__ == "__main__":
    scoreKeeper = 0
    TOTAL = 100
    for i in range(TOTAL):
        print(f"Simulation number: {i}")
        tetris = grid.Grid(10,10)
        scoreKeeper += expectiAI(tetris)
        #print(f"average score: {scoreKeeper/(i+1)}")
    ExpectiAI = scoreKeeper / TOTAL

    scoreKeeper = 0
    TOTAL = 100
    for i in range(100):
        print(f"Simulation number: {i}")
        tetris = grid.Grid(10,10)
        scoreKeeper += baseAI(tetris)
        #print(f"average score: {scoreKeeper/(i+1)}")
    
    BaseAI = scoreKeeper / TOTAL

    print(f"ExpectiAI score: {ExpectiAI} BaseAI score: {BaseAI}")

