from modules import node
from modules import shape
from modules import grid
from modules import expectimax
from modules import sysvariables
from AI import human,baseline_ai,expecti_ai,apurva_nn_ai,avantika_nn_ai

problem_size = [(4,4),(5,5),(6,6),(7,7),(8,8)]

print("Choose a problem size")
for i,pb in enumerate(problem_size):
    print(f"num: {i} size: {pb}")

choice = int(input())

print(f"Selecting problem size: {problem_size[choice]}")

print(f"Select 1. Human 2. Baseline AI 3. Expectimax(Tree) 4. Apurva NN 5. Avantika NN")

ptype = int(input())


tetris = grid.Grid(problem_size[choice][0],problem_size[choice][1])
print(f"start grid:\n {tetris.grid}")

if ptype == 1:
    human.human(tetris)
if ptype == 2:
    baseline_ai.baseAI(tetris)
if ptype == 3:
    expecti_ai.expectiAI(tetris)
if ptype == 4:
    print("If choosing NN, the problem size is fixed to 5 x 5")
    apurva_nn_ai.run()

if ptype == 5:
    print("If choosing NN, the problem size is fixed to 5 x 5")
    avantika_nn_ai.run()
