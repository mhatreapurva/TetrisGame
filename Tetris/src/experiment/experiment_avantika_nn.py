import sys
sys.path.append("..")
from modules import expectimax
from modules import shape
from modules import sysvariables
from modules import grid
import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append("..")
from modules import expectimax
from modules import shape
from modules import sysvariables
from modules import grid
import matplotlib.pyplot as plt
import numpy as np
import torch as tr

DATASET = []

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
            #print(move.grid,move.score)
            DATASET.append((move.grid,move.score))
        #print(f"Chosen move: {chosenMove} : {chosenMove.score}")
        tetris = chosenMove
        #tetris.grid[tetris.grid == 2] = 1
        #print(f"Grid state:\n {tetris.grid}")
        SCORE += 1
    #print(f"Expectimax AI final score: {SCORE}")
    return SCORE


def nnAI(tetris,net):
    s = shape.Shape()
    SCORE = 0
    NN_NODES = 0
    playable = True
    argBig = tuple((0,0))
    while(playable):
        actualShape = expectimax.randomShapeGenerator()
        #print(f"Incoming shape:\n {actualShape}")
        #input("Press Enter to continue...")
        moves = [] #reset moves
        children, _ = expectimax.generateChildren(shape = actualShape,state = tetris.grid)
        if children is None or not len(children):
            playable = False
            break
        

        best = (0,float('+inf'))
        for grid in children:
            currInput = tr.Tensor(grid[0].grid)
            currInput = currInput.reshape(1,25)
            #print(type(currInput))
            score = net(currInput)
            if score < best[1]:
                best = (grid[0].grid, score)
        tetris.grid = best[0]
        #print(f"Grid state:\n {tetris.grid}")
        SCORE += 1
        NN_NODES += len(children)
    #print(f"Neural Networl AI final score: {SCORE}")
    return SCORE,NN_NODES

def generateNN():
    print("********* Neural Network 1 * 5 x 5 grid * All shapes have same probabilities * depth = 2 **********")
    scoreKeeper = 0
    TOTAL = 2000
    expectiAIScores = []
    baseAIScores = []
    ExpectiAINodes = []
    baseAINodes = []
    depth = 2 # 3 steps, including root
    for i in range(TOTAL):
        sysvariables.NODES = 0 #Reset node counter
        if (i % 200) == 0:
            print(f'Percent complete: {i/TOTAL * 100}')
        tetris = grid.Grid(5,5)
        curr = expectiAI(tetris = tetris,depth = 1)
        expectiAIScores.append(curr)
        ExpectiAINodes.append(sysvariables.NODES)
        scoreKeeper += curr

    print(f'Data points collected: {len(DATASET)}')


    import torch as tr
    dataset_state = []
    dataset_utilities = []
    for a,c in DATASET:
        dataset_state.append(tr.Tensor(a))
        dataset_utilities.append(-1*c)

    SIZE = int(len(DATASET) * 0.8)
    print(f'size of training dataset: {SIZE}')
    print(f'size of testing dataset: {len(DATASET) - SIZE}')

    training_examples = []
    testing_examples = []
    training_examples.append(dataset_state[:SIZE])
    testing_examples.append(dataset_state[SIZE:])

    training_examples.append(dataset_utilities[:SIZE])
    testing_examples.append(dataset_utilities[SIZE:])


    class LinNet(tr.nn.Module):
        def __init__(self, size, hid_features):
            super(LinNet, self).__init__()
            self.to_hidden = tr.nn.Linear(5*size, hid_features)
            self.to_output = tr.nn.Linear(hid_features, 1)
        def forward(self, x):
            h = tr.sigmoid(self.to_hidden(x.reshape(x.shape[0],-1)))
            y = tr.relu(self.to_output(h))
            return y
        def __del__(self):
            print ("Destructor")

    def batch_error(net, batch):
        states, utilities = batch
        #print(utilities)
        u = utilities.reshape(-1,1).float()
        #print(u)
        y = net(states)
        e = tr.sum((y - u)**2) / utilities.shape[0]
        return e



    # whether to loop over individual training examples or batch them
    batched = True

    # Make the network and optimizer
    net = LinNet(size=5, hid_features=5)
    optimizer = tr.optim.SGD(net.parameters(), lr=0.002)

    # Convert the states and their minimax utilities to tensors
    
    states, utilities = training_examples
    training_batch = tr.stack(states), tr.tensor(utilities)

    states, utilities = testing_examples
    testing_batch = tr.stack(states), tr.tensor(utilities)

    # Run the gradient descent iterations
    curves = [], []
    for epoch in range(20000):
    
        # zero out the gradients for the next backward pass
        optimizer.zero_grad()

        # batch version (fast)
        if batched:
            e = batch_error(net, training_batch)
            e.backward()
            training_error = e.item()

            with tr.no_grad():
                e = batch_error(net, testing_batch)
                testing_error = e.item()

        # take the next optimization step
        optimizer.step()    
        
        # print/save training progress
        if epoch % 1000 == 0:
            print("%d: %f, %f" % (epoch, training_error, testing_error))
        curves[0].append(training_error)
        curves[1].append(testing_error)

    print("Neural network ready!")

    return net







if __name__ == "__main__":

    net = generateNN()
    
    #print("********* Experiment NN * 5 x 5 grid * All shapes have same probabilities * depth = 2 **********")
    
    TOTAL = 100
    NNScores = []
    
    NNNodes = []
    
    for i in range(TOTAL):
        
        print(f"Simulation number expectimax AI: {i}")
        tetris = grid.Grid(5,5)
        score, nodes = nnAI(tetris,net)
        NNScores.append(score)
        NNNodes.append(nodes)

        



    print(f"********* NN score avg: {sum(NNScores)/len(NNScores)}")
    print(f"********* NN Nodes avg: {sum(NNNodes)/len(NNNodes)}")
    print("\n\n\n\n")

    

    x = NNScores
    plt.title("NN Scores Experiment - Avantika")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()

    x = NNNodes
    plt.title("NN Nodes Experiment - Avantika")
    plt.style.use('ggplot')
    plt.hist(x, bins=15)
    plt.show()


