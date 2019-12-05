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
#----------funcoes para algoritmo hierarquico
def distanciaEuclidiana(Y):
    
    distanciaMatriz = np.zeros((Y.shape[0],Y.shape[0]))
    
    for j in range(0,Y.shape[0]):
        for i in range(j+1,Y.shape[0]):
            subtracaoVetor = np.subtract(Y[j,:],Y[i,:])
            elevQuadradoVetor = np.power(subtracaoVetor,2)
            somaVetor = np.sum(elevQuadradoVetor)
            distanciaMatriz[j,i] = np.sqrt(somaVetor)
            distanciaMatriz[i,j] = np.sqrt(somaVetor)
        
    return distanciaMatriz

def minimos(distanciaMatriz):
# Com a matriz de distância, achar os valores minimos para se construir os clustersJain
    for i in range(0,Y.shape[0]):
        
        # menor distancia (sem considerar o 0)
        vetorDistIndMin[i,0] = np.amin(distanciaMatriz[i,np.nonzero(distanciaMatriz[i,:])]) 
        
        # vetor do indice que ele ta saindo(linha) 
        vetorDistIndMin[i,1] = i
        
        # Checar os indices das menores distancias para saber a coluna
        vetorDistIndMin[i,2] = np.argwhere(distanciaMatriz[i,:] == vetorDistIndMin[i,0])[0][0] 
        
    return vetorDistIndMin

#----- funcao para acuracia
def mostFrequent(arr, n): 
  
    # Sort the array 
    arr.sort() 
    
    # find the max frequency using 
    # linear traversal 
    max_count = 1; res = arr[0]; curr_count = 1
      
    for i in range(1, n):  
        if (arr[i] == arr[i - 1]): 
            curr_count += 1
              
        else : 
            if (curr_count > max_count):  
                max_count = curr_count 
                res = arr[i - 1] 
              
            curr_count = 1
      
    # If last element is most frequent 
    if (curr_count > max_count): 
      
        max_count = curr_count 
        res = arr[n - 1] 
      
    return res,max_count
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






#----- algoritmo hierarquico
Y=data_set[:,0:2]
classesJain=labels_originais
# Vetor que conterá a distancia minima e os dois indices a qual essa distancia pertence
vetorDistIndMin = np.zeros((Y.shape[0],3))

# Vetor que terá os clusters de cada indice
clustersJain = np.zeros((Y.shape[0]))


distanciaMatriz = distanciaEuclidiana(Y)

First = True
breaki = False

# Ate entrar no criterio de parada
while(True):
    # função para achar a distancia minima e seus indices
    vetorDistIndMin = minimos(distanciaMatriz)
    # organizar o vetor começando pela menor distancia
    vetorOrganizado = vetorDistIndMin[vetorDistIndMin[:,0].argsort()]    
     
    
    for i in range(0,Y.shape[0]):    
        
        # Caso não seja a primeira vez (na primeira vez os primeiros vão receber o mesmo cluster)
        if(not First):
            
            # para uma dada amostra A, checa se a amostraB  que tem a menor distancia com ela
            # ja tem um cluster ou nao.
            
            # Se B ja tem um cluster
            if(clustersJain[vetorOrganizado[i,2].astype(int)] != 0):
                
                # Se o cluster da amostra A é zero ( significa que ela está sozinha em um cluster)
                if(clustersJain[vetorOrganizado[i,1].astype(int)] == 0):
                    # A amostra A recebe o cluster da amostra B que ela tem a menor distancia
                    clustersJain[vetorOrganizado[i,1].astype(int)] = clustersJain[vetorOrganizado[i,2].astype(int)]
               # Se o cluster da amostra A não é zero (ela pertence a um cluster com mais amostras)
               # Todas as amostras que estão no cluster com ela, vão receber o cluster da amostra B que tem a menor distancia
                else:
                    clustersJain[np.argwhere(clustersJain==clustersJain[vetorOrganizado[i,1].astype(int)])] = clustersJain[vetorOrganizado[i,2].astype(int)]              
                
                # Iguala zero na matriz distancia, para que elas não sejam mais computadas
                distanciaMatriz[vetorOrganizado[i,1].astype(int),vetorOrganizado[i,2].astype(int)] = 0
                distanciaMatriz[vetorOrganizado[i,2].astype(int),vetorOrganizado[i,1].astype(int)] = 0 
            # Caso a amostra B nao tem um cluster
            else: 
                # As duas amostras recebem o mesmo cluster
                clusterNumero = len(np.unique(clustersJain))
                clustersJain[vetorOrganizado[i,1].astype(int)] = clusterNumero
                clustersJain[vetorOrganizado[i,2].astype(int)] = clusterNumero
                
                # Iguala zero na matriz distancia, para que elas não sejam mais computadas
                distanciaMatriz[vetorOrganizado[i,1].astype(int),vetorOrganizado[i,2].astype(int)] = 0
                distanciaMatriz[vetorOrganizado[i,2].astype(int),vetorOrganizado[i,1].astype(int)] = 0 
        
        if(First):
            # Se for a primeira vez, as duas amostras recebem o cluster 1
            clustersJain[vetorOrganizado[i,1].astype(int)] = 1
            clustersJain[vetorOrganizado[i,2].astype(int)] = 1
            
            # Iguala zero na matriz distancia, para que elas não sejam mais computadas
            distanciaMatriz[vetorOrganizado[i,1].astype(int),vetorOrganizado[i,2].astype(int)] = 0
            distanciaMatriz[vetorOrganizado[i,2].astype(int),vetorOrganizado[i,1].astype(int)] = 0 

            
            First = False
    # Criterio de parada, quando só tiverem 2 clustersJain, sai do whule
    if(len(np.unique(clustersJain)) == 2):
        print("parou")
        breaki = True
        break

