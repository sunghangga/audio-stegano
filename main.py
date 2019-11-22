import codecs
import testing as Test
import wavelet as Compress
from use_aes import UseAES


# encrypt and decrypt
# key = "asuuu"
# print (UseAES(key).to_encryption("aku sayang kamu"))
# print (UseAES(key).openFileEncrypt())

# compare string
# print (Test.compare_str())

# resize image
# Compress.resize_img()
# rgb to grayscale image
# Compress.rgb_to_gray()

# haar wavelet (level, write, show)
Compress.wavelet_image(1, False, False)