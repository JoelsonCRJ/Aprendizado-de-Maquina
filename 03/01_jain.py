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


def distancia():
    

data_set = pd.read_csv('jain.txt', sep="\t", header=None)
data_set=np.array(data_set)
data_set=data_set[:,0:2]

#separando em dois grupos
c_1,c_2=split_in_two(data_set)



