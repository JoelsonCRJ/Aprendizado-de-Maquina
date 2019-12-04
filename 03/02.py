"""
Created on Mon Jun 11 15:10:54 2018

@author: Fabiana Santos

Lista 3

Exercício 2

"""

import numpy as np
import itertools


# Importando a base de dados
dados = np.loadtxt('transacoes.txt')

# 21 itens (I) e 6 transaçoes (T)

# Dados Teste Slide

testeDoSlide= np.array([[1,	0,	1,	0,	1,	0,	0,	0,	0,	0],
                        [1,	1,	1,	0,	1,	0,	1,	0,	0,	0],
                        [1,	1,	0,	1,	0,	0,	0,	0,	1,	0],
                        [1,	1,	1,	0,	1,	0,	0,	0,	1,	0],
                        [1,	0,	1,	1,	1,	1,	0,	1,	0,	0],
                        [0,	1,	0,	0,	0,	0,	0,	1,	1,	0]])


########################## Pré-Processamento dos Dados ########################
# Calculo do suporte mínimo (frequencia minima)
porcentagem = 0.5
frequenciaMin = np.round(porcentagem*dados.shape[0])

# Lista de transacoes unicas
transacoes = []

# Substituindo a matriz de dados binaria, por uma matriz binaria com itens 
for i in range(0,dados.shape[0]):
    for j in range(0,dados.shape[1]):
        if(dados[i,j] == 1):
            dados[i,j] = dados[i,j]*j +1
    
    # Para cada transação, somente o numero das transacoes vao compor a lista
    unicos = np.unique(dados[i,:])
    transacoes.append(np.delete(unicos,0)) 
     
# Todos itens possíveis unicos dos dados (1,10)
itens = np.delete(np.unique(dados),0)   
listaDeSubConjuntos = []

################################# FUNCOES ####################################
# Função para verificar frequencia (quantidade) de dados

def Calculo_Frequencia(transacoes,listaDeSubconjuntos,frequenciaCombinacoes):
    
    for i in range(0,len(listaDeSubconjuntos)):
        # para cada combinacao dentro da lista de subconjunto
        combinacaoEscolhida = listaDeSubConjuntos[i]
        frequencia = 0
        # Para cada uma das transacoes 
        for transacao in transacoes:
            # flag para quando as combinações são tuplas
            flag = True
            for item in combinacaoEscolhida:
                # Se o item não está não transação, então não entra na conta da frequencia
                if(item not in transacao):
                    flag = False        
            if(flag):
                frequencia = frequencia + 1
            frequenciaCombinacoes[i]= frequencia
    return frequenciaCombinacoes,combinacaoEscolhida,item,transacao

# Funcao para retornar as possíveis regras
def Regras(frequenciaCombinacoes,listaDeSubConjuntos):
    
    for i in range(0,len(frequenciaCombinacoes)):
        if(frequenciaCombinacoes[i]<frequenciaMin):
            frequenciaCombinacoes[i] = -1
        else:    
            listaSubconjuntosAprovados.append(listaDeSubConjuntos[i])
            frequenciaSubconjuntosAprovados.append(frequenciaCombinacoes[i])
            if(len(listaDeSubConjuntos[i])>1):
                regras.append(listaDeSubConjuntos[i])  
    
    return regras,frequenciaCombinacoes,frequenciaSubconjuntosAprovados

def Calculo_CombinacaoRegras(regras_2Comb,regras_3Comb):
    
    combinacao2_esq = []
    combinacao2_dir = []
    combinacao3_esq = []
    combinacao3_dir = []
    
     
    for j in range(0,len(regras_2Comb)):
        regras_2Comb_ = regras_2Comb[j]
        combinacao2_esq.append(regras_2Comb_[0])
        combinacao2_dir.append(regras_2Comb_[1])
              
        
    for j in range(0,len(regras_3Comb)):
        regras_3Comb_ = regras_3Comb[j]
        combinacao3_esq.append(regras_3Comb_[0:1])
        combinacao3_dir.append(regras_3Comb_[1:3])
        
    for j in range(0,len(regras_3Comb)):
        regras_3Comb_ = regras_3Comb[j]
        combinacao3_esq.append(regras_3Comb_[0:2])
        combinacao3_dir.append(regras_3Comb_[2:3])
            
    return combinacao2_esq, combinacao2_dir, combinacao3_esq, combinacao3_dir

