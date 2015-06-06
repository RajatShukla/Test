#from django.contrib import admin
#from DevUtils1 import models

# Register your models here.
from Crypto.Hash import HMAC
from Crypto.Hash import MD2
from Crypto.Hash import MD4
from Crypto.Hash import MD5
from Crypto.Hash import RIPEMD
from Crypto.Hash import SHA224
from Crypto.Hash import SHA256
from Crypto.Hash import SHA384
from Crypto.Hash import SHA512

print("HMAC encryption", HMAC.new('abc').hexdigest())
print("MD2 encryption", MD2.new('abc').hexdigest())
print("MD4 encryption", MD4.new('abc').hexdigest())
print("MD5 encryption", MD5.new('abc').hexdigest())
print("RIPEMD encryption", RIPEMD.new('abc').hexdigest())
print("SHA224 encryption", SHA224.new('abc').hexdigest())
print("SHA256 encryption", SHA256.new('abc').hexdigest())
print("SHA384 encryption", SHA384.new('abc').hexdigest())
print("SHA512 encryption", SHA512.new('abc').hexdigest())



#################3
from Crypto.Cipher import DES
des = DES.new('01234567', DES.MODE_ECB)
text = 'abcdefgh'
cipher_text = des.encrypt(text)
text = des.decrypt(cipher_text)
print(cipher_text, text)

#############################3
from Crypto.Cipher import DES
from Crypto import Random
iv = Random.get_random_bytes(8)
des1 = DES.new('01234567', DES.MODE_CFB, iv)
des2 = DES.new('01234567', DES.MODE_CFB, iv)
text = 'abcdefghijklmnop'
cipher_text = des1.encrypt(text)
des2.decrypt(cipher_text)
###############################


from Crypto.Cipher import ARC4
obj1 = ARC4.new('01234567')
obj2 = ARC4.new('01234567')
text = 'abcdefghijklmnop'
cipher_text = obj1.encrypt(text)
obj2.decrypt(cipher_text)



#####################################