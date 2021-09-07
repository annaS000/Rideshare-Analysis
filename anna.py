## anna's functions to use for anything

# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import os

def getPath(folder,file):
    return os.path.join(folder,file)

def getData(folder,file):
    return pd.read_csv(getPath(folder,file))

def getThis(df,col,pandas_stat):
    return getattr(df[col], pandas_stat)()

def getSeries(df,col):
    return df[col]
    
def getPercent(x,y):
    return x / y * 100

def makeDF(dic):
    return pd.DataFrame(dic)

def formatThis(df,col,how):
    return df[col].map(how.format)