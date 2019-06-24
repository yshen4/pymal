from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

from sklearn.linear_model import Perceptron
from sklearn.svm import LinearSVC, SVC
from sklearn.metrics import accuracy_score

from sklearn.datasets import load_digits

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

def learn_nonlinear_data(n = 500, c = 3, s = 7):
    # create the data set
    X, y = make_blobs(n_samples = n, centers = c, random_state = s)
    y[y==2] = 0 

    # split training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    # define the classifier
    # clf = SVC(kernel="linear", random_state = 0)
    clf = SVC(kernel="rbf", random_state = 0)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print ('Test accuracy: %.4f' % accuracy_score(y_test, y_pred))

    x_min = X[:, 0].min()
    x_max = X[:, 0].max()
    y_min = X[:, 1].min()
    y_max = X[:, 1].max()

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

    fig, ax = plot.subplots()
    for label in [0, 1]:
        mask = (y == label)
        ax.scatter(X[mask, 0], X[mask, 1])

    Z = Z.reshape(XX.shape)
    ax.contour(XX, YY, Z, colors = "black", 
               linestyles = ['--', '-', '--'],
               levels = [-.5, 0, .5])
    plot.show()

def learn_digits():
    digits = load_digits()
    X, y = digits.data, digits.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

    # define classifier
    # 93.85%
    #clf = Perceptron(max_iter=40, random_state=0)
    # 93.89%
    #clf = LinearSVC(max_iter=40, random_state=0)
    # 97.78%
    clf = SVC(kernel="linear", random_state = 0)
    # doesn't work very well
    #clf = SVC(kernel="rbf", random_state = 0)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print ('Test accuracy: %.4f' % accuracy_score(y_test, y_pred))
    '''
    fig, ax = plot.subplots()
    ax.matshow(digits.images[0])
    plot.show()
    '''

if __name__ == '__main__':
    #learn_linear_data()
    #learn_nonlinear_data()
    learn_digits()
