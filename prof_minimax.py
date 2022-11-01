# Minimax to solve tic-tac-toe
# state[r,c] is the content at position (r,c) of the board: "_", "X", or "O"
# TODO: implement base case (watch out for draws and early wins)
# TODO: compare with XKCD solution, do they match? Why or why not?
# TODO: modify magnitudes of non-zero scores for more reasonable behavior
import numpy as np

def state_string(state):
    return "\n".join(["".join(row) for row in state])

def score(state):
    magnitude = state.shape[0] * state.shape[1] + 1
    magnitude -= (state != "_").sum() # lower score when the game took longer
    # TODO: modify magnitude to influence behavior

    for player, value in (("X", magnitude), ("O", -magnitude)):
        if (state == player).all(axis=0).any(): return value
        if (state == player).all(axis=1).any(): return value
        if (np.diag(state) == player).all(): return value
        if (np.diag(np.rot90(state)) == player).all(): return value
    return 0

def get_player(state):
    return "XO"[np.count_nonzero(state == "O") < np.count_nonzero(state == "X")]

def children_of(state):
    symbol = get_player(state)
    children = []
    for r in range(state.shape[0]):
        for c in range(state.shape[1]):
            if state[r,c] == "_":
                child = state.copy()
                child[r,c] = symbol
                children.append(child)
    return children

def minimax(state):
    # returns chosen child state, utility
    player = get_player(state)
    children = children_of(state)

    # TODO: fix base case
    value = score(state)
    if value != 0 or len(children) == 0: return None, value

    # recursive case
    results = list(map(minimax, children))
    _, utilities = zip(*results)
    if player == "X": action_index = np.argmax(utilities)
    if player == "O": action_index = np.argmin(utilities)
    return children[action_index], utilities[action_index]


if __name__ == "__main__":

    # TODO: compare results with XKCD
    state = np.array([["_"]*3]*3)
    state[0,0] = "X" # optimal, according to https://xkcd.com/832/
    state[0,1] = "O" # suboptimal
    
    # Each player using minimax each turn to decide the next action and state
    while state is not None:
      print(state_string(state))
      state, u = minimax(state)
      print("utility:", u)
