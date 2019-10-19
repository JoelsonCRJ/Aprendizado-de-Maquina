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
   
    N=(a1.size*(a1.size-1))/2

    tal = (positivos-negativos)/(N)
    return tal

def get_covariance(data):
    X_til=np.zeros((data.shape[0],data.shape[1]),dtype=np.float32)
    for i in range(0,data.shape[0]):
        for j in range(0,data.shape[1]):
            X_til[i][j]=data[i][j]-np.mean(data[:,j],dtype=np.float32) 
            
    C=(1/(data.shape[0]-1))*(X_til.transpose().dot(X_til))
    P=C[0][1]/(np.sqrt(C[0][0])*np.sqrt(C[1][1]))
    return P
#-----------------------




data = pd.read_csv('Runner_num.txt',sep='\t',header = None)
data = np.array(data)


x=data[:,0]
y=data[:,1]
plt.figure(0)
plt.plot(x,y,'o')
plt.xlabel('Ano')
plt.ylabel('Tempo (s)')
plt.savefig('03a_1.svg', format='svg',dpi=300 )

x_mean=np.mean(x,dtype=np.float32)

y_mean=np.mean(y,dtype=np.float32)

x_y_mean=np.multiply(x,y)
x_y_mean=np.sum(x_y_mean)/x.shape[0]
x_2_mean=np.mean(np.power(x,2))
x_mean_2=np.power(x_mean,2)
w1=(x_y_mean-(x_mean*y_mean))/(x_2_mean-x_mean_2)

w0=y_mean-w1*x_mean
print(w1)
print(w0)
t=np.arange(x[0],x[-1]+1)
f=np.zeros((1,t.size))
        
f=w0+w1*t
plt.figure(1)
plt.plot(t,f,'r',x,y,'o')
plt.xlabel('Ano')
plt.ylabel('Tempo (s)')
plt.savefig('03a_2.svg', format='svg',dpi=300 )




RMSE = RMSE(y,x,f,t)
print('-----')
print('Erro RMSE: {0:.2f}%'.format(RMSE*100))
print('-----')
#------ letrab------
f_2020=w0+w1*(2020)
print('O valor do resultado para o ano de 2020 é de: {0:.2f} s'.format(f_2020))
print('-----')
#-------letra c ------

combinations = np.array(list(combinations(np.arange(0,29),2)))

tal=get_tal(x,y,combinations)
tal=abs(tal)
print('tal: {0:.2f}'.format(tal))
N=x.size
z_5p = 1.96
z_1p = 2.33

print('z1-a/2(5%) : {0:.2f}'.format(z_5p*np.sqrt(2*(2*N+5)/(9*N*(N-1)))))
print('z1-a/2(1%) : {0:.2f}'.format(z_1p*np.sqrt(2*(2*N+5)/(9*N*(N-1)))))
if(tal > z_5p*np.sqrt(2*(2*N+5)/(9*N*(N-1)))):
    print('A hipótese nula foi rejeitada para 5% e existe a possibilidade de haver dependência entre x e y com 95% de significância')
if(tal > z_1p*np.sqrt(2*(2*N+5)/(9*N*(N-1)))):
    print('A hipótese nula foi rejeitada para 1% e existe a possibilidade de haver dependência entre x e y com 99% de significância')
            
print('-----')

#letra d



P=get_covariance(data)
print('P = {0:.2f}'.format(P))

t_0=P*(np.sqrt(N-2))/(np.sqrt(1-np.power(P,2)))
t_0 = abs(t_0)
print('|t_0| = {0:.2f}'.format(t_0))            

z_5p=2.052
z_1p=2.771 

if(t_0 > z_5p):
    print('A hipótese nula foi rejeitada para 5%, portanto há confiabilidade de 95% ')
if(t_0 > z_1p):
    print('A hipótese nula foi rejeitada para 1%, portanto há confiabilidade de 99%  ')
            
print('-----')
