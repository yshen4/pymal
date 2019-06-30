from perceptron import *

import numpy as np

if __name__ == '__main__':
    print ("Homework 1a")
    X = np.array([[-1, -1], [1, 0], [-1, 1.5]])
    y = np.array([ 1, -1,  1])
    perceptron(X, y, 2)

    print ("Homework 1b")
    X = np.array([[-1, 1.5], [-1, -1], [1, 0]])
    y = np.array([ 1, 1, -1])
    perceptron(X, y, 2)

    print ("Homework 1c")
    X = np.array([[-1, -1], [1, 0], [-1, 10]])
    y = np.array([ 1, -1,  1])
    perceptron(X, y, 2)

    print ("Homework 1d")
    X = np.array([[1, 0], [-1, 10], [-1, -1]])
    y = np.array([-1,  1, 1])
    perceptron(X, y, 2)

    print ("Homework 2")
    X = np.array([[-4, 2], [-2, 1], [-1, -1], [2, 2], [1, -2]])
    y = np.array([1, 1, -1, -1, -1])
    perceptron(X, y, 2)
