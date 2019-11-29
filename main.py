import codecs
import testing as Test
import wavelet as Compress
import text_to_image as Tti
import image_to_wav as Itw
from use_aes import UseAES


# encrypt and decrypt
key = "iloveyou"
# encrypt message
# UseAES(key).to_encryption("aku sayang kamu")
# decrypt message
# UseAES(key).openFileEncrypt()

# resize image
# Compress.resize_img()
# haar wavelet (level, write, show)
# Compress.wavelet_image(1, True, False)

# LSB text to image
Tti.encrypt(key)
# Tti.decrypt(key)

# image to wav
# Itw.encrypt(key)
# Itw.decrypt(key)

# testing method
# print (Test.compare_str())
