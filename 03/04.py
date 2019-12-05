# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = pd.read_csv("Concrete_Data.txt",sep='\t',header=None)
data=np.array(data)
#normalizando amostras pelo desvio padrão
print("a")
desvios_padroes = np.zeros((data.shape[1]),dtype=float)


for i in range (0,data.shape[1]):
    desvios_padroes[i]=np.std(data[:,i])
    for j in range (0,data.shape[0]):
        data[i,j] = data[i,j]/ desvios_padroes[i]

data_treino = data[0:773,:]
data_teste = data[773:data.shape[0],:]
print(data) 