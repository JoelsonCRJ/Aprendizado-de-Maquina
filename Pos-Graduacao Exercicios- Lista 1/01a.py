#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:26:56 2019

@author: joelson
"""

import pandas as pd
import numpy as np
from scipy import stats
"""rocchio """



def sample_centroids(data):
    m=np.empty((data.shape[1] -1),dtype=float)
    for i in range (0,data.shape[1]-1):
        m[i]=np.mean(data[:,i],dtype=np.float64)
    return m

"""
Funcao para calcular distancia das amostras de teste ate os centroides de cada
classe
"""
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
            distances[z]=np.sqrt(np.sum(np.power(np.subtract(test_array[i,0:5],trainning_array[z,0:5]),2)))
        #min[0] = index of min value and min[1] is the min value
        #print(distances)
        distances = list(distances)
        min_index = distances.index(min(distances))
        #print(min_index)
        #print(min_index)
        labels.append(trainning_array[min_index,5])  
    return np.array(labels)

#calculando acurácia


def accuracy(labels,prediction):
    count=0
    for i in range(0,labels.shape[0]):
        if(labels[i]==prediction[i]):
            count=count+1
    return (count/len(labels))*100
#------------------------------------------------------------------
"""lendo os arquivos"""
data_test = pd.read_csv('nebulosa_test.txt',sep=' ',header = None)
data_trainning = pd.read_csv('nebulosa_train.txt',sep=' ',header = None)
#excluindo amostras que contenham dados incompletos (atributo c valor -100)
#remove_samples_by_value(data_test,7)
header=['A', 'B' ,'C', 'D', 'E', 'F', 'F', 'LABEL']
data_test.columns= header
data_trainning.columns=header
#removendo atributos que nao tem influencia na tarefa de classificacao
data_test=data_test.drop(columns=['A','B'])
data_trainning=data_trainning.drop(columns=['A', 'B'])
#transformando amostras de teste em um numpy array
samples_for_test = np.array(data_test)

#pre processamento por intervalo de valor dos atributos
samples_for_test=samples_for_test[(samples_for_test[:,0] >0)]
samples_for_test=samples_for_test[(samples_for_test[:,1] >0)]
samples_for_test=samples_for_test[(samples_for_test[:,2] >0)]
samples_for_test=samples_for_test[(samples_for_test[:,3] >0)]
samples_for_test=samples_for_test[(samples_for_test[:,4] >0)]


#separando amostras de treinamento por label
label1=data_trainning[data_trainning.LABEL == 1]
label1=np.array(label1)
label2=data_trainning[data_trainning.LABEL == 2]
label2=np.array(label2)
label3=data_trainning[data_trainning.LABEL == 3]
label3=np.array(label3)
#pre processamento por intervalo de valor dos atributos
label1=label1[(label1[:,0] >0) ]
label1=label1[(label1[:,1] >0) ]
label1=label1[(label1[:,2] >0) ]
label1=label1[(label1[:,3] >0) ]
label1=label1[(label1[:,4] >0) ]

label2=label2[(label2[:,0] >0) ]
label2=label2[(label2[:,1] >0) ]
label2=label2[(label2[:,2] >0) ]
label2=label2[(label2[:,3] >0) ]
label2=label2[(label2[:,4] >0) ]

label3=label3[(label3[:,0] >0) ]
label3=label3[(label3[:,1] >0) ]
label3=label3[(label3[:,2] >0) ]
label3=label3[(label3[:,3] >0) ]
label3=label3[(label3[:,4] >0) ]

#calculando centroides para as classes
C1=sample_centroids(label1)
C2=sample_centroids(label2)
C3=sample_centroids(label3)

#gerando novo  vetor de labels para amostras de teste 
prediction_vector_rocchio= rocchio(samples_for_test,C1,C2,C3)
labels_vector=samples_for_test[:,5]

accuracy_rocchio = accuracy(labels_vector,prediction_vector_rocchio)
print('Alternativa A - removendo apenas amostras com dados inconsistentes')

print("Accuracy using Rocchio: {0:.2f}%".format( accuracy_rocchio))
trainning_vector = np.concatenate((label1,label2,label3))
#print(len(trainning_vector))
prediction_vector_NN=NN(trainning_vector,samples_for_test)
accuracy_NN=accuracy(labels_vector,prediction_vector_NN)
print("Accuracy using NN: {0:.2f}%".format( accuracy_NN))
print('------------------------------------------------------------------')

#pre-processamento de outliers
#trocar valor de outlier por moda do atributo
rounded_trainning_vector = np.around(trainning_vector, decimals=0) 
rounded_test_vector = np.around(samples_for_test,decimals = 0)

def change_to_mode(array):
    for i in range(1,array.shape[0]-1):
        for j in range(1,array.shape[1]):
            if (array[i,j]<1 and array[i,j]>4):
                array[i,j] = int(stats.mode(array[i,:]))
    return array

print(rounded_trainning_vector)
rounded_test_vector = change_to_mode(rounded_test_vector)
rounded_trainning_vector = change_to_mode(rounded_trainning_vector)
print('-----------------------')
print(rounded_trainning_vector)