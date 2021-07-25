from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import *

def CTR_MODE(pt,key):
    for i in range(len(pt)): 
        if (pt[i] == "="): 
            pt = pt.replace(pt[i] , "?")  
    pt = "comment1=cooking%20MCs;userdata=" + pt + ";comment2=%20like%20a%20pound%20of%20bacon" 
    pt = pt.encode() 
    ctr = Counter.new(64,prefix=b'\x00'*8, initial_value=0, little_endian=True)
    ct = AES.new(key,AES.MODE_CTR,counter=ctr).decrypt(pt)
    return ct

def blocks(ct,blocksize = 16):  
    return [ct[i:i+blocksize] for i in range(0,len(ct),blocksize)]   


def dec(ct):
    x = blocks(ct)      
    block = list(x[2])        # ;admin=true; in pt[2]   
    block[5] = (block[5] ^ ord("=") ^ ord("?"))    #index("?")
    x[2] = b"".join([bytes([i]) for i in block]) 
    ciphertext = b''.join(x)
    ctr = Counter.new(64,prefix=b'\x00'*8, initial_value=0, little_endian=True)
    pt = AES.new(key,AES.MODE_CTR,counter=ctr).decrypt(ciphertext)
    if (b"admin=true" in pt):
        print("You are Admin, Welcome")
    else:
        print("Try again")


if __name__ == '__main__':
    pt = "admin=true"
    key = b"YELLOW SUBMARINE"
    ct = CTR_MODE(pt,key)
    dec(ct)
