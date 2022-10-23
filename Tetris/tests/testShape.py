import pytest
import numpy as np
from src.shape import shape
def test_shape_integrity():
    T = shape.Shape()
    assert np.array_equal(T.O,np.array([[1,1],[1,1]])) == True
    assert np.array_equal(T.I,np.array([[1,1,1,1]])) == True
    assert np.array_equal(T.T,np.array([[1,1,1],[0,1,0]])) == True
    assert np.array_equal(T.J,np.array([[0,1],[0,1],[1,1]])) == True
    assert np.array_equal(T.L,np.array([[1,0],[1,0],[1,1]])) == True
    assert np.array_equal(T.S,np.array([[0,1,1],[1,1,0]])) == True
    assert np.array_equal(T.Z,np.array([[1,1,0],[0,1,1]])) == True
