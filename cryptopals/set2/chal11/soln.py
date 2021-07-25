from Crypto.Cipher import AES   
from Crypto.Util.Padding import pad,unpad  
import os                     
import random                 
import string                 

def randomkey(): 
    return os.urandom(16) 

def iv(): 
    return os.urandom(16) 

def ECB_ENCRYPTION (str1,key): 
    ct = AES.new((key),AES.MODE_ECB).encrypt(str1) 
    print ("ECB") 
    return ct 
                                                                    

def CBC_ENCRYPTION (str1,key,iv):
    ct = AES.new((key),AES.MODE_CBC,iv).encrypt(str1) 
    print ("CBC") 
    return ct 
                     

def encryption_oracle(str1,key,iv): 
    a = ""
    b = "" 
    for i in range(random.randint(5,10)): 
      a = a +(random.choice(allow))  
      b = b +(random.choice(allow)) 
    a = a.encode()
    b = b.encode()
    str1 =a +  str1 +b 
    str_pad = pad(str1,16)
    mode = random.randint(1,2)
    if mode == 1:
        ct = ECB_ENCRYPTION(str_pad,key)
    else:
        ct = CBC_ENCRYPTION(str_pad,key,iv)

    return ct

def ecb_detect(cipher_text,blocksize = 16):   
    def repeats(cipher_text):
        return (any([j in cipher_text[i+1:] for i,j in  enumerate(cipher_text)]))  
                                 
    return repeats(cipher_text)


if __name__ == "__main__":
    allow = string.printable                                
    key = randomkey()
    iv = iv()
    str1 = input().encode()
    ct = encryption_oracle(str1,key,iv)
    mode = "ECB"
    if (ecb_detect(ct,blocksize = 16)) != 1 :
        mode = "CBC"
    print("mode =", mode)




        



