import numpy as np
import pandas as pd
import time


# Base de dados iris
dados = pd.read_csv('iris.data', sep=",", header=None)
dados =dados.iloc[:,:].values

for vez in range(0,4):
    print("\n"+str(vez+1)+" ªvez")
    np.random.shuffle(dados)
    ################################### ENTRADA ###################################
    entradas = dados[:,0:4]
    
    normalizacao = np.zeros((entradas.shape[0],entradas.shape[1]))
    
    # Normalização da entrada
    for j in range(0,len(entradas[0])):
        
        # media das colunas
        minimo = np.min(entradas,0)
        maximo = np.max(entradas,0)
        #maximo = 1.0
        #minimo = 0.0
        for i in range(0,len(entradas)):
            normalizacao[i,j] = (entradas[i,j] - minimo[j])/(maximo[j]-minimo[j]) #Media zero
    
    # Adicionar uma coluna de 1's para o bias
    X0 = np.ones((normalizacao.shape[0],1)) 
    X = np.hstack((X0,normalizacao))
    
    # Treino e validacao
    XTreino = X[0:74,:]
    XValidacao = X[74:113,:]
    
    # Treino e teste
    XTreino__ = X[0:113,:]
    XTeste = X[113::,:]
    
    
    #################################### ROTULOS #################################
    rotulosAlfabeto =  dados[:,4:]
    
    
    # Saídas Desejadas transformadas para numero
    dicionario = {'Iris-setosa': 0,'Iris-versicolor':1, 'Iris-virginica': 2}
    
    Yd = np.zeros((len(dicionario),entradas.shape[0]))
    rotulos =  np.zeros(len(entradas))
    
    # Saídas Desejadas transformadas para numero
    for i in range(0,len(rotulosAlfabeto)):
        rotulos[i] = dicionario[rotulosAlfabeto[i][0]]
        if(rotulos[i] == 0):
            Yd[:,i] = np.transpose(np.array([1,0,0]))
        if(rotulos[i] == 1):
            Yd[:,i] = np.transpose(np.array([0,1,0]))
        if(rotulos[i] == 2):
            Yd[:,i] = np.transpose(np.array([0,0,1]))
    
    
    YdTreino = Yd[:,0:74]
    YdValidacao = Yd[:,74:113]
    
    # Treino e teste
    YdTreino__ = Yd[:,0:113]
    YdTeste = Yd[:,113::]
    
    ######################## PARAMETROS ##########################################
    # numero de neuronios na camada oculta
    
    ocultaNeuronios = 10
    entradaNeuronios = X.shape[1]
    saidaNeuronios = Yd.shape[0]
    
    # Criar pesos aleatorios
    # A primeira coluna é do neuronio 1 (bias), a segunda coluna do neuronio 2
    WEntradaOculta = np.random.rand(ocultaNeuronios+1, entradaNeuronios) 
    
    WOcultaSaida = np.random.rand(saidaNeuronios,ocultaNeuronios+1)
    
    # Definir epocas, erro e aprendizagem
    epoca = 0
    erroAtual = 1
    aprendizagem = 0.3
    
    ###################### TREINO E VALIDACAO ####################################
    
    def nonlin(x,deriv=False):
    	if(deriv==True):
    	    return x*(1-x)
    
    	return 1/(1+np.exp(-x))
    
    yVetorCalculado =np.zeros((YdTreino.shape[0],YdTreino.shape[1]))
    
    while(epoca < 100 and erroAtual>0.001):
        
        startTime = time.time()
        erroAtual = 0
        
        for i in range(0,XTreino.shape[0]):
            
            # Foward 
            #
            mult = np.dot(WEntradaOculta,XTreino[i,:])
            # Funcao de ativacao tang hiperbolica
            saidaCamadaOculta = nonlin(mult)
            #Adicionar uma linha de uns
            #saidaCamadaOculta = np.append([1],saidaCamadaOculta)
            mult2 = np.dot(WOcultaSaida,saidaCamadaOculta)
            saida = nonlin(mult2)
            
            for j in range(0,3):
                yVetorCalculado[j,i] = np.round(saida[j])
            # Calculo do erro
            erro = np.power(YdTreino[:,i]-np.transpose(saida),2)
            erroAtual = erroAtual + np.mean(erro)
            
            # Backward
            gradiente2 = (saida-YdTreino[:,i])*saida*(1-saida)
         
            # atualização do peso
            for basico in range(0,gradiente2.shape[0]):
                WOcultaSaida[basico,:] = WOcultaSaida[basico,:] - aprendizagem*gradiente2[basico]*saidaCamadaOculta
                
                
            soma = np.matmul(gradiente2,WOcultaSaida)
            
            # Atualização do peso
            for k in range(0,XTreino.shape[1]):
                WEntradaOculta[:,k] = WEntradaOculta[:,k] - aprendizagem*(saidaCamadaOculta*(1-saidaCamadaOculta))*soma*XTreino[i,k]
        
        epoca = epoca + 1 
        # Tirar a media do vetor de erro e depois dividir pelo numero de amostras
        erroAtual = erroAtual/XTreino.shape[0]
       
    
    acerto = 0
    erro = yVetorCalculado - YdTreino
    for i in range(0,yVetorCalculado.shape[1]):
        if(np.count_nonzero(erro[:,i])==0):
            acerto = acerto + 1
    print("Acuracia Treino : " + str(100*acerto/XTreino.shape[0])+"%")
    
    yVetorCalculado =np.zeros((YdValidacao.shape[0],YdValidacao.shape[1]))
    
    for i in range(0,XValidacao.shape[0]):
        
        # Foward 
        #   
        mult = np.dot(WEntradaOculta,XValidacao[i,:])
        # Funcao de ativacao tang hiperbolica
        saidaCamadaOculta = nonlin(mult)
        #Adicionar uma linha de uns
        #saidaCamadaOculta = np.append([1],saidaCamadaOculta)
        mult2 = np.dot(WOcultaSaida,saidaCamadaOculta)
        saida = nonlin(mult2)
        
        for j in range(0,3):
            yVetorCalculado[j,i] =np.round(saida[j])
    
    
    acerto = 0
    erro = yVetorCalculado - YdValidacao
    for i in range(0,yVetorCalculado.shape[1]):
        if(np.count_nonzero(erro[:,i])==0):
            acerto = acerto + 1
    print("Acuracia Validacao: " + str(100*acerto/XValidacao.shape[0])+"%")
    
    fim = time.time()
    print("Tempo de execuçao Treino e Validação:" +str(fim - startTime)) 
       
    ####################### Treino e Teste ####################################    
    
    # Criar pesos aleatorios
    # A primeira coluna é do neuronio 1 (bias), a segunda coluna do neuronio 2
    WEntradaOculta = np.random.rand(ocultaNeuronios+1, entradaNeuronios) 
    
    WOcultaSaida = np.random.rand(saidaNeuronios,ocultaNeuronios+1)
        
    yVetorCalculado =np.zeros((YdTreino__.shape[0],YdTreino__.shape[1]))
    
    
    epoca = 0
    
    while(epoca < 100 and erroAtual>0.001):
        
        startTime = time.time()
        erroAtual = 0
        
        for i in range(0,XTreino__.shape[0]):
            
            # Foward 
            #
            mult = np.dot(WEntradaOculta,XTreino__[i,:])
            # Funcao de ativacao tang hiperbolica
            saidaCamadaOculta = nonlin(mult)
            #Adicionar uma linha de uns
            #saidaCamadaOculta = np.append([1],saidaCamadaOculta)
            mult2 = np.dot(WOcultaSaida,saidaCamadaOculta)
            saida = nonlin(mult2)
            
            for j in range(0,3):
                yVetorCalculado[j,i] = np.round(saida[j])
            # Calculo do erro
            erro = np.power(YdTreino__[:,i]-np.transpose(saida),2)
            erroAtual = erroAtual + np.mean(erro)
            
            # Backward
            gradiente2 = (saida-YdTreino__[:,i])*saida*(1-saida)
         
            # atualização do peso
            for basico in range(0,gradiente2.shape[0]):
                WOcultaSaida[basico,:] = WOcultaSaida[basico,:] - aprendizagem*gradiente2[basico]*saidaCamadaOculta
                
                
            soma = np.matmul(gradiente2,WOcultaSaida)
            
            # Atualização do peso
            for k in range(0,XTreino__.shape[1]):
                WEntradaOculta[:,k] = WEntradaOculta[:,k] - aprendizagem*(saidaCamadaOculta*(1-saidaCamadaOculta))*soma*XTreino__[i,k]
        
        epoca = epoca + 1 
        # Tirar a media do vetor de erro e depois dividir pelo numero de amostras
        erroAtual = erroAtual/XTreino__.shape[0]
    
    acerto = 0
    erro = yVetorCalculado - YdTreino__
    for i in range(0,yVetorCalculado.shape[1]):
        if(np.count_nonzero(erro[:,i])==0):
            acerto = acerto + 1
    print("\nAcuracia 2º Treino: " + str(100*acerto/XTreino__.shape[0])+"%")
    
    
    yVetorCalculado =np.zeros((YdTeste.shape[0],YdTeste.shape[1]))
    for i in range(0,XTeste.shape[0]):
        
        # Foward 
        #
        
        mult = np.dot(WEntradaOculta,XTeste[i,:])
        # Funcao de ativacao tang hiperbolica
        saidaCamadaOculta = nonlin(mult)
        #Adicionar uma linha de uns
        #saidaCamadaOculta = np.append([1],saidaCamadaOculta)
        mult2 = np.dot(WOcultaSaida,saidaCamadaOculta)
        saida = nonlin(mult2)
        
        for j in range(0,3):
            yVetorCalculado[j,i] =np.round(saida[j])
    
    
    acerto = 0
    erro = yVetorCalculado - YdTeste
    for i in range(0,yVetorCalculado.shape[1]):
        if(np.count_nonzero(erro[:,i])==0):
            acerto = acerto + 1
    print("Acuracia Teste: " + str(100*acerto/XTeste.shape[0])+"%")
    
    fim = time.time()
    print("Tempo de execuçao Treino e Teste:" +str(fim - startTime))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