# transformar numa sequencia seguida de clustersJain ( pois os clustersJain tem numero aleatorio)
listaclustersJainOrganizado = np.zeros(len(clustersJain))
for i in range(1,len(np.unique(clustersJain))+1):
    listaclustersJainOrganizado[clustersJain == np.unique(clustersJain)[i-1]] = i




plt.figure(0)
plt.plot(data_set[count_originais_1,0].flatten(),data_set[count_originais_1,1].flatten(),'ro',label='C1')
plt.plot(data_set[count_originais_2,0].flatten(),data_set[count_originais_2,1].flatten(),'bo',label='C2')
plt.xlabel('Atributo 1')
plt.ylabel('Atributo 2')
plt.title('Base de dados original (jain.txt) ')
plt.savefig('jain_original.eps', format='eps',dpi=300 )

plt.legend(loc='best')
plt.figure(1)
plt.plot(data_set[count_label_1_old,0].flatten(),data_set[count_label_1_old,1].flatten(),'ro',label='C1')
plt.plot(data_set[count_label_2_old,0].flatten(),data_set[count_label_2_old,1].flatten(),'bo',label='C2')
plt.xlabel('Atributo 1')
plt.ylabel('Atributo 2')
plt.title('Classificação k-means (jain.txt) ')
plt.legend(loc='best')
plt.savefig('jain_kmeans.eps', format='eps',dpi=300 )

#Retoma os labels e cria uma matriz para plot
dicio = {1.0:"k",2.0:"r",3.0:"b",4.0:"g",5.0:"k",6.0:"m",7.0:"y",8.0:"darkblue"}
plt.figure(2)
plt.title("Classificação hierarquica (jain.txt) ")
plt.xlabel('Primeiro Atributo')
plt.ylabel('Segundo Atributo')
for i in range(0,len(Y[:,0])):
    plt.scatter(Y[i,0] , Y[i,1], c = dicio[listaclustersJainOrganizado[i]+1])
plt.savefig('jain_hierarquico.eps', format='eps',dpi=300 )
##print(label_vector) #k-means
##print(listaclustersJainOrganizado) #hierarquico
##print(labels_originais)


#print(labels_originais) #original
#print(label_vector) #k-means
#print(listaclustersOrganizado)#hierarquico 

index_1_O=np.array(np.where(labels_originais ==1)).flatten()
index_2_O=np.array(np.where(labels_originais ==2)).flatten()

print("--acuracia para k-means: ----------------------")
n = len(index_1_O) 
value,times = mostFrequent(label_vector[index_1_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 1: {:.2f}%".format(100*(times/n)))
n = len(index_2_O) 
value,times = mostFrequent(label_vector[index_2_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 2: {:.2f}%".format(100*(times/n)))
print("-----------------------------------------------")
print("--acuracia para hierarquico: ------------------")
n = len(index_1_O) 
value,times = mostFrequent(listaclustersJainOrganizado[index_1_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 1: {:.2f}%".format(100*(times/n)))
n = len(index_2_O) 
value,times = mostFrequent(listaclustersJainOrganizado[index_2_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 2: {:.2f}%".format(100*(times/n)))


            
            
            