def Calculo_frequencia_uniao(combinacao2_esq,combinacao2_dir,listaSubconjuntosAprovados,possiveisRegrasConcatenadas,frequenciaSubconjuntosAprovados):
    
    frequenciaUniao = []          
    for i in range(0,len(combinacao2_esq)):     
        possiveisRegrasConcatenadas_ = possiveisRegrasConcatenadas[i]
        for j in range(0,len(listaSubconjuntosAprovados)):
            if(listaSubconjuntosAprovados[j]==possiveisRegrasConcatenadas_): 
                frequenciaUniao.append(frequenciaSubconjuntosAprovados[j])
    
    return frequenciaUniao
##############################################################################

   
# Inicialização dos vetores de frequencia(quantidade), subconjuntos que superam quantidade
# e regras
listaSubconjuntosAprovados = []
regrasCombinacoes = []  
regras = []
frequenciaSubconjuntosAprovados = []
# Calculo da frequencia de cada combinação na lista de transações
for i in range(1,len(itens)+1):
    
    listaDeSubConjuntos = []
    
    # criterio de parada
    if(len(itens)<i):
        break;
        
    # Combinacoes possíveis para cada item

    listaDeCombinacoes = list(itertools.permutations(itens, r=i))
    for combinacao in listaDeCombinacoes:
        listaDeSubConjuntos.append(list(combinacao))
        
    del combinacao,listaDeCombinacoes
    
    # vetor das frequencias de cada combinação
    frequenciaCombinacoes = np.zeros(len(listaDeSubConjuntos))
    
    frequenciaCombinacoes,combinacaoEscolhida,item,transacao = Calculo_Frequencia(transacoes,listaDeSubConjuntos,frequenciaCombinacoes)
    
    # Limpar variaveis
    del combinacaoEscolhida,transacao
    del item
    flag = True
    
    # Calculo das regras possíveis
    regras,frequenciaCombinacoes,frequenciaSubconjuntosAprovados = Regras(frequenciaCombinacoes,listaDeSubConjuntos)
    
    # Transformar os itens de subconjunto (estão em um array dentro de lista)
    # em lista
    itens = []
    for subconjunto in listaSubconjuntosAprovados:
        for i in range(0,len(subconjunto)):
            itens.append(subconjunto[i])
    
    # itens unicos para refazer as combinações
    itens = list(np.unique(np.array(itens)))
    

    
############################## VERIFICAR REGRAS ###############################    
# Função para verificar se as regras são validas pela frequencia

# Regra para 2
regras_2Comb = []
regras_3Comb = []
for i in range(0,len(regras)):
    if(len(regras[i])==2):
        regras_2Comb.append(regras[i])
    
    if(len(regras[i])==3):
        regras_3Comb.append(regras[i])

combinacao2_esq, combinacao2_dir, combinacao3_esq, combinacao3_dir = Calculo_CombinacaoRegras(regras_2Comb,regras_3Comb)        
    
# Calculo frequencia das combinacoes

# transformando os numeros em lista
for i in range(0,len(combinacao2_esq)):
    combinacao2_esq[i] = [combinacao2_esq[i]]
    combinacao2_dir[i] = [combinacao2_dir[i]]

# concatenando as possíveis regras 2 e 3
for i in range(0,len(combinacao3_esq)):
    combinacao2_esq.append(combinacao3_esq[i])
    combinacao2_dir.append(combinacao3_dir[i])
  
frequenciaUnico = []
  

# frequencia do lado esquerdo 2 combinacoes
 
for i in range(0,len(combinacao2_esq)):
    
    for j in range(0,len(listaSubconjuntosAprovados)):
        if(listaSubconjuntosAprovados[j]==combinacao2_esq[i]): 
            frequenciaUnico.append(frequenciaSubconjuntosAprovados[j])   

frequenciaUnico_ = np.array(frequenciaUnico)
    
# frequencia uniao dos lados
possiveisRegrasConcatenadas = []

# Lista concatenada das possíveis regras
for i in range(0,len(combinacao2_esq)):     
    possiveisRegrasConcatenadas.append(list(np.concatenate((combinacao2_esq[i],combinacao2_dir[i]))))
           
frequenciaUniao = Calculo_frequencia_uniao(combinacao2_esq,combinacao2_dir,listaSubconjuntosAprovados,possiveisRegrasConcatenadas,frequenciaSubconjuntosAprovados)
frequenciaUniao_ = np.array(frequenciaUniao)

confianca = frequenciaUniao_/frequenciaUnico_
# AChando as regras pela minima confiancia    
    
confiancia_Minima = 0.9


print("Regras:")
for i in range(0,len(combinacao2_dir)):
    if((confianca[i]>confiancia_Minima)):
        print( str(combinacao2_esq[i]) + " => " + str(combinacao2_dir[i]))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    