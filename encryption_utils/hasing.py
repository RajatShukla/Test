__author__ = 'RAJAT'
from Crypto.Hash import *
from Crypto.Cipher import *
hashTypes = (('1','MD2'), ('2','MD4'), ('3','MD5'),
            ('4','SHA-1'), ('5','SHA-224'),('6','SHA-256'),
            ('7','SHA-384'),('8','SHA-512'),('9','RIPEMD'))


def hash(input_str, hash_type):
    if hash_type == 1: # MD2
        return str(MD2.new(input_str).hexdigest())
    if hash_type == 2: #MD4
        return MD4.new(input_str).hexdigest()
    if hash_type == 3: #MD5
        return MD5.new(input_str).hexdigest()
    if hash_type == 4: #SHA-1
        return SHA.new(input_str).hexdigest()
    if hash_type == 5: #SHA-224
        return SHA224.new(input_str).hexdigest()
    if hash_type == 6: #SHA-256
        return SHA256.new(input_str).hexdigest()
    if hash_type == 7: #SHA-384
        return SHA384.new(input_str).hexdigest()
    if hash_type == 8: #SHA-512
        return SHA512.new(input_str).hexdigest()
    if hash_type == 9: #RIPEMD
        return RIPEMD.new(input_str).hexdigest()
    else:
        return "Invalid type of Hashing algo code"




