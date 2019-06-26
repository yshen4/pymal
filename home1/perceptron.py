import numpy as np

def perceptron(X, y, T):
    theta = np.zeros(X.shape[1])
    theta0= 0

    error = 0
    for t in range(1, T+1):
        for i in range(len(y)):
            z = np.matmul(theta, X[i]) + theta0
            z *= y[i]

            if z <= 0:
               error += 1
               print(error, theta)
               theta = theta + y[i] * X[i]
               theta0= theta0 + y[i]

if __name__ == '__main__':
    print ("Home 1a")
    X = np.array([[-1, -1], [1, 0], [-1, 1.5]])
    y = np.array([ 1, -1,  1])
    perceptron(X, y, 10)

    print ("Home 1b")
    X = np.array([[-1, 1.5], [-1, -1], [1, 0]])
    y = np.array([ 1, 1, -1])
    perceptron(X, y, 10)

    print ("Home 1c")
    X = np.array([[-1, -1], [1, 0], [-1, 10]])
    y = np.array([ 1, -1,  1])
    perceptron(X, y, 10)

    print ("Home 1d")
    X = np.array([[1, 0], [-1, 10], [-1, -1]])
    y = np.array([-1,  1, 1])
    perceptron(X, y, 10)
