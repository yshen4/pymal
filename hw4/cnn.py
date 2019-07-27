import numpy as np
import scipy.signal as sg

def relu(X):
    return np.maximum(0, X)

if __name__ == '__main__':
    f = np.array([1, 3, -1, 1, -3])
    g = np.array([-1, 0, 1])
    print(np.convolve(f, g))

    f = np.array([[1, 2, 1], [2, 1, 1], [1, 1, 1]])
    g = np.array([[0.5, 1], [1, 0.5]])
    print(sg.convolve2d(f, g))

    I = np.array([[1, -1, 2], [3, 1, -1], [-1, -1, 4]])
    I = relu(I)
    print(I)

    F = np.array([[1, 0], [0, 1]])
    H = sg.convolve2d(I, F)
    H = relu(H)
    print(H)
