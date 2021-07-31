from Crypto.Util.number import *
a = [2,3,5]
n = [5,11,17]
res = 0
N = 1
for i in n: 
    N = N*i 
print(N) 

Ni = [] 
for i in range(3): 
    Ni.append(N//n[i]) 
print(Ni) 

M = []
for i in range(3):
    M.append(inverse(Ni[i],n[i]))

x = 0
for i in range(3): 
    x += (a[i]*Ni[i]*M[i]) 
print(x%N) 
