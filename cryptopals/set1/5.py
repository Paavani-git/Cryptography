from itertools import cycle
from binascii import hexlify
from codecs import *
def rep_xor(text,key):
	x = ("".join(chr(ord(i)^ord(j)) for i,j in zip(text,cycle(key)))
return (x.encode("utf-8").hex()) 
msg=b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"""
key = b"ICE"
print(rep_xor(msg,key))