#!/usr/bin/python
import numpy as np
import pandas as pd
import csv

def load (file):
    X = np.matrix(np.loadtxt(open(file),delimiter=",",usecols=(0,1,2,3),skiprows=1))
    return X

def scaleFeatures (X):
    mean = np.sum(X,axis=0) * (1/X.shape[0])
    X = np.tile(mean, (X.shape[0],1))
    return X

def getMulticlassOutput (file):
    return file

def engineerPolynomials(X, degree):
    return


def regularizedCost(X, y, theta, lmbda):
    return

file = "irisflowers.csv"
X = load(file)
Y = getMulticlassOutput(file)
X = scaleFeatures(X)
print(X)
