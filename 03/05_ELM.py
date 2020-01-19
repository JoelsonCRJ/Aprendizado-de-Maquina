import numpy as np
import pandas as pd
import time

################################ ENTRADA DE DADOS ############################
# Base de dados iris
dados = pd.read_csv('iris.data', sep=",", header=None)
dados = dados.iloc[:,:].values

# Dicionario para transformar as saídas de string para número
dicionario = {'Iris-setosa': 0,'Iris-versicolor':1, 'Iris-virginica': 2}

########################## FUNCOES ###########################################
# Função de ativação sigmoide

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

########################### ELM ##############################################
  
######### PARAMETROS ################
# Numero de neuronios camada escondida
neuronioCamadaOculta = 3

######## REDE ######################
# Rodas o algoritmo 4x para comparar os resultados
for vezes in range(4):
    
    # Computar o tempo de excecução
    startTime = time.time()
    
    # Da um shuffle nos dados
    np.random.shuffle(dados)
    
    # Saídas Desejadas transformadas para numero
    
    rotulosAlfabeto = dados[:,-1]
    rotulos = np.zeros((len(rotulosAlfabeto)))
    
    for i in range(0,dados.shape[0]):
        rotulos[i] = dicionario[rotulosAlfabeto[i]]
        
    rotulos = np.reshape(rotulos,(1,len(rotulos)))

    # Divide em partes para treino e validação
    entradas = np.array(dados[:,0:-1],dtype=float)
    
    treino = entradas[0:74,:]
    valida = entradas[74:112,:]
    rotuloTreino = rotulos[:,0:74]
    rotuloValida = rotulos[:,74:112]

    # Divide em partes para treino e teste
    treino_ = entradas[0:112,:]
    rotuloTreino_ = rotulos[:,0:112]
    teste = entradas[112:,:]
    rotuloTeste = rotulos[:,112:]
    
    ########################### TREINO E VALIDACAO ###########################
    # Primeira e segunda parte de treino e 1 de validaçãp
    # Gerar pesos e bias aleatorios da camada oculta

    W = np.random.rand(treino.shape[1], neuronioCamadaOculta) 
    b = np.array([np.abs(np.random.randn(neuronioCamadaOculta))])
    
    # Vetor de uns
    I = np.ones(len(treino))
    I = np.transpose([I])
    
    # Transpor o vetor de rotulos
    T = np.copy(rotuloTreino)
    T = np.transpose(T)
    
    # TempH = somatario de cada neuronio
    tempH = np.matmul(treino,W) + np.matmul(I,b)
    
    # Matriz função de ativação
    H = sigmoid(tempH)
    
    # Solução minimos quadrados
    Beta = np.matmul((np.linalg.inv(np.matmul(np.transpose(H),H))),np.matmul(np.transpose(H),T))
    
    # Classificando amostras 
    T = np.matmul(H,Beta)

###################### CLASSIFICACAO #########################################
    # Classificar a parte separada para validação
    classificados = np.zeros(len(valida))
    
    for i in range(0,len(valida)):
        
        tempHClassificacao = np.matmul(valida[i],W) + b
        
        H = sigmoid(tempHClassificacao)
        
        # Classificar amostra de validação
        T = np.matmul(H,Beta)
        classificados[i] = abs((np.round(T[0])))  

###################### CALCULO ACURACIA #######################################
    erros = 0
    for i in range(rotuloValida.shape[0]):
        if classificados[i] != rotuloValida[0][i]:
            erros = erros + 1
    
    print("\nELM")
    print("Treino e validação: " + str(vezes+1) +" vez")
    print("Acuracia: " + str(((classificados.shape[0] - erros)/classificados.shape[0])*100))
    fim = time.time()
    print("Tempo de execuçao :" +str(fim - startTime))
    
    
    ######################## TREINO E TESTE ################################
    
    startTime = time.time()
    
    # Tres partes para treino e uma para teste
    # Gerar pesos e bias aleatorios da camada oculta
    W = np.random.randn(treino_.shape[1],neuronioCamadaOculta)/3
    b = np.array([np.abs(np.random.randn(neuronioCamadaOculta)/3)])
    
    # Vetor de uns
    I = np.ones(len(treino_))
    I = np.transpose([I])
    
    # Transpor o vetor de rótulos
    T = np.copy(rotuloTreino_)
    T = np.transpose(T)
    
    # TempH = somatario de cada neuronio
    tempH = np.matmul(treino_,W) + np.matmul(I,b)
    
    # Matriz da função de ativação
    H = sigmoid(tempH)
    
    # Solução minimos quadrados
    Beta = np.matmul((np.linalg.inv(np.matmul(np.transpose(H),H))),np.matmul(np.transpose(H),T))
    
    # Classificando amostras
    T = np.matmul(H,Beta)

###################### CLASSIFICACAO #########################################
    # lassificar a parte separada para teste
    classificados = np.zeros(len(teste))
    
    for i in range(len(teste)):
        tempHClassificacao = np.matmul(teste[i],W) + b
            
        H = sigmoid(tempHClassificacao)
        
        # Classificar amostra de teste
        T = np.matmul(H,Beta)
        classificados[i] = abs((np.round(T[0])))  


###################### CALCULO ACURACIA #######################################
    erros = 0
    for i in range(rotuloTeste.shape[0]):
        if classificados[i] != rotuloTeste[0][i]:
            erros = erros + 1
    
    
    print("\nTreino e Teste: " + str(vezes+1) +" vez")
    print("Acuracia: " + str(((classificados.shape[0] - erros)/classificados.shape[0])*100))
    fim = time.time()
    print("Tempo de execuçao :" +str(fim - startTime))
   
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        