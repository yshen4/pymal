import numpy as np

def estimate(X, dict):
    K = len(dict)
    C = np.zeros((K, K), dtype=float)

    for i in range(len(X) - 1):
        w1 = X[i]
        w2 = X[i+1]
        C[ dict[w1], dict[w2] ] += 1

    for i in range(K):
        tt = np.sum(C[i, :])
        C[i, :] = np.divide(C[i, :], tt)

    return C

if __name__ == '__main__':
    X = 'A B A B B C A B A A B C A C'.split()
    W = 'A B C'.split()

    dict = {}
    for i in range(len(W)):
        dict[W[i]] = i

    cpw = estimate(X, dict)
    print(cpw)

    Y = "A A B C B A B".split()
    p = 1.0/3
    for i in range(1, len(Y)):
        w2 = Y[i]
        w1 = Y[i-1]
        p *= cpw[ dict[w1], dict[w2] ]

    print(p)
    
        
