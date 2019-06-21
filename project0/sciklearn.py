from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

from sklearn.linear_model import Perceptron
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plot
import numpy as np

def learn_linear_data():
    # create the data set
    X, y = make_blobs(n_samples = 1000, centers = 2, random_state = 0)

    # split data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # define the classifier
    #clf = Perceptron(max_iter = 40, random_state = 0)
    clf = LinearSVC(max_iter=40, random_state=0)

    # train the classifier with training data
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print ('Test accuracy: %.4f' % accuracy_score(y_test, y_pred))

    fig, ax = plot.subplots()

    # plot the training and testing
    for label in [0, 1]:
        mask = (y_train == label)
        ax.scatter(X_train[mask, 0], X_train[mask, 1])

    for label in [0, 1]:
        mask = (y_test == label)
        ax.scatter(X_test[mask, 0], X_test[mask, 1])

    # plot the classifer
    theta = clf.coef_[0]
    theta_0 = clf.intercept_
    x_bnd = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1,  400)
    y_bnd = - x_bnd * (theta[0] /theta[1]) - (theta_0 / theta[1])
    ax.plot(x_bnd, y_bnd)
    
    plot.show()

if __name__ == '__main__':
    learn_linear_data()
