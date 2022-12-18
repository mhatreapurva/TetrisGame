import sys
sys.path.append("..")
from modules import expectimax
from modules import shape
from modules import sysvariables
from modules import grid
import matplotlib.pyplot as plt
import numpy as np


def expectiAI(tetris,depth):
    SCORE = 0
    playable = True
    
    s = shape.Shape() #Initialize shape object.
    while(playable):
        actualShape = expectimax.randomShapeGenerator()
        #print(f"Incoming shape:\n {actualShape}")
        #input("Press Enter to continue...")
        moves = [] #reset moves
        moves = expectimax.expectimax(depth,tetris,actualShape)
        if not len(moves):
            break
        chosenMove,_ = zip(*moves)
        chosenMove = chosenMove[0]
        for move,_ in moves:
            #print(move.grid)
            #print(move.score)
            #print("\n")
            if move.score > chosenMove.score:
                chosenMove = move

        #print(f"Chosen move: {chosenMove} : {chosenMove.score}")
        tetris = chosenMove
        #tetris.grid[tetris.grid == 2] = 1
        #print(f"Grid state:\n {tetris.grid}")
        SCORE += 1
    #print(f"Expectimax AI final score: {SCORE}")
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
    Replace self.shapeProb in modules/shape.py with the below, this is what we used!

    self.shapeProb = {
        str(self.O) : 0.4,
        str(self.I) : 0.2,
        str(self.T) : 0.1,
        str(self.J) : 0.3,
    } 
    """
    
    print("********* Experiment 3 * 5 x 5 grid  * depth = 3 **********")
    scoreKeeper = 0
    TOTAL = 100
    expectiAIScores = []
    baseAIScores = []
    ExpectiAINodes = []
    baseAINodes = []
    depth = 3 # 3 steps, including root
    print("\n\nEXPECTIMAX AI\n\n")
    for i in range(TOTAL):
        sysvariables.NODES = 0 #Reset node counter
        print(f"Simulation number expectimax AI: {i}")
        tetris = grid.Grid(5,5)
        curr = expectiAI(tetris = tetris,depth = depth-1)
        expectiAIScores.append(curr)
        ExpectiAINodes.append(sysvariables.NODES)
        scoreKeeper += curr
    

    ExpectiAI = scoreKeeper / TOTAL
    

    print("\n\nBASELINE AI\n\n")

    scoreKeeper = 0
    TOTAL = 100
    for i in range(TOTAL):
        print(f"Simulation number baseline AI: {i}")
        tetris = grid.Grid(5,5)
        curr, nodes = baseAI(tetris)
        baseAINodes.append(nodes)
        baseAIScores.append(curr)
        scoreKeeper += curr
        
    
    BaseAI = scoreKeeper / TOTAL


    print(f"********* ExpectiAI score avg: {ExpectiAI} BaseAI score avg: {BaseAI} *********")
    print(f"********* ExpectiAI Nodes avg: {sum(ExpectiAINodes)/len(ExpectiAINodes)} BaseAI Nodes avg: {sum(baseAINodes)/len(baseAINodes)} *********")
    print("\n\n\n\n")

    x = expectiAIScores
    plt.title("Expectimax Scores Experiment 3")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()

    x = baseAIScores

    plt.title("Baseline AI Scores Experiment 3")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()

    x = ExpectiAINodes
    plt.title("Expectimax Nodes Experiment 3")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()

    x = baseAINodes

    plt.title("Baseline AI Nodes Experiment 3")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()
