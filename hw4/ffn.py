import numpy as np

# W: n x m, X: m x 1
def cal_one_layer(W, X):
    z = np.matmul(W, X)
    return np.array([max(v, 0) for v in z])

def cal_softmax(U, beta=1):
    exp = np.exp(beta*U)
    sum_exp = np.sum(exp)
    return exp/sum_exp
 
def reluffn():
    X = np.array([3, 14, 1])
    X = np.transpose(X)
    W = np.array([[1, 0, -1], [0, 1, -1], [-1, 0, -1], [0, -1, -1]])

    fz = cal_one_layer(W, X)
    fz = np.append(fz, 1)
    V = np.array([[1, 1, 1, 1, 0], [-1, -1, -1, -1, 2]])
    fu = cal_one_layer(V, fz)

    return cal_softmax(fu)

def fu(u):
    eu = np.exp(u)
    sm = np.sum(eu)
    return eu/sm

if __name__ == "__main__":
    output = reluffn()
    print(output)

    u1 = np.array([1, 1])
    print(fu(u1)[0])
    u2 = np.array([0, 2])
    print(fu(u2)[0])
    u3 = np.array([3, -1])
    print(fu(u3)[0])
