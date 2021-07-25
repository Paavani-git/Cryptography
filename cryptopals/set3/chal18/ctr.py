#https://pythonhosted.org/pycrypto/Crypto.Util.Counter-module.html

from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import *

def CTR_MODE(ct,key):
    ctr = Counter.new(64,prefix=b'\x00'*8, initial_value=0, little_endian=True)
    pt = AES.new(key,AES.MODE_CTR,counter=ctr).decrypt(ct)
    return pt
if __name__ == '__main__':
    ct ="L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
    ct = a2b_base64(ct.encode())
    key = b"YELLOW SUBMARINE"
    pt = CTR_MODE(ct,key)
    ct = CTR_MODE(pt,key)
    print(pt)
    print(ct)    
