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
    I11 = np.where(atreino[:,0]<=2)
    #print(I11)
    I12 = np.where(atreino[:,0]>2)
    a11 = atreino[I11,0]
    a12 = atreino[I12,0]
#    print(a11)
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



def noDois(ctreino,atreino):
    
    sdClasse = sd(ctreino)
    I11 = np.where(atreino[:,0]<=2)
    #print(I11)
    I12 = np.where(atreino[:,0]>2)
    a11 = atreino[I11,0]
    a12 = atreino[I12,0]
#    print(a11)
    SDR1 = sdClasse - (a11.size/atreino.size)*sd(a11) - (a12.size/atreino.size)*sd(a12)
    
    
    I21 = np.where(atreino[:,1]<=3)
    I22 = np.where(atreino[:,1]>3)
    a21 = atreino[I21,1]
    a22 = atreino[I22,1]
    
    SDR2 = sdClasse - (a21.size/atreino.shape[0])*sd(a21) - (a22.size/atreino.shape[0])*sd(a22)
    
    I41 = np.where(atreino[:,3]<=4)
    I42 = np.where(atreino[:,3]>4)
    a41 = atreino[I41,3]
    a42 = atreino[I42,3]
    
    SDR4 = sdClasse - (a41.size/atreino.shape[0])*sd(a41) - (a42.size/atreino.shape[0])*sd(a42)
    
    SDRF = np.array([SDR1,SDR2,SDR4])
    
    SDRF_max = np.amax(SDRF)
    INDEX = np.where(SDRF_max == np.amax(SDRF_max))
    
    return INDEX,I11,I12,I21,I22,I41,I42

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
print(a31)
#segundo nó
natreinoMenor = atreino[a31,:           ]
nctreinoMenor = ctreino[a31,:]
natreinoMaior = atreino[a32,:]
nctreinoMaior = ctreino[a32,:]

index2Menor,_,_,_,_,i41,i42  = noDois(nctreinoMenor,natreinoMenor)


