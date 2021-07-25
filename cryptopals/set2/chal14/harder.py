from Crypto.Cipher import AES    
from Crypto.Util.Padding import pad,unpad   
from binascii import *   
from string import * 
rand = b"STIMULUS" 
def encrypt_oracle(ipt,rand): 
    secret="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK" 
    secret = a2b_base64(secret) 
    pt = rand + ipt.encode() + secret 
    pr = pad(pt,16) 
    key = b'YELLOW SUBMARINE' 
    CT = AES.new(key,AES.MODE_ECB).encrypt(pr) 
    return CT 


def sec_len(rand):
    sec_len = 0 
    msg = rand + "A"*sec_len  
    l = 0 
    il = len(encrypt_oracle(msg,rand)) 
    for i in range(40): 
        m = rand + i*"A" 
        al = len(encrypt_oracle(m,rand)) 
        if (al != il): 
            len_sec = len_rand_input() + i 
            break 
    len_secret = il-len_sec 
    return len_secret 
  
    
def len_rand_input():           #length of random
    x = [] 
    for i in range(10): 
        ipt = "" 
        for j in range(16): 
            il = encrypt_oracle(ipt,rand)[i*16:(i+1)*16] 
            #print(il,i) 
            ipt+="A" 
            al = encrypt_oracle(ipt,rand)[i*16:(i+1)*16] 
            #print(al,i) 
            if (il) == (al): 
                x+=[len(ipt)-1] 
                x = 16 - x[0] 
                break 
                 
    return x 

def expliot():  
    sec = ""  
    block = (len(encrypt_oracle("A",rand))) // 16    
    for k in range(2,(block+1)):  
        for j in range(15,-1,-1):  
            imput = len_rand_input()*"A" + j *"A"  
            x =  encrypt_oracle(imput,rand)  
            for i in range(256):  
                final = encrypt_oracle(imput+sec+chr(i),rand) 
                if (final[:16*k] == x[:16*k]):  
                    sec += chr(i)  
                    break  
    print(sec)  
 

if __name__ == "__main__":
    expliot()
    