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

        labels.append(trainning_array[min_index,labels_column])  
    return np.array(labels)

def accuracy(labels,prediction):
    count=0
    for i in range(0,labels.shape[0]):
        if(labels[i]==prediction[i]):
            count=count+1
    return (count/len(labels))*100