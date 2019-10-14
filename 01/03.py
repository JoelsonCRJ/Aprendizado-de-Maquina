import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations 

#-------functions

def RMSE (real_data,real_x,calculated_data,calculated_t):
    quadratic_error = 0
    for i in range (0,real_x.size):
        for j in range(0,calculated_t.size):
            if(real_x[i]==calculated_t[j]):
                quadratic_error = quadratic_error + np.power((real_data[i]-calculated_data[j]),2)
    RMSE = np.sqrt((1/real_data.size)*quadratic_error)
    return RMSE

def RSS(real_data,real_x,calculated_data,calculated_t):
    quadratic_error = 0
    for i in range (0,real_x.size):
        for j in range(0,calculated_t.size):
            if(real_x[i]==calculated_t[j]):
                quadratic_error = quadratic_error + np.power((real_data[i]-calculated_data[j]),2)
    return quadratic_error

def get_tal(a1,a2,combinations):
    positivos = 0
    negativos = 0
    matrix = 0
    for i in range(combinations.shape[0]):
        matrix=(a1[combinations[i][0]]-a1[combinations[i][1]])*(a2[combinations[i][0]]-a2[combinations[i][1]])
        if(matrix>0):
            positivos = positivos +1
        else:
            negativos=negativos+1
    print(positivos)
    print(negativos)
    
    N=(a1.size*(a1.size-1))/2
    print(N)
    tal = (positivos-negativos)/(N)
    return tal

#-----------------------




data = pd.read_csv('Runner_num.txt',sep='\t',header = None)
data = np.array(data)


x=data[:,0]
y=data[:,1]
#plt.figure(0)
#plt.plot(x,y,'o')
#plt.savefig('03a_1.svg', format='svg',dpi=300 )

x_mean=np.mean(x,dtype=np.float32)

y_mean=np.mean(y,dtype=np.float32)

x_y_mean=np.multiply(x,y)
x_y_mean=np.sum(x_y_mean)/x.shape[0]
x_2_mean=np.mean(np.power(x,2))
x_mean_2=np.power(x_mean,2)
w1=(x_y_mean-(x_mean*y_mean))/(x_2_mean-x_mean_2)

w0=y_mean-w1*x_mean
#print(w1)
t=np.arange(x[0],x[-1]+1)
f=np.zeros((1,t.size))
        
f=w0+w1*t
#plt.figure(1)
#plt.plot(t,f,'r',x,y,'o')
#plt.savefig('03a_2.svg', format='svg',dpi=300 )




RMSE = RMSE(y,x,f,t)
print('-----')
print('Erro RMSE: {0:.2f}%'.format(RMSE*100))
print('-----')
#------ letrab------
f_2020=w0+w1*(2020)
print('O valor do resultado para o ano de 2020 é de: {0:.2f} m/s'.format(f_2020))
print('-----')
#-------letra c ------

combinations = np.array(list(combinations(np.arange(0,29),2)))
print(combinations.shape[0])
tal=get_tal(x,y,combinations)
tal=abs(tal)
print(tal)

z_5p = 1.96
z_1p = 2.33




            


