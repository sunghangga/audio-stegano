import codecs
from aes import AES

class UseAES:
    def __init__(self, key):
        keyConvert = key.encode("utf-8")
        keyConvert = int(codecs.encode(keyConvert, "hex"), 16)
        master_key = keyConvert
        self.AES = AES(master_key)

    def to_encryption(self, message, pathPlain, pathChiper):
        # message: my message / 0x6d79206d657373616765
        message = message.encode("utf-8")
        # convert from byte string to hex int
        message = int(codecs.encode(message, "hex"), 16)
        plaintext = message
        
        # insert plaintext to txt
        file = open(pathPlain,"w+")
        file.write(str(plaintext))
        file.close()

        encrypted = self.AES.encrypt(plaintext)

        file = open(pathChiper,"w+")
        file.write(str(encrypted))
        file.close()

    def to_decryption(self, ciphertext, pathDecrypt):
        decrypted = self.AES.decrypt(ciphertext)
        file = open(pathDecrypt,"w+")
        file.write(str(decrypted))
        file.close()

    def openFileEncrypt(self, pathChiper, pathDecrypt):
        file = open(pathChiper,"r+")
        self.encStr = int(file.read())
        file.close()
        self.to_decryption(self.encStr, pathDecrypt)
