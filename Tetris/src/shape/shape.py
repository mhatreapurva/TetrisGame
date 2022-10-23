# Shape generation package
import numpy as np
"""
Definition for Tetris shapes:
https://en.wikipedia.org/wiki/Tetromino

"""
class Shape(object):
    O = np.array([[1,1],[1,1]])
    I = np.array([[1,1,1,1]])
    T = np.array([[1,1,1],[0,1,0]])
    J = np.array([[0,1],[0,1],[1,1]])
    L = np.array([[1,0],[1,0],[1,1]])
    S = np.array([[0,1,1],[1,1,0]])
    Z = np.array([[1,1,0],[0,1,1]])
