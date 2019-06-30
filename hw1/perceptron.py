import numpy as np

def perceptron(X, y, T, it=None, it0=0):
    theta = it
    if theta is None:
        theta = np.zeros(X.shape[1])
    theta0= it0

    error = 0
    for t in range(1, T+1):
        for i in range(len(y)):
            z = np.matmul(theta, X[i]) + theta0
            z *= y[i]

            if z <= 0:
               error += 1
               print(error, theta, theta0)
               theta = theta + y[i] * X[i]
               theta0= theta0 + y[i]
            else:
               print('+', theta, theta0)

    print(theta, theta0)

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
