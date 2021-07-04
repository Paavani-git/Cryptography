from collections import Counter

def single_byte_xor(text, key): 
     return bytes([b ^ key for b in text]) 

frequency= {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094, 'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025, 'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929, 'q': .00095, 'r': .05987, 's': .06327, 't': .09056, 'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150, 'y': .01974, 'z': .00074, ' ': .13000}


dist_english = list(frequency.values())

def score(text):
    freq_lt = Counter(text)                     #frequency of each letters in the given text
    dist_text = [(freq_lt.get(ord(ch), 0) ) / len(text) for ch in frequency]            
    
    return sum([abs(a - b) for a, b in zip(dist_english, dist_text)]) / len(dist_text)

def decipher(text):
    pt, key, min_fq = None, None, None
    for k in range(256):
        xor_text = single_byte_xor(text, k)
        fq = score(xor_text)
        # print(fq,k)
        if min_fq is None or fq < min_fq:
            key, pt, min_fq = k, xor_text, fq
    return pt, key
hex_text='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
ct=bytes.fromhex(hex_text)
print(decipher(ct))