from modules import node
from modules import shape
from modules import grid
from modules import expectimax
from modules import sysvariables
import matplotlib.pyplot as plt

import numpy as np



def expectiAI(tetris,depth):
    SCORE = 0
    playable = True
    argBig = tuple((0,0))
    while(playable):
        actualShape = expectimax.randomShapeGenerator()
        moves = [] #reset moves
        moves = expectimax.expectimax(depth = depth,grid = tetris,shape = actualShape)
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
    NODES = 0
    while(playable):
        actualShape = expectimax.randomShapeGenerator()
        moves = [] #reset moves
        children, _ = expectimax.generateChildren(shape = actualShape,state = tetris.grid)
        NODES += len(children)
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
    return SCORE,NODES


if __name__ == "__main__":

    """
    Replace self.shapeProb in shape.py with the below, this is what we used!
    self.shapeProb = {
            self.O.tobytes() : 0.25,
            self.I.tobytes() : 0.25,
            self.T.tobytes() : 0.25,
            self.J.tobytes() : 0.25,
        } 
    
    """
    
    print("********* Experiment 1 * 8 x 8 grid * All shapes have same probabilities * depth = 2 **********")
    scoreKeeper = 0
    TOTAL = 100
    expectiAIScores = []
    baseAIScores = []
    ExpectiAINodes = []
    baseAINodes = []
    depth = 2 # 3 steps, including root
    print("\n\nEXPECTIMAX AI\n\n")
    for i in range(TOTAL):
        sysvariables.NODES = 0 #Reset node counter
        print(f"Simulation number expectimax AI: {i}")
        tetris = grid.Grid(8,8)
        curr = expectiAI(tetris = tetris,depth = 2)
        expectiAIScores.append(curr)
        ExpectiAINodes.append(sysvariables.NODES)
        scoreKeeper += curr
    

    ExpectiAI = scoreKeeper / TOTAL
    

    print("\n\nBASELINE AI\n\n")

    scoreKeeper = 0
    TOTAL = 100
    for i in range(TOTAL):
        print(f"Simulation number baseline AI: {i}")
        tetris = grid.Grid(8,8)
        curr, nodes = baseAI(tetris)
        baseAINodes.append(nodes)
        baseAIScores.append(curr)
        scoreKeeper += curr
        
    
    BaseAI = scoreKeeper / TOTAL


    print(f"********* ExpectiAI score avg: {ExpectiAI} BaseAI score avg: {BaseAI} *********")
    print(f"********* ExpectiAI Nodes avg: {sum(ExpectiAINodes)/len(ExpectiAINodes)} BaseAI Nodes avg: {sum(baseAINodes)/len(baseAINodes)} *********")
    print("\n\n\n\n")

    

    x = expectiAIScores
    plt.title("Expectimax Scores Experiment 1")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()

    x = baseAIScores

    plt.title("Baseline AI Scores Experiment 1")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()

    x = ExpectiAINodes
    plt.title("Expectimax Nodes Experiment 1")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()

    x = baseAINodes

    plt.title("Baseline AI Nodes Experiment 1")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()

