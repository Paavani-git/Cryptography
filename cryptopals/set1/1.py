from binascii import *
str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
str_hex = unhexlify(str)   #hex to bytes
str_asc = b2a_base64(str_hex) #bytes to ascii
print(str_asc.decode("UTF-8"))