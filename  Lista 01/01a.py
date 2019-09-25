#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:26:56 2019

@author: joelson
"""

import pandas as pd
import numpy as np
from scipy import stats
from my_awesome_functions import *

#------------------------------------------------------------------
"""lendo os arquivos"""
data_test = pd.read_csv('nebulosa_test.txt',sep=' ',header = None)
data_trainning = pd.read_csv('nebulosa_train.txt',sep=' ',header = None)
#excluindo amostras que contenham dados incompletos (atributo c valor -100)
#remove_samples_by_value(data_test,7)
header=['A', 'B' ,'C', 'D', 'E', 'F', 'G', 'LABEL']
data_test.columns= header
data_trainning.columns=header
#removendo atributos que nao tem influencia na tarefa de classificacao
data_test=data_test.drop(columns=['A','B','G']) 
data_trainning=data_trainning.drop(columns=['A', 'B' , 'G'])
#transformando amostras de teste em um numpy array
samples_for_test = np.array(data_test)
data_trainning=np.array(data_trainning)

#separando amostras de treinamento por label
label1,label2,label3=split_by_labels(data_trainning)
#pre processamento para dados inconsistentes
label1=drop_incomplete(label1)
label2=drop_incomplete(label2)
label3=drop_incomplete(label3)
samples_for_test=drop_incomplete(samples_for_test)
#calculando centroides para as classes
C1=sample_centroids(label1)
C2=sample_centroids(label2)
C3=sample_centroids(label3)

#gerando novo  vetor de labels para amostras de teste 
prediction_vector_rocchio= rocchio(samples_for_test,C1,C2,C3)
labels_vector=samples_for_test[:,4]

accuracy_rocchio = accuracy(labels_vector,prediction_vector_rocchio)
print('Alternativa A - removendo apenas amostras com dados inconsistentes')

print("Accuracy using Rocchio: {0:.2f}%".format( accuracy_rocchio))
trainning_vector = np.concatenate((label1,label2,label3))
#print(len(trainning_vector))
prediction_vector_NN=NN(trainning_vector,samples_for_test)
accuracy_NN=accuracy(labels_vector,prediction_vector_NN)
print("Accuracy using NN: {0:.2f}%".format( accuracy_NN))
print('------------------------------------------------------------------')

#pre-processamento de ruido
#arredondar os valores para numeros inteiros
rounded_trainning_vector = np.around(trainning_vector, decimals=0) 
rounded_test_vector = np.around(samples_for_test,decimals = 0)
#pre-processamento para outliers
#substituir outliers pela moda de seu respectivo atributo
rounded_trainning_vector = replace_by_mode(rounded_trainning_vector)
rounded_test_vector = replace_by_mode(rounded_test_vector)
#separando conjunto de treino por label
label1_n,label2_n,label3_n=split_by_labels(rounded_trainning_vector)
#calculando centroides para as classes
C1_n=sample_centroids(label1_n)
C2_n=sample_centroids(label2_n)
C3_n=sample_centroids(label3_n)

#gerando novo  vetor de labels para amostras de teste 
prediction_vector_rocchio= rocchio(rounded_test_vector,C1_n,C2_n,C3_n)
labels_vector=rounded_test_vector[:,4]

print('Alternativa B - filtrando ruido e outliers')

accuracy_rocchio = accuracy(labels_vector,prediction_vector_rocchio)
print("Accuracy using Rocchio: {0:.2f}%".format( accuracy_rocchio))
prediction_vector_NN=NN(rounded_trainning_vector,rounded_test_vector)
accuracy_NN=accuracy(labels_vector,prediction_vector_NN)
print("Accuracy using NN: {0:.2f}%".format( accuracy_NN))