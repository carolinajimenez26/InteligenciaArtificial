import numpy as np
import pandas as pd
from mlxtend.evaluate import plot_decision_regions
import matplotlib.pyplot as plt

class Perceptron(object):

        def __init__(self, eta=0.01, epochs=50):
                self.eta = eta
                self.epochs = epochs

        def train(self, X, y):

                self.w_ = np.zeros(1 + X.shape[1])
                self.errors_ = []

                for _ in range(self.epochs):
                        errors = 0
                        for xi, target in zip(X, y):
                                update = self.eta * (target - self.predict(xi))
                                self.w_[1:] +=  update * xi
                                self.w_[0]  +=  update
                                errors += int(update != 0.0)
                        self.errors_.append(errors)
                return self

        def net_input(self, X):
                return np.dot(X, self.w_[1:]) + self.w_[0]

        def predict(self, X):
                return np.where(self.net_input(X) >= 0.0, 1, -1)

if __name__ == "__main__":
    df = pd.read_csv('iris.csv',header=None)
    y = df.iloc[0:100,4].values
    y = np.where(y == 'setosa', -1, 1)
    x = df.iloc[0:100,[0,2]].values
    ppn = Perceptron(eta=0.01, epochs=10)
    ppn.train(x,y)
    plot_decision_regions(x,y,ppn)
    plt.title("Perceptron setosa-versicolor")
    plt.show()

    y = df.iloc[50:150,4].values
    y = np.where(y == 'versicolor', -1, 1)
    x = df.iloc[50:150,[0,2]].values
    ppn = Perceptron(eta=0.01, epochs=50)
    ppn.train(x,y)
    plot_decision_regions(x,y,ppn)
    plt.title("Perceptron versicolor-virginica")
    plt.show()
