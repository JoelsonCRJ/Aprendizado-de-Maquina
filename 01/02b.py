import pandas as pd
import numpy as np
from functions02 import *

data = pd.read_csv('wdbc.txt',sep=',',header = None)
data = data.drop(data.columns[0], axis=1)

data = np.array(data)
trainning_data = data[0:300,:]
test_data = data[300:data.shape[0],:]
 

def get_x(array):
    
    X=np.zeros((array.shape[0],array.shape[1]),dtype = np.float32)
    for i in range(0,array.shape[0]):
        for j in range(0, array.shape[1]):
            X[i][j]=(array[i][j] - np.mean(array[:,j],dtype=np.float32))/np.std(array[:,j],dtype=np.float32)
        
    return X


X_til = get_x(trainning_data[:,2:trainning_data.shape[1]]) # atributo 1 ate o final 
X_til_transposed = np.transpose(X_til)
N=29 # tirando dois primeiros atributos pois são irrelevantes
C=1/(N-1)* 
#    np.linalg.eigh(X,UPLO = 'U')