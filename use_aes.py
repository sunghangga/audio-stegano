import unittest
import codecs
from aes import AES

class UseAES:
    def __init__(self, key):
        keyConvert = key.encode("utf-8")
        keyConvert = int(codecs.encode(keyConvert, "hex"), 16)
        master_key = keyConvert
        self.AES = AES(master_key)

    def to_encryption(self, message):
        # message: my message / 0x6d79206d657373616765
        message = message.encode("utf-8")
        # convert from byte string to hex int
        message = int(codecs.encode(message, "hex"), 16)
        plaintext = message
        
        # insert plaintext to txt
        file = open("./text/plaintext.txt","w+")
        file.write(str(plaintext))
        file.close()

        encrypted = self.AES.encrypt(plaintext)

        file = open("./text/encryption.txt","w+")
        file.write(str(encrypted))
        file.close()

    def to_decryption(self, ciphertext):
        decrypted = self.AES.decrypt(ciphertext)
        # convert from int to hex
        # varDecrypted = format(decrypted, "x")
        # convert hex to string
        # varDecrypted = bytes.fromhex(varDecrypted).decode("utf-8")
        file = open("./text/decryption.txt","w+")
        file.write(str(decrypted))
        file.close()

    def openFileEncrypt(self):
        file = open("./text/encryption.txt","r+")
        self.encStr = int(file.read())
        file.close()
        self.to_decryption(self.encStr)
