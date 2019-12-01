import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

#functions
def split_in_three(array):
        array_1=array[0:(round(array.shape[0]/3)+1),:]
        array_2=array[(round(array.shape[0]/3)+1):(round(2*array.shape[0]/3)+1),:]
        array_3=array[(round(2*array.shape[0]/3)+1):array.shape[0],:]
        c1= array_1[round(array_1.shape[0]/2),:]
        c2=array_2[round(array_2.shape[0]/2),:]
        c3=array_3[round(array_3.shape[0]/2),:]
        return c1,c2,c3

def distance(A_x,A_y,B_x,B_y):
    d = np.sqrt(math.pow(A_x-B_x,2)+math.pow(A_y-B_y,2))
    return d 

def labelling(array,C1,C2,C3):
    label = np.zeros((array.shape[0]))
    for i in range(0,array.shape[0]):
        d1=distance(array[i,0],array[i,1],C1[0],C1[1])
        d2=distance(array[i,0],array[i,1],C2[0],C2[1])
        d3=distance(array[i,0],array[i,1],C3[0],C3[1])
        if(d1<d2 and d1<d3):
            label[i] = 1
        elif(d2<d1 and d2<d3):
            label[i]=2
        elif(d3<d1 and d3<d2):
            label[i]=3
    return label


#-------------------
data_set = pd.read_csv("spiral.txt",sep="\t",header= None)
data_set=np.array(data_set)
labels_originais = data_set[:,2]
count_originais_2=np.array(np.where(labels_originais== 2))
count_originais_1=np.array(np.where(labels_originais== 1))
count_originais_3=np.array(np.where(labels_originais== 3))
data_set=data_set[:,0:2]

#arbitrando C1 e C2
c_1,c_2,c_3=split_in_three(data_set)
#fazendo o vetor de labels pela primeira vez
label_vector = labelling(data_set,c_1,c_2,c_3)
print(label_vector)


#agora loop onde os novos centroides serao calculados de acordo com a media das
#amostras com o mesmo rotulo

flag = 1
count= 0
while flag == 1:
    count_label_2=np.array(np.where(label_vector== 2))
    count_label_1=np.array(np.where(label_vector== 1))
    count_label_3=np.array(np.where(label_vector== 3))
    C2 = np.zeros((2))
    C1 = np.zeros((2))
    C3=np.zeros((2))
    C2[0]=np.mean(data_set[count_label_2,0])
    C2[1]=np.mean(data_set[count_label_2,1])
    C1[0]=np.mean(data_set[count_label_1,0])
    C1[1]=np.mean(data_set[count_label_1,1])
    C3[0]=np.mean(data_set[count_label_3,0])
    C3[1]=np.mean(data_set[count_label_3,1])
    old_label_vector = label_vector
    label_vector = labelling(data_set,C1,C2,C3)
    print(np.array_equal(label_vector,old_label_vector))
    if(np.array_equal(label_vector,old_label_vector)):
        count +=1
        print(count)
        if(count ==3):
            flag=0
            print(label_vector)
    else:
        flag=1
        count = 0 
        
plt.figure(0)
plt.plot(data_set[count_originais_1,0].flatten(),data_set[count_originais_1,1].flatten(),'go',label='C1')
plt.plot(data_set[count_originais_2,0].flatten(),data_set[count_originais_2,1].flatten(),'bo',label='C2')
plt.plot(data_set[count_originais_3,0].flatten(),data_set[count_originais_3,1].flatten(),'ro',label='C3')

plt.xlabel('Atributo 1')
plt.ylabel('Atributo 2')
plt.title('Base de dados original (spiral.txt) ')

plt.legend(loc='best')
plt.figure(1)
plt.plot(data_set[count_label_1,0].flatten(),data_set[count_label_1,1].flatten(),'go',label='C1')
plt.plot(data_set[count_label_2,0].flatten(),data_set[count_label_2,1].flatten(),'bo',label='C2')
plt.plot(data_set[count_label_3,0].flatten(),data_set[count_label_3,1].flatten(),'ro',label='C3')
plt.xlabel('Atributo 1')
plt.ylabel('Atributo 2')
plt.title('Classificação k-means (jain.txt) ')
plt.legend(loc='best')
plt.show()