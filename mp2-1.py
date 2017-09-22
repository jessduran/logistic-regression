#!/usr/bin/python
import numpy as np
import pandas as pd

def load (file):
    container = pd.read_csv(file, sep=',')
    return container

def scaleFeatures (X):
    stdevs = []
    for column in X:
        stdevs.append(np.sqrt(np.square(X[column] - X[column].mean()).mean()))
    i = 0
    for column in X:
        X[column] = (X[column] - X[column].mean()) / stdevs[i]
        i += 1

    return X

file = open("irisflowers.csv", "rb")
container = load(file)
X = container.iloc[:, :-1]
X = scaleFeatures(X)

print(X)
