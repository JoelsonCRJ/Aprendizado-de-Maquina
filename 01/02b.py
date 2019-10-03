import pandas as pd
import numpy as np
from functions02 import *

data = pd.read_csv('wdbc.txt',sep=',',header = None)
data = data.drop(data.columns[0], axis=1)

data = np.array(data)
trainning_data = data[0:300,:]
test_data = data[300:data.shape[0],:]
print(trainning_data.shape[1])

def get_x(array):
    X=np.zeros((array.shape[1]-1,array.shape[0]),dtype = np.float32)
    for i in range(0,array.shape[1]-1):
        for j in range(0, array.shape[0]):
            X[i][j]=(array[i][j] - np.mean(array[i,:],dtype=np.float64))/np.std(array[i,:],dtype=np.float32)
            
    return X

print(trainning_data[:,1:trainning_data.shape[1]].shape[1])
X_til = get_x(trainning_data[:,1:trainning_data.shape[1]])
print(X_til)
            
#    np.linalg.eigh(X,UPLO = 'U')