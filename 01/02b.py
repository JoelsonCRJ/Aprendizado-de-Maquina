import pandas as pd
import numpy as np

def get_x_trainning(array):
    X=np.zeros((array.shape[0],array.shape[1]),dtype = np.float32)
    for i in range(0,array.shape[0]):
        for j in range(0, array.shape[1]):
            X[i][j]=(array[i][j] - np.mean(array[:,j],dtype=np.float32))/np.std(array[:,j],dtype=np.float32)
        
    return X

def get_x_test(array_test,array_trainning):
    X=np.zeros((array_test.shape[0],array_test.shape[1]),dtype = np.float32)
    for i in range(0,array_test.shape[0]):
        for j in range(0, array_test.shape[1]):
            X[i][j]=(array_test[i][j] - np.mean(array_trainning[:,j],dtype=np.float32))/np.std(array_trainning[:,j],dtype=np.float32)
        
    return X


def reduce_percent(array,stop_condititon):
    total=0
    full=np.sum(array)
    for i in range(array.size-1,1,-1):
        total=total+(total+array[i])/full
        #print(total)
        if(total >= stop_condititon):
            return (total,abs(i-array.size))

def NN(trainning_array,test_array,labels_column):
    labels=[]
    for i in range(0,test_array.shape[0]):
        distances=np.zeros((len(trainning_array)))
        for z in range(0,trainning_array.shape[0]):
            distances[z]=np.sqrt(np.sum(np.power(np.subtract(test_array[i,0:test_array.shape[1]],trainning_array[z,1:trainning_array.shape[1]]),2)))
        #min[0] = index of min value and min[1] is the min value
        #print(distances)
        distances = list(distances)
        min_index = distances.index(min(distances))

        labels.append(trainning_array[min_index,labels_column])  
    return np.array(labels)

def accuracy(labels,prediction):
    count=0
    for i in range(0,labels.shape[0]):
        if(labels[i]==prediction[i]):
            count=count+1
    return (count/len(labels))*100

data = pd.read_csv('wdbc.txt',sep=',',header = None)
data = data.drop(data.columns[0], axis=1)

data = np.array(data)
trainning_data = data[0:300,:]
test_data = data[300:data.shape[0],:]

X_til = get_x_trainning(trainning_data[:,2:trainning_data.shape[1]]) # atributo 1 ate o final 
X_til_transposed = X_til.transpose()
N=300 # tirando dois primeiros atributos pois são irrelevantes
C=(1/(N-1))*(X_til_transposed.dot(X_til))
L=np.linalg.eigh(C,UPLO = 'U')
#L[0] - vetor de autovalores em ordem crescente
#L[1] - matriz com os autovetores relacionados aos autovalores
autovalores = L[0]
autovetores = L[1]
# print(autovalores)
# print(np.sum(autovalores))
percentagem,componentes = reduce_percent(autovalores,0.9)

# print(percentagem)
#print(componentes)
print("foram selecionadas {} componentes principais".format(componentes)) 
autovetores_selecionados = autovetores[:,29-componentes:29]
#print(autovetores_selecionados)

trainning_PCA =X_til.dot(autovetores_selecionados)

#print(trainning_PCA)

#trainning_PCA=np.append(trainning_data[:,0].T,trainning_PCA,axis=1)
#trainning_PCA = np.insert(trainning_PCA, 0, values=trainning_data[:,0], axis=1)

dataset = pd.DataFrame({'A': trainning_data[:, 0], 'B': trainning_PCA[:, 0],'C': trainning_PCA[:, 1],'D': trainning_PCA[:, 2],'E': trainning_PCA[:, 3],'F': trainning_PCA[:, 4]})

trainning_PCA= np.array(dataset)
#print(trainning_PCA.shape)
#print(test_data.shape)
labels_vector=test_data[:,0]

#aplicando PCA nos dados de teste
X_til_test = get_x_test(test_data[:,2:test_data.shape[1]],trainning_data[:,2:trainning_data.shape[1]])
test_PCA =X_til_test.dot(autovetores_selecionados)

prediction_vector_NN=NN(trainning_PCA,test_PCA,0)
accuracy_NN=accuracy(labels_vector,prediction_vector_NN)
print("Accuracy using NN: {0:.2f}%".format( accuracy_NN))