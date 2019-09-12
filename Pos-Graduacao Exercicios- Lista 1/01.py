#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:26:56 2019

@author: joelson
"""

import pandas as pd
import numpy as np

"""
função para separar as amostras de acordo com o label
ou seja:
data_label1
data_label3
data_label3
"""

def split_by_labels(data,label,labels_column):
    index_data_label=[]
    for i in range(0,len(data.index)):
        if(data.loc[i,labels_column]==label):
           index_data_label.append(i)
    return index_data_label

"""
função para calcular os centroides das classes
""" 

def sample_centroids(data,sample_index_list,n_atributes):
    m=np.empty((7),dtype=float)
    for i in range (0,n_atributes):
        m[i]=data.loc[sample_index_list,i].median()
    return m
        
#------------------------------------------------------------------
"""lendo os arquivos"""
data_test = pd.read_csv('nebulosa_test.txt',sep=' ',header = None)
#print(data)mposta por 8 atributos:
data_trainning = pd.read_csv('nebulosa_train.txt',sep=' ',header = None)
#print(data_train)

index_label1= split_by_labels(data_trainning,1,7)
index_label2= split_by_labels(data_trainning,2,7)
index_label3= split_by_labels(data_trainning,3,7)

C1=sample_centroids(data_trainning,index_label1,7)
print(C1)
C2=sample_centroids(data_trainning,index_label2,7)
print(C2)
C3=sample_centroids(data_trainning,index_label3,7)
print(C3)






    