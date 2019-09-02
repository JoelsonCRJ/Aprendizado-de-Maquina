import matplotlib as plt
import pandas as pd

data= pd.read_csv('iris.txt',sep=" ", header = None)
print(data)
pd.plotting.scatter_matrix(data.loc[:,0:3])

data.info()