from Crypto.Cipher import AES
from binascii import *

def CTR_ENC(ct, key):
   pt = b''
   lists = blocks(ct)
   for i,j in zip((range(len(blocks(ct)))),lists):
       iv = counterq(i)
       pt += rep_xor(ecb_mode(iv,key),j) 
   return pt[:-12]

        
def rep_xor(text,key):
    return b''.join(bytes([key[i%len(key)]^j]) for i,j in enumerate(text))

def blocks(ct,blocksize = 16):  
    return [ct[i:i+blocksize] for i in range(0,len(ct),blocksize)]   

def counterq(n):
    nonce = 0
    x = nonce.to_bytes(length=8, byteorder='little') + (n).to_bytes(length = 8, byteorder = "little")
    return x

def ecb_mode(pt, key): 
    return AES.new(key,AES.MODE_ECB).encrypt(pt) 

ct ="L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
ct = a2b_base64(ct.encode())
key=b"YELLOW SUBMARINE"
pt = CTR_ENC(ct,key)
ct = CTR_ENC(pt,key)
print("pt:",pt)
print("ct:",ct)





