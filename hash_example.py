import hashlib

text = "I am Satoshi Nakamoto"

for nonce in range(20):
    input = text + str(nonce)
    hash = hashlib.sha256(str(input).encode('utf-8')).hexdigest()
    print (input, '=>', hash)
