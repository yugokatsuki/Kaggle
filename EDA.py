import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm
%matplotlib inline

def GetNumericalIndex(train):
  return train.dtypes[train.dtypes != "object"].index
def GetCategoricalIndex(train):
  return train.dtypes[train.dtypes == "object"].index
def GetInfoOfData(train):
  print("*"*50)
  print("data contents")
  print(train)
  print("*"*50)
  print("data shape")
  print(train.shape)
  print("*"*50)
  print("data dtypes")
  print(train.dtypes)
  print("*"*50)
  print("data info")
  print(train.info())
  print("*"*50)
  print("data stats")
  print(sales_train.describe(include='all'))
  print("*"*50)
  print("data null count")
  print(train.isnull().sum().sort_values(ascending=False))

def PlotData(train, label1, label2):
  plt.figure(figsize=(10, 10))
  sns.distplot(train[abel1], fit=norm ).set(xlim=(0,10000))
  train.plot.scatter(x=label1 ,y=label2, xlim=(0,75000), ylim=(0,750))
  #sns.boxplot(x=label1, y=label2, data=sales_train)
  corrmat = train.corr()
  plt.figure(figsize=(10, 10))
  #pick k largest correlation using corrmat.nlargest
  sns.heatmap(corrmat, vmax=1.0, square=True)
  sns.pairplot(train, size = 2.5)
  fig = plt.figure()
  res = stats.probplot(train[label1], plot=plt)  
  
