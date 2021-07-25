from Crypto.Cipher import AES    
from Crypto.Util.Padding import pad,unpad   
from binascii import *   
def encrypt_oracle(ipt): 
    secret="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK" 
    secret = a2b_base64(secret) 
    pt = ipt.encode() + secret 
    pr = pad(pt,16) 
    key = b'YELLOW SUBMARINE' 
    CT = AES.new(key,AES.MODE_ECB).encrypt(pr) 
    return CT 

def sec_len():               #for finding lenght of flag
    sec_len = 0 
    msg = "A"*sec_len 
    l = 0 
    il = len(encrypt_oracle(msg)) 
    for i in range(20): 
        m = i*"A" 
        al = len(encrypt_oracle(m)) 
        if (al != il): 
            len_sec = i 
            break 
    len_secret = il-len_sec 
    return len_secret 
     
def expliot(): 
    sec = "" 
    block = (len(encrypt_oracle("A"))) // 16   
    for k in range(1,(block+1)): 
        for j in range(15,-1,-1): 
            imput = j *"A" 
            x =  encrypt_oracle(imput) 
            for i in range(256): 
                final = encrypt_oracle(imput+sec+chr(i)) 
                if (final[:16*k] == x[:16*k]): 
                    sec += chr(i) 
                    break 
    print(sec) 

if __name__ == "__main__":
    expliot()
    sec_len()
    


  
