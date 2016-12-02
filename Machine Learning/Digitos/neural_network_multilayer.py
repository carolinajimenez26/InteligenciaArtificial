# coding: utf-8
import numpy as np
import pandas as pd

class neuro_network():

    def __init__(self, layers, activation = 'tanh'):
        if activation == 'logistic':
            self.activation = lambda x : 1 / (1 + np.exp(-x))
            self.deriv = lambda x : self.activation(x) * (1 - self.activation(x))
        elif activation == 'tanh':
            self.activation = lambda x : np.tanh(x)
            self.deriv = lambda x : 1.0 - np.tanh(x) ** 2

        self.weights = []
        for i in range(1, len(layers) - 1):
            self.weights.append((2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1) * 0.25)
        self.weights.append((2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1) * 0.25)

    def fit(self, X, y, learning_rate = 0.2, epochs = 10000) :
        X = np.atleast_2d(X)
        temp  = np.ones([X.shape[0], X.shape[1] + 1])
        temp[:, 0 : -1] = X
        X = temp
        y = np.array(y)
        for k in range(epochs):
            i = np.random.randint(y.shape[0]);
            a = [X[i]]
            for l in range(len(self.weights)):
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            error = y[i] - a[-1]
            deltas = [error * self.deriv(a[-1])]

            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T) * self.deriv(a[l]))
            deltas.reverse()
            for i in range(len(self.weights)) :
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0]+1)
        temp[0:-1] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a

def convertDecimal(n):
    a = [0]*10
    a[n] = 1
    return a

def DecimalToBinary(n):
    ans = [int(i) for i in str(bin(n)[2:])]
    a = 4 - len(ans)
    return [0] * a + ans

if __name__ == "__main__":
    # XOR
    """nn = NeuralNetwork([2,2,1],activation='logistic')
    X = np.array([[0,0],[0,1],[1,0],[1,1]])
    y = np.array([0,1,1,0])
    nn.fit(X,y)

    for x in X:
        print (x,nn.predict(x))
    """
    # Digitos decimales
    capas = [64,50,10]
    df = pd.read_csv('digits.csv',header=None)
    digitos = neuro_network(capas, 'logistic')
    x = np.array(df.iloc[0:1797,[i for i in range(0,64)]].values)
    y = df.iloc[0:1797,64].values
    y = np.array([convertDecimal(int(y[i])) for i in range(0,len(y))])
    digitos.fit(x,y)

    for X in x:
        print (X, [round(i) for i in digitos.predict(X)])

    # Digitos binarios
    capas = [64,50,4]
    df = pd.read_csv('digits.csv',header=None)
    digitos = neuro_network(capas, 'logistic')
    x = np.array(df.iloc[0:1797,[i for i in range(0,64)]].values)
    y = df.iloc[0:1797,64].values
    y = np.array([DecimalToBinary(int(y[i])) for i in range(0,len(y))])
    digitos.fit(x,y)

    for X in x:
        print (X, [round(i) for i in digitos.predict(X)])
