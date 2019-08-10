import numpy as np

def estimate(X, W):
    C = np.zeros(len(W), dtype=int)

    dict = {}
    for i in range(len(W)):
        dict[W[i]] = i

    for w in X:
        C[ dict[w] ] += 1

    tt = np.sum(C)
    return np.divide(C, tt)


if __name__ == '__main__':
    X = 'A B A B B C A B A A B C A C'.split()
    W = 'A B C'.split()

    print(estimate(X, W))
    
        
