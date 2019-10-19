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