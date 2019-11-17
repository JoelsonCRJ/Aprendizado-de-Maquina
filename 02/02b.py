import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats


def accuracy(lab, lab_teste):
    erros = 0
    for i in range(lab.shape[0]):
        if lab_teste[i] != lab[i]:
            erros = erros + 1
    return ((lab_teste.shape[0] - erros)/lab_teste.shape[0])*100


def discretiza_v(X):
    discretizado = []
    for i in range(1):
        discretizado.append(np.count_nonzero(X == i+1))  
    return discretizado
"""calcular medias e desvio padrao de cada atributo 
lembrando que a primeira, segunda e última coluna poderam ser desprezadas
pois são, respectivamente label e id"""
test_dataset = pd.read_csv('monks-2_test.txt', sep=" ", header=None)
test_dataset=np.array(test_dataset)
train_dataset= pd.read_csv('monks-2_train.txt', sep=" ", header=None)
train_dataset=np.array(train_dataset)

#separar as amostras por classe 0 e 1
treino1 = train_dataset[train_dataset[:,1]==1]
treino0=train_dataset[train_dataset[:,1]==0]
#print(treino0)
#quantidades
qTotal = train_dataset.shape[0]
q0 = treino0.shape[0]
q1 = treino1.shape[0]


#discretizando classe 0
discretizaX1_0 = discretiza_v(treino0[:,2])
discretizaX2_0 = discretiza_v(treino0[:,3])
discretizaX3_0= discretiza_v(treino0[:,4])
discretizaX4_0= discretiza_v(treino0[:,5])
discretizaX5_0= discretiza_v(treino0[:,6])
discretizaX6_0= discretiza_v(treino0[:,7])
#discretizando classe 1
discretizaX1_1 = discretiza_v(treino1[:,2])
discretizaX2_1 = discretiza_v(treino1[:,3])
discretizaX3_1 = discretiza_v(treino1[:,4])
discretizaX4_1 = discretiza_v(treino1[:,5])
discretizaX5_1 = discretiza_v(treino1[:,6])
discretizaX6_1 = discretiza_v(treino1[:,7])

probabilidades = np.zeros((len(test_dataset),2))
probabilidades_s = np.zeros((len(test_dataset),2))

print(probabilidades.shape)

#classificando
for j in range(len(test_dataset)):
        #Classe 0
        X1_0 = discretizaX1_0[test_dataset[j,2]-1] / (sum(discretizaX1_0))
        X2_0 = discretizaX2_0[test_dataset[j,3]-1] / (sum(discretizaX2_0))
        X3_0 = discretizaX3_0[test_dataset[j,4]-1] / (sum(discretizaX3_0))
        X4_0 = discretizaX4_0[test_dataset[j,5]-1] / (sum(discretizaX4_0))
        X5_0 = discretizaX5_0[test_dataset[j,6]-1] / (sum(discretizaX5_0))
        print(X5_0)
        X6_0 = discretizaX6_0[test_dataset[j,7]-1] / (sum(discretizaX6_0))
        
        #Classe 0 com suavizacao
        X1_0s= (discretizaX1_0[test_dataset[j,2]-1]+1) / (sum(discretizaX1_0)+1)
        X2_0s= (discretizaX2_0[test_dataset[j,3]-1]+1) / (sum(discretizaX2_0)+1)
        X3_0s= (discretizaX3_0[test_dataset[j,4]-1]+1) / (sum(discretizaX3_0)+1)
        X4_0s= (discretizaX4_0[test_dataset[j,5]-1]+1) / (sum(discretizaX4_0)+1)
        X5_0s= (discretizaX5_0[test_dataset[j,6]-1]+1) / (sum(discretizaX5_0)+1)
        X6_0s= (discretizaX6_0[test_dataset[j,7]-1]+1) / (sum(discretizaX6_0)+1)

         #Classe 1
        X1_1 = discretizaX1_1[test_dataset[j,2]-1] / (sum(discretizaX1_1))
        X2_1 = discretizaX2_1[test_dataset[j,3]-1] / (sum(discretizaX2_1))
        X3_1 = discretizaX3_1[test_dataset[j,4]-1] / (sum(discretizaX3_1))
        X4_1 = discretizaX4_1[test_dataset[j,5]-1] / (sum(discretizaX4_1))
        X5_1 = discretizaX5_1[test_dataset[j,6]-1] / (sum(discretizaX5_1))
        X6_1 = discretizaX6_1[test_dataset[j,7]-1] / (sum(discretizaX6_1))
        
        #Classe 1 com suavizacao
        X1_1s = (discretizaX1_1[test_dataset[j,2]-1]+1) / (sum(discretizaX1_1)+1)
        X2_1s = (discretizaX2_1[test_dataset[j,3]-1]+1) / (sum(discretizaX2_1)+1)
        X3_1s = (discretizaX3_1[test_dataset[j,4]-1]+1) / (sum(discretizaX3_1)+1)
        X4_1s = (discretizaX4_1[test_dataset[j,5]-1]+1) / (sum(discretizaX4_1)+1)
        X5_1s = (discretizaX5_1[test_dataset[j,6]-1]+1) / (sum(discretizaX5_1)+1)
        X6_1s = (discretizaX6_1[test_dataset[j,7]-1]+1) / (sum(discretizaX6_1)+1)


        probabilidades[j,0] = X1_0*X2_0*X3_0*X4_0*X5_0*X6_0*(q0 / qTotal)
        probabilidades[j,1] = X1_1*X2_1*X3_1*X4_1*X5_1*X6_1*(q1/qTotal)

        probabilidades_s[j,0] = X1_0s*X2_0s*X3_0s*X4_0s*X5_0s*X6_0s*(q0 / qTotal)
        probabilidades_s[j,1] = X1_1s*X2_1s*X3_1s*X4_1s*X5_1s*X6_1s*(q0 / qTotal)

label_teste = np.zeros(len(test_dataset))
label_teste = np.argmax(probabilidades, axis=1)

label_teste_s = np.zeros(len(test_dataset))
label_teste_s = np.argmax(probabilidades_s, axis=1)

Accuracy= accuracy(labels,label_teste)
Accuracy_s= accuracy(labels,label_teste)
print("Accuracy using Naive Bayes + discretization: {0:.2f}%".format( Accuracy))
print("Accuracy using Naive Bayes + discretization+ LaPlace: {0:.2f}%".format( Accuracy))