import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats


test_dataset = pd.read_csv('monks-2_test.txt', sep=" ", header=None)
train_dataset= pd.read_csv('monks-2_train.txt', sep=" ", header=None)


#id_train=train_dataset.loc[:,8]
#print(id_train)

"""calcular medias e desvio padrao de cada atributo 
lembrando que a primeira, segunda e última coluna poderam ser desprezadas
pois são, respectivamente label e id"""

train_dataset=np.array(train_dataset)
test_dataset=np.array(test_dataset)

labels = test_dataset[:,1]
#print(labels)
#separar as amostras por classe 0 e 1
treino1 = train_dataset[train_dataset[:,1]==1]
treino0=train_dataset[train_dataset[:,1]==0]
#print(treino0)
#quantidades
qTotal = train_dataset.shape[0]
q0 = treino0.shape[0]
q1 = treino1.shape[0]

#calculando as medias e desvios de cada atributo
#media classe 0
mediaX1_0 = np.mean(treino0[:,2],axis=0)
mediaX2_0 = np.mean(treino0[:,3],axis=0)
mediaX3_0= np.mean(treino0[:,4],axis=0)
mediaX4_0= np.mean(treino0[:,5],axis=0)
mediaX5_0= np.mean(treino0[:,6],axis=0)
mediaX6_0= np.mean(treino0[:,7],axis=0)
#desvio padrao classe 0
desvioX1_0 = np.std(treino0[:,2],axis=0)
desvioX2_0 = np.std(treino0[:,3],axis=0)
desvioX3_0= np.std(treino0[:,4],axis=0)
desvioX4_0= np.std(treino0[:,5],axis=0)
desvioX5_0= np.std(treino0[:,6],axis=0)
desvioX6_0= np.std(treino0[:,7],axis=0)

#media classe 1
mediaX1_1 = np.mean(treino1[:,2],axis=0)
mediaX2_1 = np.mean(treino1[:,3],axis=0)
mediaX3_1= np.mean(treino1[:,4],axis=0)
mediaX4_1= np.mean(treino1[:,5],axis=0)
mediaX5_1= np.mean(treino1[:,6],axis=0)
mediaX6_1= np.mean(treino1[:,7],axis=0)
#desvio padrao classe 1
desvioX1_1 = np.std(treino1[:,2],axis=0)
desvioX2_1= np.std(treino1[:,3],axis=0)
desvioX3_1= np.std(treino1[:,4],axis=0)
desvioX4_1= np.std(treino1[:,5],axis=0)
desvioX5_1= np.std(treino1[:,6],axis=0)
desvioX6_1= np.std(treino1[:,7],axis=0)

probabilidades = np.zeros((len(test_dataset),2))

print(probabilidades.shape)

#classificando
for j in range(len(test_dataset)):
        #Gaussiana 0
        gauX1_0 = scipy.stats.norm(mediaX1_0, desvioX1_0).pdf(test_dataset[j,2])
        gauX2_0 = scipy.stats.norm(mediaX2_0, desvioX2_0).pdf(test_dataset[j,3])
        gauX3_0 = scipy.stats.norm(mediaX3_0, desvioX3_0).pdf(test_dataset[j,4])
        gauX4_0= scipy.stats.norm(mediaX4_0, desvioX4_0).pdf(test_dataset[j,5])
        gauX5_0 = scipy.stats.norm(mediaX5_0, desvioX5_0).pdf(test_dataset[j,6])
        gauX6_0= scipy.stats.norm(mediaX6_0, desvioX6_0).pdf(test_dataset[j,7])
    
        #Gaussiana 1
        gauX1_1 = scipy.stats.norm(mediaX1_1, desvioX1_1).pdf(test_dataset[j,2])
        gauX2_1 = scipy.stats.norm(mediaX2_1, desvioX2_1).pdf(test_dataset[j,3])
        gauX3_1 = scipy.stats.norm(mediaX3_1, desvioX3_1).pdf(test_dataset[j,4])
        gauX4_1= scipy.stats.norm(mediaX4_1, desvioX4_1).pdf(test_dataset[j,5])
        gauX5_1 = scipy.stats.norm(mediaX5_1, desvioX5_1).pdf(test_dataset[j,6])
        gauX6_1= scipy.stats.norm(mediaX6_1, desvioX6_1).pdf(test_dataset[j,7])
        
        probabilidades[j,0] = gauX1_0 * gauX2_0 * gauX3_0 * gauX4_0 * gauX5_0 *gauX6_0*(q0 / qTotal)
        probabilidades[j,1] = gauX1_1 * gauX2_1 * gauX3_1 * gauX4_1 * gauX5_1 *gauX6_1*(q1 / qTotal)
        
label_teste = np.zeros(len(test_dataset))
label_teste = np.argmax(probabilidades, axis=1)

def accuracy(lab, lab_teste):
    erros = 0
    for i in range(lab.shape[0]):
        if lab_teste[i] != lab[i]:
            erros = erros + 1
    return ((lab_teste.shape[0] - erros)/lab_teste.shape[0])*100

Accuracy= accuracy(labels,label_teste)
print("Accuracy using Naive Bayes: {0:.2f}%".format( Accuracy))
