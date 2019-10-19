import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def elimina_linhas(dados):

    indices = np.argwhere(data == '?')
    indices = indices[:,0]
    dados_new = np.zeros((dados.shape[0] - indices.shape[0], dados.shape[1]))
    linha = 0
    for i in range(dados.shape[0]):
        if not i in indices:
            dados_new[linha,:] = dados[i,:]
            linha = linha + 1
    return dados_new, indices
#regressao linear multipla
def regressao_mult(dados, coluna):
    t = dados[:,coluna-1]
    X = np.ones(dados.shape, dtype=float)
    X[:,1:]=dados[:,1:]
    X_trans = np.transpose(X)
    #X por X_trans (inversa)
    A = np.linalg.inv(np.matmul(X_trans,X))
    B = np.matmul(A,X_trans)
    C = np.matmul(B,t)
    
    return C
#calcula para saída desejada
def equacao(X, W):
    X_new = np.ones((X.shape))
    X_new[:,1:]=X[:,1:]
    t = np.zeros(X.shape[0], dtype=float)
    t = np.sum(X_new*W, axis=1)
    return t

#RMSE mult
def RMSE_mult(vet_real, vet_calc):
    A = np.sum(np.power((vet_real[:,0]-vet_calc), 2))
    return np.sqrt(A/vet_real.shape[0])

#Teste de relacionamento entre as entradas (x) e a saída (t)

def F_RSS(data,WW):
    F_teste = []
    N = data.shape[0]
    n = WW.shape[0]-1
    q = 6
    for i in range(WW.shape[0]):
        if i==0:
            #calculando o RSS
            t = equacao(data,WW)
            RSS = np.sum(np.power((data[:,0]-t),2))
        else:
            w = np.copy(WW)
            w[i]=0
            t = equacao(data,w)
            RSS0 = np.sum(np.power((data[:,0]-t),2))
            FRSS0 = (((RSS0-RSS)/(n-q))/((RSS)/(N-n-1)))
            F_teste.append(FRSS0)
    return F_teste

#teste de hipotese
def hipo_F(lista_f,F):
    menores = []
    for i in range(len(lista_f)):
        if lista_f[i] < F:
            menores.append(i+1)
            print("O atributo x" + str(i+1) + " pode ser desconsiderado")
    return menores

def mod_W(W,delet):
    W_new = np.copy(W)
    for i in delet:
        W_new[i]=0
    return W_new
#----------------------------------------------------
dados = pd.read_csv('auto-mpg.csv', sep=",", header=None)
data = dados.values

data = data[1:,0:-1]# eliminando a ultima coluna 
data_new, indices = elimina_linhas(data)
treino = data_new[0:150,:]
teste = data_new[150:,:]

W = regressao_mult(treino,1)
#testando o modelo no restante dos dados
vetor_t = equacao(teste,W)

#Calculando o RMSE do modelo
rmse = RMSE_mult(teste,vetor_t)
print(rmse)


# questao b 

vetor_F = F_RSS(treino,W)
deletados = hipo_F(vetor_F, 3.908)

#Desconsiderando as variáveis testadas
W_new = mod_W(W,deletados)
#testando o modelo no restante dos dados
vetor_t = equacao(teste,W_new)
#Calculando o RMSE do modelo
rmse = RMSE_mult(teste,vetor_t)
print(rmse)