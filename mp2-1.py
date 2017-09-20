#!/usr/bin/python
import numpy as np
import pandas as pd

def load (file):
    # loads data from the attached dataset
    # places it in a container
    container = pd.read_csv(file, sep=',')
    return container

def scaleFeatures (X):
    # scales each feature in the container X using z-score
    # print (means)
    stdevs = []
    stdevs.append(np.sqrt(np.square(X["SepalLengthCm"] - X["SepalLengthCm"].mean()).mean()))
    stdevs.append(np.sqrt(np.square(X["SepalWidthCm"] - X["SepalWidthCm"].mean()).mean()))
    stdevs.append(np.sqrt(np.square(X["PetalLengthCm"] - X["PetalLengthCm"].mean()).mean()))
    stdevs.append(np.sqrt(np.square(X["PetalWidthCm"] - X["PetalWidthCm"].mean()).mean()))

    X["SepalLengthCm"] = (X["SepalLengthCm"] - X["SepalLengthCm"].mean()) / stdevs[0]
    X["SepalWidthCm"] = (X["SepalWidthCm"] - X["SepalWidthCm"].mean()) / stdevs[1]
    X["PetalLengthCm"] = (X["PetalLengthCm"] - X["PetalLengthCm"].mean()) / stdevs[2]
    X["PetalWidthCm"] = (X["PetalWidthCm"] - X["PetalWidthCm"].mean()) / stdevs[3]
    print (X)
    return X

file = open("irisflowers.csv", "rb")
X = load(file)
scaleFeatures(X)
