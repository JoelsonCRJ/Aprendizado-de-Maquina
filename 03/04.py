# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = pd.read_csv("Concrete_Data.txt",sep='\t',header=None)
data=np.array(data)
#normalizando amostras pelo desvio padrão

X= data[:,0:9]
print(X)



for i in range (0,X.shape[1]):
  
        X[:,i] = X[:,i]/ np.std(X[:,i])

#tudo normalizado
        
#dividindo treino e teste        
data_treino = X[0:773,:]
data_teste = X[773:data.shape[0],:]
print(X)

def GRNN(data_treino,data_teste,sigma):
    teste = data_teste[:,0:8]
    saida_teste= data_teste[:,8]
    treino = data_treino[:,0:8]
    saida_treino= data_treino[:,8]
    saida = np.zeros((saida_teste.shape[0]))
    denominador = np.zeros((treino.shape[0]))
    numerador = np.zeros((treino.shape[0]))
    for i in range(0,data_teste.shape[0]):
        for j in range(0,data_treino.shape[0]):
            denominador[j] = np.exp(np.dot(-teste[i,:]+treino[j,:],np.transpose(teste[i,:]-treino[j,:]))/(2*np.power(sigma,2)))
            numerador[j] = saida_treino[j]*np.exp((-(teste[i,:]-treino[j,:])*np.transpose(teste[i,:]-treino[j,:]))/2*np.power(sigma,2))
        saida[i] = np.sum(numerador)/np.sum(denominador)
    
    RMSE = np.sqrt(np.sum(np.power(saida-saida_teste,2))/saida_teste.shape[0])
    return saida, RMSE

print(GRNN(data_treino,data_teste,1))

