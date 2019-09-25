import pandas as pd
import numpy as np


def NN(trainning_array,test_array,labels_column):
    labels=[]
    for i in range(0,test_array.shape[0]):
        distances=np.zeros((len(trainning_array)))
        for z in range(0,trainning_array.shape[0]):
            distances[z]=np.sqrt(np.sum(np.power(np.subtract(test_array[i,1:test_array.shape[1]],trainning_array[z,1:trainning_array.shape[1]]),2)))
        #min[0] = index of min value and min[1] is the min value
        #print(distances)
        distances = list(distances)
        min_index = distances.index(min(distances))
        #print(min_index)
        #print(min_index)
        labels.append(trainning_array[min_index,labels_column])  
    return np.array(labels)

def accuracy(labels,prediction):
    count=0
    for i in range(0,labels.shape[0]):
        if(labels[i]==prediction[i]):
            count=count+1
    return (count/len(labels))*100
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



