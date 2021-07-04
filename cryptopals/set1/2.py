str1=bytes.fromhex('1c0111001f010100061a024b53535009181c')
str2=bytes.fromhex('686974207468652062756c6c277320657965')

x=bytes([x1^x2 for x1,x2 in zip(str1,str2)])

print(x.hex())
