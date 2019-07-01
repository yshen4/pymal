import numpy as np

def perceptron(X, y, T, it=None):
    theta = it
    if theta is None:
        theta = np.zeros(X.shape[1])

    error = 0
    for t in range(1, T+1):
        for i in range(len(y)):
            z = np.matmul(theta, X[i])
            z *= y[i]

            if z <= 0:
               error += 1
               print(error, theta)
               theta = theta + y[i] * X[i]
            else:
               print('+', theta)

    print(theta)

if __name__ == '__main__':
    print ("Homework 2.3")
    X = np.array([[-1, 0], [0, 1]])
    y = np.array([1,  1])
    perceptron(X, y, 4)
