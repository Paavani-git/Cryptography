from Crypto.Util.Padding import pad,unpad 

key = "YELLOW SUBMARINE"
key = key.encode()
block_size = 20
print(pad(key,block_size))

def padding(pt,blocksize=20): 
    pad = blocksize - (len(pt)%blocksize) 
    return pt+(chr(pad)*pad).encode() 
     
print(padding(key))
