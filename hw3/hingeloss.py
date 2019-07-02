import numpy as np

def hinge_loss(y, X, theta, theta0 = 0):
    z = y - np.matmul(theta, X) - theta0
    return 0 if z > 1 else 1 - z

def square_loss(y, X, theta, theta0 = 0):
    z = y - np.matmul(theta, X) - theta0
    return z * z / 2.0

def empirical_risk(f_loss, v_y, v_X, theta, theta0 = 0):
    total_loss = 0
    for i in range(v_y.shape[0]):
        total_loss += f_loss(v_y[i], v_X[i], theta, theta0)

    return total_loss / float(v_y.shape[0])
    
if __name__ == '__main__':
    y = np.array([2., 2.7, -0.7, 2.])
    X = np.array([[1, 0, 1], [1, 1, 1], [1, 1, -1], [-1, 1, 1]])
    theta = [0, 1, 2]
    print("X = ", X)
    print("y = ", y)
    print("theta = ", theta)

    re = empirical_risk(hinge_loss, y, X, theta)
    print("Empirical risk with hinge loss: ", re)

    re = empirical_risk(square_loss, y, X, theta)
    print("Empirical risk with square loss: ", re)
    
