import torch
import random
import numpy as np

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)


def get_dataset():
    from sklearn.datasets import make_classification
    set_seed(7)

    X, y = make_classification(n_features = 2,
                               n_redundant = 0,
                               n_informative = 1,
                               n_clusters = 1)

    print("Number of examples: %d" % X.shape[0])
    print("Number of features: %d" % X.shape[1])

    return X, y

def plot_dataset(X, Y):
    import matplotlib
    import matplotlib.pyplot as plot

    plot.scatter(X[:, 0], X[:, 1], marker='o', c= Y, s = 25, edgecolor= 'k')
    plot.show()

if __name__ == '__main__':
    X, y = get_dataset()
    plot_dataset(X, y)   
