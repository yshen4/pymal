import numpy as np

def relu(z):
    return max(0, z)

def get_z(x, w, b):
    return x * w + b

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def loss(y, t):
    return (y - t)**2/2.0

if __name__ == '__main__':
    t = 1
    x = 3
    w1 = 0.01
    w2 = -5
    b = -1

    z1 = w1 * x
    a1 = relu(z1)
    z2 = w2 * a1 + b
    y = sigmoid(z2)
    c = loss(y, t)

    print (c)

    db = np.exp(-z2)/((1+np.exp(-z2))**2) * (y - t)
    dw1 = x * db * w2
    print (dw1)

    dw2 = a1 * db
    print (dw2)
    print (db)

    
