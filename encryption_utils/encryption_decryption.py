__author__ = 'RAJAT'
from Crypto.Cipher import *
from Crypto import Random

def encrypt_decrypt(input_text, input_key, encryption_type, operatation):
    if operatation == 1 : # means encrypt the  string
        encrypted_str = encryption(input_text, input_key, encryption_type)
        return encrypted_str
    if operatation == 2: # means decrypt the string
        decrypted_str = decryption(input_text, input_key, encryption_type)
        return decrypted_str
    else:
        return "Unwanted operation type"



def encryption(input_text, input_key, encryption_type):
    if encryption_type == 1:
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(input_key, AES.MODE_CFB, iv)
        encrypted_text = cipher.encrypt(input_text)
        hex_str = ""
        for i in encrypted_text:
            hex_str += str("%0.02X"%ord(i))
        return hex_str
    if encryption_type == 2:
        cipher = ARC2.new(input_key, ARC2.MODE_CFB)
        return cipher.encrypt(input_text)
    if encryption_type == 3:
        cipher = ARC4.new(input_key, ARC4.MODE_CFB)
        return cipher.encrypt(input_text)
    if encryption_type == 4:
        cipher = Blowfish.new(input_key, Blowfish.MODE_CFB)
        return cipher.encrypt(input_text)
    if encryption_type == 5:
        cipher = CAST.new(input_key, CAST.MODE_CFB)
        return cipher.encrypt(input_text)
    if encryption_type == 6:
        cipher = DES.new(input_key, DES.MODE_CFB)
        return cipher.encrypt(input_text)
    if encryption_type == 7:
        cipher = DES3.new(input_key, DES3.MODE_CFB)
        return cipher.encrypt(input_text)
    if encryption_type == 8:
        cipher = PKCS1_OAEP.new(input_key, PKCS1_OAEP.MODE_CFB)
        return cipher.encrypt(input_text)
    if encryption_type == 9:
        cipher = XOR.new(input_key, XOR.MODE_CFB)
        return cipher.encrypt(input_text)
    else:
        return "Unwanted encryption algo"





def decryption(input_text, input_key, encryption_type):
    if encryption_type == 1:
        cipher = AES.new(input_key, AES.MODE_CFB)
        return cipher.decrypt(input_text)
    if encryption_type == 2:
        cipher = ARC2.new(input_key, ARC2.MODE_CFB)
        return cipher.decrypt(input_text)
    if encryption_type == 3:
        cipher = ARC4.new(input_key, ARC4.MODE_CFB)
        return cipher.decrypt(input_text)
    if encryption_type == 4:
        cipher = Blowfish.new(input_key, Blowfish.MODE_CFB)
        return cipher.decrypt(input_text)
    if encryption_type == 5:
        cipher = CAST.new(input_key, CAST.MODE_CFB)
        return cipher.decrypt(input_text)
    if encryption_type == 6:
        cipher = DES.new(input_key, DES.MODE_CFB)
        return cipher.decrypt(input_text)
    if encryption_type == 7:
        cipher = DES3.new(input_key, DES3.MODE_CFB)
        return cipher.decrypt(input_text)
    if encryption_type == 8:
        cipher = PKCS1_OAEP.new(input_key, PKCS1_OAEP.MODE_CFB)
        return cipher.decrypt(input_text)
    if encryption_type == 9:
        cipher = XOR.new(input_key, XOR.MODE_CFB)
        return cipher.decrypt(input_text)
    else:
        return "Unwanted encryption algorithm"