# compare string
def compare_str():
    file = open("./text/plaintext.txt","r+")
    plaintext = file.read()
    file.close()

    file = open("./text/decryption.txt","r+")
    decrypt_text = file.read()
    file.close()

    return plaintext == decrypt_text