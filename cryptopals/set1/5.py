def rep_xor(text,key): 
    return b''.join([bytes([key[i%len(key)]^j]) for i,j in enumerate(text)]) 
msg = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal" 
key = b"ICE" 
print(rep_xor(msg,key).hex()) 
