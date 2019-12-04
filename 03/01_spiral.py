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


#funcoes para hierarquico
    
def distanciaEuclidiana(X):
    
    distanciaMatriz = np.zeros((X.shape[0],X.shape[0]))
    
    for j in range(0,X.shape[0]):
        for i in range(j+1,X.shape[0]):
            subtracaoVetor = np.subtract(X[j,:],X[i,:])
            elevQuadradoVetor = np.power(subtracaoVetor,2)
            somaVetor = np.sum(elevQuadradoVetor)
            distanciaMatriz[j,i] = np.sqrt(somaVetor)
            distanciaMatriz[i,j] = np.sqrt(somaVetor)
        
    return distanciaMatriz

def minimos(distanciaMatriz):
# Com a matriz de distância, achar os valores minimos para se construir os clusters
    for i in range(0,X.shape[0]):
        
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
#print(label_vector)


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
#    print(np.array_equal(label_vector,old_label_vector))
    if(np.array_equal(label_vector,old_label_vector)):
        count +=1
#        print(count)
        if(count ==3):
            flag=0
           # print(label_vector)
    else:
        flag=1
        count = 0 
        



# algoritmo hierarquico

X=data_set[:,0:2]
classes= labels_originais

# Vetor que conterá a distancia minima e os dois indices a qual essa distancia pertence
vetorDistIndMin = np.zeros((X.shape[0],3))
# Vetor que terá os clusters de cada indice
clusters = np.zeros(X.shape[0])
distanciaMatriz = distanciaEuclidiana(X)
First = True
breaki = False

# Ate entrar no criterio de parada
while(True):
    # função para achar a distancia minima e seus indices
    vetorDistIndMin = minimos(distanciaMatriz)
    # organizar o vetor começando pela menor distancia
    vetorOrganizado = vetorDistIndMin[vetorDistIndMin[:,0].argsort()]    
     
    
    for i in range(0,X.shape[0]):    
        
        # Caso não seja a primeira vez (na primeira vez os primeiros vão receber o mesmo cluster)
        if(not First):
            
            # para uma dada amostra A, checa se a amostraB  que tem a menor distancia com ela
            # ja tem um cluster ou nao.
            
            # Se B ja tem um cluster
            if(clusters[vetorOrganizado[i,2].astype(int)] != 0):
                
                # Se o cluster da amostra A é zero ( significa que ela está sozinha em um cluster)
                if(clusters[vetorOrganizado[i,1].astype(int)] == 0):
                    # A amostra A recebe o cluster da amostra B que ela tem a menor distancia
                    clusters[vetorOrganizado[i,1].astype(int)] = clusters[vetorOrganizado[i,2].astype(int)]
               # Se o cluster da amostra A não é zero (ela pertence a um cluster com mais amostras)
               # Todas as amostras que estão no cluster com ela, vão receber o cluster da amostra B que tem a menor distancia
                else:
                    clusters[np.argwhere(clusters==clusters[vetorOrganizado[i,1].astype(int)])] = clusters[vetorOrganizado[i,2].astype(int)]              
                
                # Iguala zero na matriz distancia, para que elas não sejam mais computadas
                distanciaMatriz[vetorOrganizado[i,1].astype(int),vetorOrganizado[i,2].astype(int)] = 0
                distanciaMatriz[vetorOrganizado[i,2].astype(int),vetorOrganizado[i,1].astype(int)] = 0 
            # Caso a amostra B nao tem um cluster
            else: 
                # As duas amostras recebem o mesmo cluster
                clusterNumero = len(np.unique(clusters))
                clusters[vetorOrganizado[i,1].astype(int)] = clusterNumero
                clusters[vetorOrganizado[i,2].astype(int)] = clusterNumero
                
                # Iguala zero na matriz distancia, para que elas não sejam mais computadas
                distanciaMatriz[vetorOrganizado[i,1].astype(int),vetorOrganizado[i,2].astype(int)] = 0
                distanciaMatriz[vetorOrganizado[i,2].astype(int),vetorOrganizado[i,1].astype(int)] = 0 
        
        if(First):
            # Se for a primeira vez, as duas amostras recebem o cluster 1
            clusters[vetorOrganizado[i,1].astype(int)] = 1
            clusters[vetorOrganizado[i,2].astype(int)] = 1
            
            # Iguala zero na matriz distancia, para que elas não sejam mais computadas
            distanciaMatriz[vetorOrganizado[i,1].astype(int),vetorOrganizado[i,2].astype(int)] = 0
            distanciaMatriz[vetorOrganizado[i,2].astype(int),vetorOrganizado[i,1].astype(int)] = 0 

            
            First = False
    # Criterio de parada, quando só tiverem 3 clusters, sai do whule
    if(len(np.unique(clusters)) == 3):
        print("parou")
        breaki = True
        break

# transformar numa sequencia seguida de clusters ( pois os clusters tem numero aleatorio)
listaclustersOrganizado = np.zeros(len(clusters))#
Labels_novo = np.arange(0,data_set.shape[0],1)

for i in range(1,len(np.unique(clusters))+1):
    listaclustersOrganizado[clusters == np.unique(clusters)[i-1]] = i 

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
plt.title('Classificação k-means (spiral.txt) ')
plt.legend(loc='best')

plt.figure(2)
plt.title("Classificação Hierarquica (spiral.txt)")
plt.xlabel('Primeiro Atributo')
plt.ylabel('Segundo Atributo')
##Retoma os labels e cria uma matriz para plot
dicio = {1.0:"k",2.0:"r",3.0:"b",4.0:"g",5.0:"k",6.0:"m",7.0:"y",8.0:"green"}

for i in range(0,len(X[:,0])):
    plt.scatter(X[i,0] , X[i,1], c = dicio[listaclustersOrganizado[i]+1])

plt.show()
#print(labels_originais) #original
#print(label_vector) #k-means
#print(listaclustersOrganizado)#hierarquico 

index_3_O=np.array(np.where(labels_originais ==3)).flatten()
index_1_O=np.array(np.where(labels_originais ==1)).flatten()
index_2_O=np.array(np.where(labels_originais ==2)).flatten()

print("--acuracia para k-means: ------------------")
n = len(index_3_O) 
value,times = mostFrequent(label_vector[index_3_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 1: {:.2f}%".format(100*(times/n)))
n = len(index_2_O) 
value,times = mostFrequent(label_vector[index_2_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 2: {:.2f}%".format(100*(times/n)))
n = len(index_1_O) 
value,times = mostFrequent(label_vector[index_1_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 3: {:.2f}%".format(100*(times/n)))
print("-------------------------------------------")
print("--acuracia para hierarquico: ------------------")
n = len(index_3_O) 
value,times = mostFrequent(listaclustersOrganizado[index_3_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 1: {:.2f}%".format(100*(times/n)))
n = len(index_2_O) 
value,times = mostFrequent(listaclustersOrganizado[index_2_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 2: {:.2f}%".format(100*(times/n)))
n = len(index_1_O) 
value,times = mostFrequent(listaclustersOrganizado[index_1_O], n) 
#print("{} {}".format(value,times))
print("acuracia para o cluster 3: {:.2f}%".format(100*(times/n)))