from Crypto.Util.Padding import pad,unpad 

key = "YELLOW SUBMARINE"
key = key.encode()
block_size = 20
print(pad(key,block_size))