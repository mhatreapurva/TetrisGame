# Tetris game

## 1. Code Attribution

### _All the code has been written by both of us, although we took inspiration from professor's Minimax Code shared on google colab_

## 2. Installation of dependencies.

``` 
pip3 install matplotlib
 
pip3 install numpy

pip3 install pandas
```

## 3. Running the interactive domain

#### Running the interactive domain is just as it was specified (run play_tetris.py)
#### 1. Choose the problem size
#### 2. Select player type human, baseline ai, expectimax tree
#### If you choose human, it will show you all the possible moves you have by displaying a list of coordinates where the shape can be placed, if you want to choose the first move enter 0 and so on until (n-1), please note there is no error handling for inputs so if there was a wrong choice pressed one needs to restart the process
#### For baseline you only need to press enter, the code pauses every move and waits for your input, same goes for expectimax AI

#### Final score is then returned once there are no valid moves remaining.

## 4. Running the experiments

#### Every experiment has its own file experiment{no}.py, run that file to run the experiment. The most important thing to note while running an experiment is, under every experiment.py file there is a if __name__ == main code block which has a comment.

#### This comment includes a code snippet, that you need to replace within shape.py file, more instructions are written under each experiment file, these code snippets change the probabilities of shapes which was given in our proposal.

#### Thank you


