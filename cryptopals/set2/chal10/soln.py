from Crypto.Cipher import AES  
from Crypto.Util.Padding import pad,unpad 
from binascii import * 
x = open("10.txt",'r').read() 
xb = a2b_base64(x)  
iv = "\x00\x00\x00 &c"  
key = "YELLOW SUBMARINE"
iv = pad(iv.encode() ,16) 
key =(key.encode()) 
pt=AES.new(key,AES.MODE_CBC,iv).decrypt(xb)  
print(pt)
