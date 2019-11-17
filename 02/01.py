#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math



#funçoes
#funcao letra a P(x1 =med) e P(x2 = low)
def prob_a(attribute, value, data):
    ind = attribute-1
    prob = len(data[data[:,ind]==value])/data[:,ind].shape[0]
    return prob

#funcao para calcular probabilidade de um atributo dado que
#outro valor ocorra em outro atributo 
def prob_dadoq(attribute_1, attribute_2, value_1, value_2, data):
    ind_1 = attribute_1-1
    ind_2 = attribute_2-1
    dado_x = dados[dados[:,ind_2]==value_2]
    prob = prob_a(attribute_1, value_1, dado_x)
    return prob



def prob_atr2(attribute_1, attribute_2, attribute_p, value_1, value_2, value_p, dados):
    ind1 = attribute_1-1
    ind2 = attribute_2-1
    d = dados[dados[:,ind1]==value_1]
    d = d[d[:,ind2]==value_2]    
    prob = prob_a(attribute_p, value_p, d)
    return prob


def prob_atr3(attribute_1, attribute_2, attribute_3, value_1, value_2, value_3, dados):
    ind1 = attribute_1-1
    ind2 = attribute_2-1
    ind3 = attribute_3-1
    d = dados[dados[:,ind3]==value_3]
    d1 = d[d[:,ind2]==value_2]
    d2 = d1[d1[:,ind1]==value_1]
    prob = len(d2)/len(d)
    return prob

#------------------------------------------------------------------------
data = pd.read_csv('car.data', sep=",", header=None)


dados=data.values
data=dados[:,0:-1]
label = data[:,-1]


#letra a

pa_1=prob_a(1,'med',data)
print("P(X1 = med) = {} %".format(pa_1*100))

pa_2=prob_a(2,'low',data)
print("P(X2 = Low) = {} %".format(pa_2*100))

#letra b

#P(x6=high|x3=2)
pb_1 = prob_dadoq(6, 3, 'high', '2', data)
print("P(x6=high|x3=2) = {0:.2f} %".format(pb_1*100))

#P(x2=low|x4=4)
pb_2 = prob_dadoq(2, 4, 'low', '4', data)
print("P(x2=low|x4=4) = {0:.2f} %".format(pb_2*100))

#letra c 

#P(x1=low|x2=low,X5=small)
pc_1 = prob_atr2(2, 5, 1, 'low', 'small', 'low', data)
print("P(x1=low|x2=low,X5=small) = {0:.2f} %".format(pc_1*100))

#P(x4=4|x1=med,X3=2)
pc_2 = prob_atr2(1, 3, 4, 'med', '2', '4', data)
print("P(x4=4|x1=med,X3=2) = {0:.2f} %".format(pc_2*100))

#letra D

#P(x2= vhigh,X3=2|X4=2)
pd_1 = prob_atr3(2, 3, 4, 'vhigh', '2', '2', data)
print("P(x2= vhigh,X3=2|X4=2) = {0:.2f} %".format(pd_1*100))

#P(x3=4,x5=med|x1=med)
pd_2 = prob_atr3(3, 5, 1, '4', 'med', 'med', data)
print("P(x2= vhigh,X3=2|X4=2) = {0:.2f} %".format(pd_2*100))
