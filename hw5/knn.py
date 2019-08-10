import numpy as np

# manhanttan distance
def l1norm(x1, x2):
    distance = 0
    for v in x1 - x2:
        distance += np.abs(v)

    return distance

def l2norm(x1, x2):
    distance = 0.0
    for v in x1 - x2:
        distance += v**2

    return np.sqrt(distance)

def test_l1norm():
    A1 = [1, 2, 3]
    A2 = [-1, -2, -3]
    A3 = [2, 3, 4]
    B = [2, 3, 4]

    print(l1norm(np.array(A1), np.array(B)))
    print(l1norm(np.array(A2), np.array(B)))
    print(l1norm(np.array(A3), np.array(B)))

def init_medoid():
    return np.array([[0, -6], [4, 4], [0, 0], [-5, 2]]), np.array([[-5, 2], [0, -6]])

def kmean_estimate_centroids(X, a, K, f_norm):
    sj = np.zeros((K, X.shape[1]))
    nj = np.zeros(K) 
    for i in range(a.shape[0]):
        sj[ a[i] ] += X[i, :]
        nj[ a[i] ] += 1

    return np.divide(sj, nj)

def kmedoid_estimate_centroids(X, a, K, f_norm):
    centroids = np.array([None] * K)
    ss = np.zeros(K)
    for k in range(K):
        idx = (a == k)
        for x in X[idx]:
            ssx = 0
            for xx in X[idx]:
                ssx += f_norm(x, xx)
            if centroids[k] is None or ss[k] > ssx:
                centroids[k] = x
                ss[k] = ssx
    return centroids            

def knn(X, K, centroids, f_norm, f_centroid):
    # assign x(i) to j
    a = np.zeros(X.shape[0], dtype=int)
    for i in range(X.shape[0]):
        min_d = -1
        for k in range(centroids.shape[0]):
            d = f_norm(X[i, :], centroids[k, :])
            if min_d < 0:
                a[i] = k
                min_d = d
            elif min_d > d:
                a[i] = k
                min_d = d

    for k in range(K):
        print("Cluster", k)
        [print(x) for x in X[a == k] ]

    # update centroid
    centroids = f_centroid(X, a, centroids.shape[0], f_norm)
    print("Estimate:", centroids)
    return a, centroids

if __name__ == '__main__':
    #test_l1norm()
    X, C = init_medoid()
    knn(X, 2, C, l1norm, kmean_estimate_centroids)
    knn(X, 2, C, l2norm, kmean_estimate_centroids)
    #knn(X, 2, C, l1norm, kmedoid_estimate_centroids)
    #knn(X, 2, C, l2norm, kmedoid_estimate_centroids)
