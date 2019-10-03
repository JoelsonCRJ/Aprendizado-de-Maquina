import pandas as pd
import numpy as np
from functions02 import *


#-------------------------------------------
data = pd.read_csv('wdbc.txt',sep=',',header = None)
data = data.drop(data.columns[0], axis=1)

data = np.array(data)
trainning_data = data[0:300,:]
test_data = data[300:data.shape[0],:]

#necessario excluir coluna 1 e a de labels so na funcao do NN
labels_vector=test_data[:,0]
prediction_vector_NN=NN(trainning_data,test_data,0)
accuracy_NN=accuracy(labels_vector,prediction_vector_NN)
print("Accuracy using NN: {0:.2f}%".format( accuracy_NN))



