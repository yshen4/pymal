from scipy import stats
import numpy as np

def compute_posterior(mu, std, X):
    nd = stats.norm(mu, std)

    return [nd.pdf(x) for x in X]

def estimate(mu, std, P, X):
    pv1list = compute_posterior(mu[0], std[0], X)
    pv2list = compute_posterior(mu[1], std[1], X)

    eta1 = [pv1*P[0]/(P[0]*pv1+P[1]*pv2) for pv1, pv2 in zip(pv1list, pv2list)]
    eta2 = [pv2*P[0]/(P[0]*pv1+P[1]*pv2) for pv1, pv2 in zip(pv1list, pv2list)]
    return eta1, eta2

if __name__ == '__main__':
    X = [0.2, -0.9, -1, 1.2, 1.8]

    mu = [-3, 2]
    std = [2, 2]
    P = [0.5, 0.5]

    eta1, eta2 = estimate(mu, std, P, X)
    print("Expected for cluster 1:")
    [print(p) for p in eta1]
    print("Expected for cluster 2:")
    [print(p) for p in eta2]

    p1 = sum(eta1)/len(eta1)
    p2 = sum(eta2)/len(eta1)
    print("P1, P2:", p1, p2)

    mu1 = np.array(X).dot(eta1)/sum(eta1)
    ss1 = np.array(X) - mu1
    ss1 = np.square(ss1)
    ss1 = ss1.dot(eta1)/sum(eta1)
    print ("mu1, ss1: ", mu1, ss1)


    
