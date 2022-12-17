import sys
sys.path.append("..")
from modules import expectimax
from modules import shape
from modules import sysvariables
from modules import grid
import matplotlib.pyplot as plt
import numpy as np

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

if __name__ == "__main__":

    
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

def run():

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
        if epoch % 10 == 0:
            print("%d: %f, %f" % (epoch, training_error, testing_error))
        curves[0].append(training_error)
        curves[1].append(testing_error)

import matplotlib.pyplot as pt
pt.figure(figsize=(10,5))
# visualize learning curves on train/test data
pt.plot(curves[0], 'b-')
pt.plot(curves[1], 'r-')
#pt.plot([0, len(curves[1])], 'g-')
pt.plot()
pt.legend(["Train","Test"])

pt.show()


