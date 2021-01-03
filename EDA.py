import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
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

def PlotData(train):
  sns.distplot(sales_train['item_price'])

  
  
