import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def split_in_two(array):
        array_1=array[0:(round(array.shape[0]/2)+1),:]
        array_2=array[(round(array.shape[0]/2)+1):array.shape[0],:]
        c1= array_1[round(array_1.shape[0]/2),:]
        c2=array_2[round(array_2.shape[0]/2),:]
        return c1,c2


def distance(A_x,A_y,B_x,B_y):
    d = np.sqrt(math.pow(A_x-B_x,2)+math.pow(A_y-B_y,2))
    return d 
    

def labelling(array,C1,C2):
    label = np.zeros((array.shape[0]))
    for i in range(0,array.shape[0]):
        d1=distance(array[i,0],array[i,1],C1[0],C1[1])
        d2=distance(array[i,0],array[i,1],C2[0],C2[1])
        if(d1<d2):
            label[i] = 2
        else:
            label[i]=1
    return label
        
    #-------------------------------
data_set = pd.read_csv('jain.txt', sep="\t", header=None)
data_set=np.array(data_set)
labels_originais = data_set[:,2]
count_originais_2=np.array(np.where(labels_originais== 2))
count_originais_1=np.array(np.where(labels_originais== 1))
data_set=data_set[:,0:2]

#arbitrando C1 e C2
c_2,c_1=split_in_two(data_set)
#fazendo o vetor de labels pela primeira vez
label_vector = labelling(data_set,c_2,c_1)



#agora loop onde os novos centroides serao calculados de acordo com a media das
#amostras com o mesmo rotulo

flag = 1
count= 0
while flag == 1:
    count_label_2=np.array(np.where(label_vector== 2))
    count_label_1=np.array(np.where(label_vector== 1))
    
    C2 = np.zeros((2))
    C1 = np.zeros((2))
    C2[0]=np.mean(data_set[count_label_2,0])
    C2[1]=np.mean(data_set[count_label_2,1])
    C1[0]=np.mean(data_set[count_label_1,0])
    C1[1]=np.mean(data_set[count_label_1,1])
    old_label_vector = label_vector
    label_vector = labelling(data_set,C2,C1)
    
    if(label_vector.all() == old_label_vector.all()):
        count +=1
       
        if(count ==2):
            flag=0
            
    else:
        flag=1
        count = 0 
    
count_label_2_old = np.array(np.where(label_vector== 2))
count_label_1_old = np.array(np.where(label_vector== 1))


#plt.figure(0)
#plt.plot(data_set[count_originais_1,0].flatten(),data_set[count_originais_1,1].flatten(),'go',label='C1')
#plt.plot(data_set[count_originais_2,0].flatten(),data_set[count_originais_2,1].flatten(),'bo',label='C2')
#plt.xlabel('Atributo 1')
#plt.ylabel('Atributo 2')
#plt.title('Base de dados original (jain.txt) ')
#
#plt.legend(loc='best')
#plt.figure(1)
#plt.plot(data_set[count_label_1_old,0].flatten(),data_set[count_label_1_old,1].flatten(),'go',label='C1')
#plt.plot(data_set[count_label_2_old,0].flatten(),data_set[count_label_2_old,1].flatten(),'bo',label='C2')
#plt.xlabel('Atributo 1')
#plt.ylabel('Atributo 2')
#plt.title('Classificação k-means (jain.txt) ')
#plt.legend(loc='best')
#plt.show()


#plt.xlabel(data_set)/
#plt.ylabel(iris.feature_names[1]);


#agora com o algoritmo hierarquico (aglomerativo)
#inicialmente tem-se Numero de clusters = numero de amostras
#(matriz de similaridade)

def matriz_de_similaridade(array):
    SIMILARIDADE = np.zeros((array.shape[0],array.shape[0]))
    for i in range(0,SIMILARIDADE.shape[0]):
        for j in range(0,SIMILARIDADE.shape[0]):
            SIMILARIDADE[i,j]= distance(data_set[i,0],data_set[i,1],data_set[j,0],data_set[j,1])
    return(SIMILARIDADE)

M = matriz_de_similaridade(data_set)

for i in range(0,data_set.shape[0]):
    for j in range(0,data_set.shape[0]):
        if (i ==j):    
                M[i,j]=10000

#result1 = dist_min = np.argsort(M[:,6])[:3]
#result2 = dist_min = np.argsort(M[:,7])[:3]
#result3 = dist_min = np.argsort(M[:,8])[:3]
#result4 = dist_min = np.argsort(M[:,9])[:3]
#
#print('{} {} {} {}'.format(result1,result2,result3,result4))
Labels_novo = np.arange(0,data_set.shape[0],1)
#print(Labels_novo[4])
#print(Labels_novo[result1[0]])
#print(np.where(Labels_novo[0:2]==2))

#Labels_novo[3]=3
#Labels_novo[result[0]]=3
#print(Labels_novo)




flag=1
while (flag ==1):
    print("aqui comeca o loop")
    dist_min = np.argsort(M[:,0])[:3]
    Labels_novo[int(dist_min[0])]=0 
    for i in range(1,M.shape[0]-1):
        dist_min = np.argsort(M[:,i])[:3]
#        next_dist_min=np.argsort(M[:,i+1])[:3]
#        last_dist_min=np.argsort(M[:,i-1])[:3]
        if(Labels_novo[i]!=i): #fui rotulado!   
#            print(i)
            print("{} rotulado".format(i))
            continue
        else:#nao fui rotulado
            #se ninguem rotulou a msm amostra q eu
            print("{} {}" .format((np.asarray((np.where(Labels_novo[0:i]==Labels_novo[dist_min[0]])))).shape[1],i))
            if( np.asarray(np.where(Labels_novo[0:i]==dist_min[0])).shape[1]==0):
               # print("a")
                Labels_novo[int(dist_min[0])]=i #rotular         
            if(np.asarray(np.where(Labels_novo[0:i]==Labels_novo[dist_min[0]])).shape[1] !=0):
                
                print("entrei aqui")
                Labels_novo[int(dist_min[1])]=i
            #        if( dist_min[0]!=Labels_novo[dist_min[0]] and  dist_min[0]<i and dist_min[1]!=Labels_novo[dist_min[1]] and  dist_min[1]<i):
    #            print("entrei aqui2")
    #            Labels_novo[dist_min[2]]=i
            
                            
                
                
                
            
                
                
    flag=0

#print(np.sort(Labels_novo))
print(Labels_novo)

            
            
            



