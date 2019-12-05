import codecs
import wave
from scipy.io import wavfile as wav
import cv2
import testing as Test
import wavelet as Compress
import text_to_image as Tti
import image_to_wav as Itw
from use_aes import UseAES


'''encrypt and decrypt'''
key = "iloveyou"
msg = "aku sayang kamu"
'''encrypt message (message, path of plaintext, path of chipertext)'''
# UseAES(key).to_encryption(msg, "./text/plaintext.txt", "./text/encryption.txt")
'''decrypt message (path of chipertext, path of decrypt)'''
# UseAES(key).openFileEncrypt("./text/encryption.txt", "./text/decryption.txt")

'''resize image'''
# Compress.resize_img()

'''haar wavelet (level, path of original image, write, show)'''
# Compress.wavelet_image(3, "./image/image.bmp", True, False)

'''LSB text to image (key, pathOriginalImage, pathChiperText, pathDestinationImage)'''
# Tti.encrypt(key, "./image/LL_haar_1.bmp", "./text/encryption.txt", "./image/text_to_img.bmp")
'''LSB image to text (key, pathEmbbedImage, pathDestinationText, pathExtractImage)'''
# Tti.decrypt(key, "./image/text_to_img.bmp", "./text/extract_from_image.txt", "./image/extract_image.bmp")

'''LSB image to wav (key, pathOriginalMusic, pathImageEmbbed, pathEmbbedWav)'''
# Itw.encrypt(key, "./music/Sympy.wav", "./image/text_to_img.bmp", "./music/song_embedded.wav")
'''LSB wav to image (key, pathEmbbedWav, pathDestinationImage, pathExtractWav)'''
# Itw.decrypt(key, "./music/song_embedded.wav", "./image/img_from_wav.bmp", "./music/song_extract.wav")


'''testing method'''
# im1 = cv2.imread("./image/LL_haar_1.bmp")
# im2 = cv2.imread("./image/extract_image.bmp")
# print(Test.mse(im1,im2))
# print(Test.psnr(im1,im2))

# song1 = wave.open("./music/Sympy.wav", mode='rb')
# song1 = list(song1.readframes(song1.getnframes()))
# song2 = wave.open("./music/song_extract.wav", mode='rb')
# song2 = list(song2.readframes(song2.getnframes()))
# print(Test.mse(song1,song2))
# print(Test.psnr(song1,song2))

# text1 = open("./text/encryption.txt", "r").read()
# text1 = list(map(int, list(text1)))
# text2 = open("./text/extract_from_image.txt", "r").read()
# text2 = list(map(int, list(text2)))
# print(Test.mse(text1,text2))
# print(Test.psnr(text1,text2))