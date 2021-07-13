from Crypto.Cipher import AES     
from Crypto.Util.Padding import pad,unpad    
from binascii import *                                     
   
  
def blocks(ct,blocksize):  
    return [ct[i:i+blocksize] for i in range(0,len(ct),blocksize)]   
def repeats(ct):  
    return (any([j in ct[i+1:] for i,j in  enumerate(ct)]))  
   
   
ct = []                                                    
blocksize = 16  
for l in open("8.txt"):   
    ct.append(unhexlify(l.strip()))   
x = [blocks(i,blocksize) for i in ct]                                  
ct_reps = [repeats(i) for i in x] 
resi = ct_reps.index(True) 
result = ct[resi] 
print("ECB block :", result)

 
