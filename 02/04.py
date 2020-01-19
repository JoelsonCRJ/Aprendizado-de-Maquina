
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math


#alternativa a 
#probabilidades condicionais e a priori de cada nós
dados = np.genfromtxt('transito.txt',delimiter="")
print(dados)
data = dados


#chuva
ProbC = len(data[data[:,0]==1])/len(data)
print('P(C)={0:.2f}'.format(ProbC))

#feriado
ProbF = len(data[data[:,1]==1])/len(data)
print('P(F) = {0:.2f}'.format(ProbF))

C1 = C2 = 0
for i in range(0,len(data)):
    if(data[i,0]== 0 and data[i,3] == 0):
        C1 = C1 +1
    if(data[i,0]== 1 and data[i,3] == 1):
        C2 = C2 +1
Rua_al_f = C1/len(data)
Rua_al_f = C2/len(data)  

print("chuva / R alagada = 0 e Chuva = 0: " +str((Rua_al_f/(1-ProbC))))
print("chuva / R alagada = 1 e Chuva = 0: " +str(100-(Rua_al_f/(1-ProbC))))
print("chuva / R alagada = 1 e Chuva = 0: " +str(100 - (Rua_al_f/ProbC)))
print("chuva / R alagada = 1 e Chuva = 1: " +str((Rua_al_f/ProbC)))

C1 = C2 = C3 = C4 = C5 = C6 = C7 = C8 = 0
for i in range(0,len(data)):
    if(data[i,3]== 0 and data[i,2] == 0 and data[i,4] == 0):
        C1 = C1 +1
    if(data[i,3]== 0 and data[i,2] == 1 and data[i,4] == 0):
        C2 = C2 +1
    if(data[i,3]== 1 and data[i,2] == 0 and data[i,4] == 0):
        C3 = C3 +1
    if(data[i,3]== 1 and data[i,2] == 1 and data[i,4] == 0):
        C4 = C4 +1
        # P(Ra,E)        
    if(data[i,3]== 0 and data[i,2] == 0):
        C5 = C5 +1
    if(data[i,3]== 1 and data[i,2] == 0):
        C6 = C6 +1
    if(data[i,3]== 0 and data[i,2] == 1):
        C7 = C7 +1
    if(data[i,3]== 1 and data[i,2] == 1):
        C8 = C8 +1

R_alag_enga_A1 = C1/len(data)
R_alag_enga_A2 = C2/len(data)  
R_alag_enga_A3 = C3/len(data)
R_alag_enga_A4 = C4/len(data)   
Rua_ala_E1 = C5/len(data) 
Rua_ala_E2 = C6/len(data)
Rua_ala_E3 = C7/len(data)
Rua_ala_E4 = C8/len(data)
print("R alagada = 0, Engarrafamento = 0 e Acidente = 0: " +str((R_alag_enga_A1/(Rua_ala_E1))))
print("R alagada = 0, Engarrafamento = 0 e Acidente = 1: " +str(100-(R_alag_enga_A1/(Rua_ala_E1))))
print("R alagada = 0, Engarrafamento = 1 e Acidente = 0: " +str((R_alag_enga_A2/Rua_ala_E3)))
print("R alagada = 0, Engarrafamento = 1 e Acidente = 1:" +str(100-(R_alag_enga_A2/Rua_ala_E3)))
print("R alagada = 1, Engarrafamento = 0 e Acidente = 0: " +str(R_alag_enga_A3/Rua_ala_E2))
print("R alagada = 1, Engarrafamento = 0 e Acidente = 1: " +str(100-(R_alag_enga_A3/Rua_ala_E2)))
print("R alagada = 1, Engarrafamento = 1 e Acidente = 0: " +str(R_alag_enga_A4/Rua_ala_E4))
print("R alagada = 1, Engarrafamento = 1 e Acidente = 1: " +str(100-(R_alag_enga_A4/Rua_ala_E4)))



#alternativa b
#P(Acidente = 1|R Alagadas= 1)

ProbRL = len(data[data[:,3]==1])/len(data)

C = 0
for i in range(0,len(data)):
    if(data[i,3]== 1 and data[i,4] == 1):
        C = C +1
Prob_R_L = C/len(data)    
print("P(Acidente = 1|R Alagadas = 1) = {0:.2f} %" .format((Prob_R_L/ProbRL)*100))


#alternativa C 
#(P(Feriado = 1|Chuva = 1, Engarrafamento = 1))
C1 = C2 = 0
for i in range(0,len(data)):
    if(data[i,0]== 1 and data[i,2] == 1 and data[i,1]==0):
        C2 = C2 +1
    if(data[i,0]== 1 and data[i,2] == 1):
        C1 = C1 +1

Prob_E_RA_A = C2/len(data)
Prob_E_RA = C1/len(data)  
print("P(Feriado = 1|Chuva = 1, Engarrafamento= 1) = {0:.2f}%" .format((100-(Prob_E_RA_A/Prob_E_RA)*100)))