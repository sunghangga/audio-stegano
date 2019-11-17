import unittest
from aes import AES

class AES_TEST(unittest.TestCase):
    def setUp(self):
        master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
        self.AES = AES(master_key)

    def test_encryption(self):
        # message: my message
        plaintext = 0x6d79206d657373616765
        encrypted = self.AES.encrypt(plaintext)
        print ("enkrip: ")
        print (hex(encrypted))
        # self.assertEqual(encrypted, 0x3925841d02dc09fbdc118597196a0b32)

    def test_decryption(self):
        ciphertext = 0xe883a19a08a94bdb88663e18edb00a18
        decrypted = self.AES.decrypt(ciphertext)
        print ("dekrip: ")
        print (hex(decrypted))
        # self.assertEqual(decrypted, 0x3243f6a8885a308d313198a2e0370734)

if __name__ == '__main__':
    unittest.main()