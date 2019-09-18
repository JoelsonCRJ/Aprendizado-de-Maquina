#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:26:56 2019

@author: joelson
"""

import pandas as pd
import numpy as np

"""rocchio """

"""
função para separar as amostras de acordo com o label
ou seja:
data_label1
data_label3
data_label3
"""

def split_by_labels(data,label,labels_column):
    index = data[data.'{}'.format(labels_column) == label].index
    index_data_label = list(index)
    
    return index_data_label

"""
função para calcular os centroides das classes
""" 

def sample_centroids(data,sample_index_list,n_atributes):
    m=np.empty((7),dtype=float)
    for i in range (2,n_atributes):
        m[i]=data.loc[sample_index_list,i].median()
    return m

"""
Funcao para calcular distancia das amostras de teste ate os centroides de cada
classe
"""
def rocchio(data,Center_1,Center_2,Center_3,n_atributes):
    labels=[]
    euclidian=np.empty((3),dtype = float)
    for i in range(0,len(data)):
        for j in range(2,n_atributes):
            euclidian[0]=np.sqrt(np.power(np.sum(Center_1[j]-data.loc[i,'{}'.format(j)]),2))
            euclidian[1]=np.sqrt(np.power(np.sum(Center_2[j]-data.loc[i,'{}'.format(j)]),2))
            euclidian[2]=np.sqrt(np.power(np.sum(Center_3[j]-data.loc[i,'{}'.format(j)]),2))
            
        if(np.min(euclidian)==euclidian[0]):
            labels.append(1)
        elif(np.min(euclidian)==euclidian[1]):
            labels.append(2)
        else:
            labels.append(3)
    return labels

def NN(data_training,data_test):
    distances=[]
    labels=[]
    for i in range(0,len(data_test)):
        test=np.array(data_test.loc[i,0:6])
        for z in range(0,len(data_training)):
            trainning=np.array(data_training.loc[z,0:6])        
            distances.append(np.sqrt(np.sum(np.power(np.subtract(trainning,test),2))))
        
        #min[0] = index of min value and min[1] is the min value
        min = np.where(distances == np.amin(distances))
        index = int(min[0])
        labels.append(data_training.loc[index,7])
        distances.clear()
        
    return np.array(labels)

##calculando acurácian_atributes

def accuracy(labels,prediction):
    count=0
    for i in range(0,len(labels_vector)):
        if(labels[i]==prediction[i]):
            count=count+1
    return (count/len(labels))*100



def remove_samples_by_value(data,n_atributes):
    for i in range(0,len(data.index)):
        if(data.loc[i,:]<-100):
            print(i)
    #print(data)                
    return data
#------------------------------------------------------------------
"""lendo os arquivos"""
data_test = pd.read_csv('nebulosa_test.txt',sep=' ',header = None)
data_trainning = pd.read_csv('nebulosa_train.txt',sep=' ',header = None)
#excluindo amostras que contenham dados incompletos (atributo c valor -100)
#remove_samples_by_value(data_test,7)
header=['A', 'B' ,'C', 'D', 'E', 'F', 'F', 'LABEL']
data_test.columns= header
data_trainning.columns=header

data_test=data_test.drop(columns=['A','B'])
data_trainning=data_trainning.drop(columns=['A', 'B'])


#   data_trainning.drop(data_trainning[data_trainning[i] <= 0].index, inplace=True)


print(len(data_trainning))
#separando amostras por label
label1=data_trainning[data_trainning.LABEL == 1]
label1=np.array(label1)
label2=data_trainning[data_trainning.LABEL == 2]
label2=np.array(label2)
label3=data_trainning[data_trainning.LABEL == 3]
label3=np.array(label3)

print(label1[label1[:,1] != -100])
#calculando centroides para as classes
C1=sample_centroids(data_trainning,index_label1,7)
C2=sample_centroids(data_trainning,index_label2,7)
C3=sample_centroids(data_trainning,index_label3,7)


#gerando novo  vetor de labels para amostras de teste 
prediction_vector_rocchio= np.array(rocchio(data_test,C1,C2,C3,7))
labels_vector=np.array(data_test.loc[:,7])

accuracy_rocchio = accuracy(labels_vector,prediction_vector_rocchio)
   
print("Accuracy using Rocchio: {0:.2f}%".format( accuracy_rocchio))

prediction_vector_NN=NN(data_trainning,data_test)
accuracy_NN=accuracy(labels_vector,prediction_vector_NN)
print("Accuracy using NN: {0:.2f}%".format( accuracy_NN))
    