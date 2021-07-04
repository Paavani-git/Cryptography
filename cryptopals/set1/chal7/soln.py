from base64 import *
from Crypto.Cipher import AES
with open("7.txt") as f:
	cipher = b64decode(f.read())
key = "YELLOW SUBMARINE"
key = key.encode()
ct = AES.new(key,AES.MODE_ECB)
pt = ct.decrypt(cipher)
print(pt)
