from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os


key = os.urandom(16)
iv = os.urandom(16)
    
def enc(pt): 
    for i in range(len(pt)): 
        if (pt[i] == ";") or (pt[i] == "="): 
            pt = pt.replace(pt[i] , "?")  
    pt = "comment1=cooking%20MCs;userdata=" + pt + ";comment2=%20like%20a%20pound%20of%20bacon" 
    pt = pad(pt.encode(),16) 
    mid = AES.new(key,AES.MODE_CBC,iv)
    ct = mid.encrypt(pt) 
    return ct


def blocks(ct,blocksize = 16):  
    return [ct[i:i+blocksize] for i in range(0,len(ct),blocksize)]   

def dec(ct):
    x = blocks(ct)      
    block = list(x[1])        # ;admin=true; in pt[2]
    block[0] = (block[0] ^ ord(";") ^ ord("?"))   #index("?")
    block[6] = (block[6] ^ ord("=") ^ ord("?"))
    block[11] = (block[11] ^ ord(";") ^ ord("?"))
    #print(block)
    x[1] = b"".join([bytes([i]) for i in block])   
    ciphertext = b''.join(x)
    pt =  unpad(AES.new(key,AES.MODE_CBC,iv).decrypt(ciphertext),16)
    if (b";admin=true;" in pt):
        print("You are Admin, Welcome")
    else:
        print("Try again")

    

if __name__ == "__main__":
    pt = ";admin=true;"
    ct = enc(pt)
    dec(ct)


