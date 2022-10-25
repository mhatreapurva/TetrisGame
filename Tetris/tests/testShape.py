
import pytest

import sys
sys.dont_write_bytecode = True # Avoid creating __pycache__

import numpy as np
from src.modules.Shape import Shape
from src.modules.Grid import Grid
def test_shape_integrity():
    T = Shape()
    assert np.array_equal(T.O,np.array([[1,1],[1,1]])) == True
    assert np.array_equal(T.I,np.array([[1,1,1,1]])) == True
    assert np.array_equal(T.T,np.array([[1,1,1],[0,1,0]])) == True
    assert np.array_equal(T.J,np.array([[0,1],[0,1],[1,1]])) == True
    assert np.array_equal(T.L,np.array([[1,0],[1,0],[1,1]])) == True
    assert np.array_equal(T.S,np.array([[0,1,1],[1,1,0]])) == True
    assert np.array_equal(T.Z,np.array([[1,1,0],[0,1,1]])) == True

def test_insert_shape_O():
    T = Shape()
    Tetris = Grid()

    #-------------------O-------------------------
    Tetris.GRID = np.array([[0,0]])
    actual = T.validPositions(T.O,Tetris.GRID)
    expected = []
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[0,0,0,0]])
    actual = T.validPositions(T.O,Tetris.GRID)
    expected = [(0,0),(0,1),(0,2)]
    assert actual == expected

    Tetris.GRID = np.array([[0,0,1,0]])
    actual = T.validPositions(T.O,Tetris.GRID)
    expected = []
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    actual = T.validPositions(T.O,Tetris.GRID)
    expected = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    assert actual == expected

    Tetris.GRID = np.array([[0,0,1,1],[0,0,1,1],[1,1,0,0],[1,1,0,0]])
    actual = T.validPositions(T.O,Tetris.GRID)
    expected = [(0,0),(2,2)]
    assert actual == expected



def test_insert_shape_I():
    T = Shape()
    Tetris = Grid()
    #-------------------I-------------------------
    Tetris.GRID = np.array([[0,0]])
    actual = T.validPositions(T.I,Tetris.GRID)
    expected = []
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0]])
    actual = T.validPositions(T.I,Tetris.GRID)
    expected = [(0,0)]
    assert actual == expected

    Tetris.GRID = np.array([[0,0,1,0]])
    actual = T.validPositions(T.I,Tetris.GRID)
    expected = []
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    actual = T.validPositions(T.I,Tetris.GRID)
    expected = [(0,0),(1,0),(2,0),(3,0)]
    assert actual == expected

def test_insert_shape_T():
    T = Shape()
    Tetris = Grid()
    #-------------------T-------------------------
    Tetris.GRID = np.array([[0,0]])
    actual = T.validPositions(T.T,Tetris.GRID)
    expected = [] 
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[0,0,0,0]])
    actual = T.validPositions(T.T,Tetris.GRID)
    expected = [(0,0),(0,1)]
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[1,0,1,0]])
    actual = T.validPositions(T.T,Tetris.GRID)
    expected = [(0,0)]
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    actual = T.validPositions(T.T,Tetris.GRID)
    expected = [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]
    assert actual == expected

def test_insert_shape_J():
    T = Shape()
    Tetris = Grid()
    #-------------------J-------------------------
    Tetris.GRID = np.array([[0,0]])
    actual = T.validPositions(T.J,Tetris.GRID)
    expected = []
    assert actual == expected

    Tetris.GRID = np.array([[1,0],[1,0],[0,0]])
    actual = T.validPositions(T.J,Tetris.GRID)
    expected = [(0,0)]
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    actual = T.validPositions(T.J,Tetris.GRID)
    expected = [(0,0),(0,1),(0,2)]
    assert actual == expected

    Tetris.GRID = np.array([[0,0],[0,0],[0,1]])
    actual = T.validPositions(T.J,Tetris.GRID)
    expected = []
    assert actual == expected

def test_insert_shape_L():
    T = Shape()
    Tetris = Grid()
    #-------------------L-------------------------
    Tetris.GRID = np.array([[0,0]])
    actual = T.validPositions(T.L,Tetris.GRID)
    expected = []
    assert actual == expected

    Tetris.GRID = np.array([[0,1],[0,1],[0,0]])
    actual = T.validPositions(T.L,Tetris.GRID)
    expected = [(0,0)]
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    actual = T.validPositions(T.L,Tetris.GRID)
    expected = [(0,0),(0,1),(0,2)]
    assert actual == expected

    Tetris.GRID = np.array([[0,0],[0,0],[0,1]])
    actual = T.validPositions(T.L,Tetris.GRID)
    expected = []
    assert actual == expected

def test_insert_shape_S():
    T = Shape()
    Tetris = Grid()
    #-------------------S-------------------------
    Tetris.GRID = np.array([[]])
    actual = T.validPositions(T.S,Tetris.GRID)
    expected = []
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    actual = T.validPositions(T.S,Tetris.GRID)
    expected = [(0,0),(0,1),(1,0),(1,1)]
    assert actual == expected

    Tetris.GRID = np.array([[1,0,0,0],[0,0,0,1],[1,0,0,0]])
    actual = T.validPositions(T.S,Tetris.GRID)
    expected = [(0,0),(0,1)]
    assert actual == expected

def test_insert_shape_Z():
    T = Shape()
    Tetris = Grid()
    #-------------------Z-------------------------
    Tetris.GRID = np.array([[]])
    actual = T.validPositions(T.Z,Tetris.GRID)
    expected = []
    assert actual == expected

    Tetris.GRID = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    actual = T.validPositions(T.Z,Tetris.GRID)
    expected = [(0,0),(0,1),(1,0),(1,1)]
    assert actual == expected

    Tetris.GRID = np.array([[1,0,0,0],[0,0,0,1],[1,0,0,0]])
    actual = T.validPositions(T.Z,Tetris.GRID)
    expected = [(1,0),(1,1)]
    assert actual == expected


    



