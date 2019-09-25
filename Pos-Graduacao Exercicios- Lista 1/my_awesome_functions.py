import numpy as np
from scipy import stats

def split_by_labels(array):
    L1=array[array[:,array.shape[1]-1]==1]
    L2=array[array[:,array.shape[1]-1]==2]
    L3=array[array[:,array.shape[1]-1]==3]
    
    return L1,L2,L3
def drop_incomplete(array):
    for i in range(0,array.shape[1]-1):
        array=array[array[:,i]>0]
    return array

def sample_centroids(data):
    m=np.empty((data.shape[1] -1),dtype=float)
    for i in range (0,data.shape[1]-1):
        m[i]=np.mean(data[:,i],dtype=np.float64)
    return m

def rocchio(data,Center_1,Center_2,Center_3):
    labels=[]
    euclidian=np.empty((3),dtype = float)
    for i in range(0,data.shape[0]):
        for j in range(0,(data.shape[1]-1)):
            euclidian[0]=np.sqrt(np.power(np.sum(Center_1[j]-data[i,j]),2))
            euclidian[1]=np.sqrt(np.power(np.sum(Center_2[j]-data[i,j]),2))
            euclidian[2]=np.sqrt(np.power(np.sum(Center_3[j]-data[i,j]),2))
            
        if(np.min(euclidian)==euclidian[0]):
            labels.append(1)
        elif(np.min(euclidian)==euclidian[1]):
            labels.append(2)
        else:
            labels.append(3)
    return labels

def NN(trainning_array,test_array):
    labels=[]
    for i in range(0,test_array.shape[0]):
        distances=np.zeros((len(trainning_array)))
        for z in range(0,trainning_array.shape[0]):
            distances[z]=np.sqrt(np.sum(np.power(np.subtract(test_array[i,0:4],trainning_array[z,0:4]),2)))
        #min[0] = index of min value and min[1] is the min value
        #print(distances)
        distances = list(distances)
        min_index = distances.index(min(distances))
        #print(min_index)
        #print(min_index)
        labels.append(trainning_array[min_index,4])  
    return np.array(labels)


def accuracy(labels,prediction):
    count=0
    for i in range(0,labels.shape[0]):
        if(labels[i]==prediction[i]):
            count=count+1
    return (count/len(labels))*100

def replace_by_mode(array):
    
    for i in range(0,array.shape[1]-1):
        while (i==0):
            index = np.where((array[:,i]<1) | (array[:,i]>3)) #get indexes
            index = index[0] #array of indexes
            m=stats.mode(array[:,i],axis=None) #calculating the mode of this atribute
            for j in range(0,len(index)):
                array[index[j],i]=int(m[0])
            i=1
        
        index = np.where((array[:,i]<1) | (array[:,i]>4))
        index = index[0]
        m=stats.mode(array[:,i],axis=None)
        for j in range(0,len(index)):
            array[index[j],i]=int(m[0])
    return array
