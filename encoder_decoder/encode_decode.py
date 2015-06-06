__author__ = 'RAJAT'
import base64
codecTypes = (('1','UTF-16'), ('2','UTF-32'), ('3','UTF-8'),
                  ('4','ASCII'), ('5','CP1256'), ('6','ISO-8859-1'),
                  ('7','ISO-8859-2'), ('8','ISO-8859-6'), ('9','ISO-8859-15'),
                  ('10','Windows-1252'))

def encoder(string_for_encoding, codecType):
    if codecType == 1:
        return encodeBase64ToUTF16(string_for_encoding)
    if codecType == 2:
        return encodeBase64ToUTF32(string_for_encoding)
    if codecType == 3:
        return encodeBase64ToUTF8(string_for_encoding)
    if codecType == 4:
        return encodeBase64ToAscii(string_for_encoding)
    if codecType == 5:
        return encodeBase64ToCP1256(string_for_encoding)
    if codecType == 6:
        return encodeBase64ToISO8859_1(string_for_encoding)
    if codecType == 7:
        return encodeBase64ToISO8859_2(string_for_encoding)
    if codecType == 8:
        return encodeBase64ToISO8859_6(string_for_encoding)
    if codecType == 9:
        return  encodeBase64ToISO8859_15(string_for_encoding)
    if codecType == 10:
        return encodeBase64ToWinows1252(string_for_encoding)



def decoder(string_for_decoding, codecType):
    if codecType == 1:
        return decodeBase64ToUTF16(string_for_decoding)
    if codecType == 2:
        return decodeBase64ToUTF32(string_for_decoding)
    if codecType == 3:
        return decodeBase64ToUTF8(string_for_decoding)
    if codecType == 4:
        return decodeBase64ToAscii(string_for_decoding)
    if codecType == 5:
        return decodeBase64ToCP1256(string_for_decoding)
    if codecType == 6:
        return decodeBase64ToISO8859_1(string_for_decoding)
    if codecType == 7:
        return decodeBase64ToISO8859_2(string_for_decoding)
    if codecType == 8:
        return decodeBase64ToISO8859_6(string_for_decoding)
    if codecType == 9:
        return  decodeBase64ToISO8859_15(string_for_decoding)
    if codecType == 10:
        return decodeBase64ToWinows1252(string_for_decoding)


def encodeBase64ToAscii(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('ascii'))





def encodeBase64ToUTF8(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('utf-8'))



def encodeBase64ToUTF16(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('utf-16'))


def encodeBase64ToUTF32(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('utf-32'))



def encodeBase64ToCP1256(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('cp1256'))



def encodeBase64ToISO8859_1(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('iso-8859-1'))


def encodeBase64ToISO8859_2(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('iso-8859-2'))


def encodeBase64ToISO8859_6(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('iso-8859-6'))

def encodeBase64ToISO8859_15(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('iso-8859-15'))



def encodeBase64ToWinows1252(stringForEncoding):
    return base64.b64encode(stringForEncoding.encode('windows-1252'))



#This module converts  the encoded base64 string into respective format

#Converts the base64 string into ASCII
def decodeBase64ToAscii(encodedBase64String):
    print("String returned from the decodeBase64ToAscii function")
    try:
        return base64.b64decode(encodedBase64String)
    except Exception:
        return "Invalid padding of encoded string"



#Converts the base64 string into UTF-8
def decodeBase64ToUTF8(encodedBase64String):
    try:
        return base64.b64decode(encodedBase64String).decode('utf8')
    except Exception:
        return "Invalid padding of encoded string"



def decodeBase64ToUTF16(encodedBase64String):
    try:
        return base64.b64decode(encodedBase64String).decode('utf16')
    except Exception:
        return "Invalid padding of encoded string"







def decodeBase64ToUTF32(encodedBase64String):
    try:
        return base64.b64decode(encodedBase64String).decode('utf32')
    except Exception:
        return "Invalid padding of encoded string"

def decodeBase64ToCP1256(encodedBase64String):
    try:
        decodedString=base64.b64decode(encodedBase64String).decode('cp1256')
        print("Decoded string:",decodedString)
        return decodedString
    except Exception:
        return "Invalid padding of encoded string"



def decodeBase64ToISO8859_1(encodedBase64String):
    try:
        return base64.b64decode(encodedBase64String).decode('iso8859-1')
    except Exception:
        return "Invalid padding of encoded string"


def decodeBase64ToISO8859_2(encodedBase64String):
    try:
        return base64.b64decode(encodedBase64String).decode('iso8859-2')
    except Exception:
        return "Invalid padding of encoded string"



def decodeBase64ToISO8859_6(encodedBase64String):
    try:
        return base64.b64decode(encodedBase64String).decode('iso8859-6')
    except Exception:
        return "Invalid padding of encoded string"

def decodeBase64ToISO8859_15(encodedBase64String):
    try:
        return base64.b64decode(encodedBase64String).decode('iso8859-15')
    except Exception:
        return "Invalid padding of encoded string"



def decodeBase64ToWinows1252(encodedBase64String):
    try:
        return base64.b64decode(encodedBase64String).decode('windows-1252')
    except Exception:
        return "Invalid padding of encoded string"


