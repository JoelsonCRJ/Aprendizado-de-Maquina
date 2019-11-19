import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math



def sd(a):
    media = np.mean(a)
    v1=np.power((a-media),2)
    v2=np.sum(v1)
    v3=v2/a.size
    v4=np.sqrt(v3)
    return v4


def noUm(ctreino,atreino):
    sdClasse=sd(ctreino)
    I11 = np.array(np.where(atreino[:,0]<=2))
    
    I12 = np.where(atreino[:,0]>2)
    a11 = atreino[I11,0]
    a12 = atreino[I12,0]
    SDR1 = sdClasse - (a11.size/atreino.size)*sd(a11) - (a12.size/atreino.size)*sd(a12)
    
    
    I21 = np.where(atreino[:,1]<=3)
    I22 = np.where(atreino[:,1]>3)
    a21 = atreino[I21,1]
    a22 = atreino[I22,1]
    
    SDR2 = sdClasse - (a21.size/atreino.shape[0])*sd(a21) - (a22.size/atreino.shape[0])*sd(a22)
    I31 = np.where(atreino[:,2]<=5)
    I32 = np.where(atreino[:,2]>5)
    a31 = atreino[I31,2]
    a32 = atreino[I32,2]
    
    SDR3 = sdClasse - (a31.size/atreino.shape[0])*sd(a31) - (a32.size/atreino.shape[0])*sd(a32)
    I41 = np.where(atreino[:,3]<=4)
    I42 = np.where(atreino[:,3]>4)
    a41 = atreino[I41,3]
    a42 = atreino[I42,3]
    
    SDR4 = sdClasse - (a41.size/atreino.shape[0])*sd(a41) - (a42.size/atreino.shape[0])*sd(a42)
    
    SDRF = np.array([SDR1,SDR2,SDR3,SDR4])
    
    SDRF_max = np.amax(SDRF)
    INDEX = np.where(SDRF_max == np.amax(SDRF_max))
    
    return INDEX,I31,I32



def noDois(ctreino,atrain):
#    print(atreino)
    sdClasse = sd(ctreino)
    J11 = np.array(np.where(atrain[:,0]<=2))
    
    J12 = np.where(atrain[:,0]>2)
    
    a11 = atrain[J11,0]
    a12 = atrain[J12,0]
#    print(a11)
    SDR1 = sdClasse - (a11.size/atrain.size)*sd(a11) - (a12.size/atrain.size)*sd(a12)
    
    
    J21 = np.where(atrain[:,1]<=3)
    J22 = np.where(atrain[:,1]>3)
    a21 = atrain[J21,1]
    a22 = atrain[J22,1]
    
    SDR2 = sdClasse - (a21.size/atrain.shape[0])*sd(a21) - (a22.size/atrain.shape[0])*sd(a22)
    
    J41 = np.where(atrain[:,3]<=4)
    J42 = np.where(atrain[:,3]>4)
    a41 = atrain[J41,3]
    a42 = atrain[J42,3]
    SDR4 = sdClasse - (a41.size/atrain.shape[0])*sd(a41) - (a42.size/atrain.shape[0])*0 #a42=0
    
    SDRF = np.array([SDR1,SDR2,SDR4])
    
    SDRF_max = np.amax(SDRF)
    INDEX = np.where(SDRF_max == np.amax(SDRF_max))
    
    return INDEX,J11,J12,J21,J22,J41,J42





#------------------------------------------------------------
data = pd.read_csv('servo.txt', sep=",", header=None)
data = np.array(data)
#print(data)
"""
 1. motor: A,B,C,D,E = 1,2,3,4,5
 2. screw: A,B,C,D,E = 1,2,3,4,5
 3. pgain: 3,4,5,6
 4. vgain: 1,2,3,4,5
 5. class: 0.13 to 7.10"""
#mudanca dos dois primeiros atributos para numeros
for i in range(0,2):
    data[:,i]=np.where(data[:,i]== 'A', 1, data[:,i])
    data[:,i]=np.where(data[:,i]== 'B', 2, data[:,i])
    data[:,i]=np.where(data[:,i]== 'C', 3, data[:,i])
    data[:,i]=np.where(data[:,i]== 'D', 4, data[:,i])
    data[:,i]=np.where(data[:,i]== 'E', 5, data[:,i])
    
atributos = data[:,0:4]
classes = data[:,4]
atreino = atributos[0:round(0.75*atributos.shape[0])+1,:]
ctreino = classes[0:round(classes.shape[0]*0.75)+1]

ateste= atributos[atreino.shape[0]:atributos.shape[0]+1,:]
cteste= classes[ctreino.shape[0]:classes.shape[0]+1]



#Alternativa A 
#primeiro nó
index1,a31,a32 = noUm(ctreino,atreino)
a31=np.array(a31)
a32=np.array(a32)
natreinoMenor = np.squeeze(atreino[a31],axis=0)
nctreinoMenor = np.squeeze(ctreino[a31],axis=0)
natreinoMaior = np.squeeze(atreino[a32],axis=0)
nctreinoMaior = np.squeeze(ctreino[a32],axis=0)
#segundo nó
index2Menor,_,_,_,_,i41,i42  = noDois(nctreinoMenor,natreinoMenor)
index2Maior,_,_,i21,i22,_,_=noDois(nctreinoMaior,natreinoMaior)

#árvore de regressão
C1 = np.squeeze(np.where((atreino[:,2]<=5) & (atreino[:,3]<=4)),axis=0)
media1=np.mean(np.take(ctreino,C1))
C2 = np.where((atreino[:,2]<=5) & (atreino[:,3]<4))
media2=np.mean(np.take(ctreino,C2))
C3 = np.where((atreino[:,2]>5) & (atreino[:,3]<=3))
media3=np.mean(np.take(ctreino,C3))
C4 = np.where((atreino[:,2]>5) & (atreino[:,3]>4))
media4=np.mean(np.take(ctreino,C4))


#alternativa b
rotulo=np.zeros((ateste.shape[0]))
for i in range(0,ateste.shape[0]):
    if (ateste[i,2]<=4):
        if(ateste[i,3]<=4):
            rotulo[i]=media1
        elif(ateste[i,3]>4):
            rotulo[i]=media2
    elif(ateste[i,2]>4):
        if(ateste[i,1]<=3):
            rotulo[i]=media3
        elif(ateste[i,1]>3):
            rotulo[i]=media4


MAPE = np.sum(abs(cteste-rotulo)/abs(cteste))/len(cteste)*100
print(MAPE)

RMSE = np.sqrt(np.sum(np.power(cteste-rotulo,2))/len(cteste))
print(RMSE)

