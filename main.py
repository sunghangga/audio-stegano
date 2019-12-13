import time
import os
import wave
from scipy.io import wavfile as wav
import cv2
import testing as Test
import wavelet as Compress
import text_to_image as Tti
import image_to_wav as Itw
from use_aes import UseAES


key = "ilkom123"
msg = "ilkom udayana"

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


'''Pengujian'''
for i in range(1,81):
	all_time = time.time()

	'''encrypt time'''
	all_encrypt_time = time.time()

	text_encrypt_time = time.time()
	'''encrypt message (message, path of plaintext, path of chipertext)'''
	UseAES(key).to_encryption(msg, "./text/plaintext/"str(i) + "_plaintext.txt", "./text/encrypt/"str(i) + "_encrypt.txt")
	text_encrypt_time = time.time() - text_encrypt_time

	img_encrypt_time = time.time()
	'''LSB text to image (key, pathOriginalImage, pathChiperText, pathDestinationImage)'''
	Tti.encrypt(key, "./image/source/LL_haar_1.bmp", "./text/encrypt/"str(i) + "_encrypt.txt", "./image/embed/"str(i) + "_embed.bmp")
	img_encrypt_time = time.time() - img_encrypt_time

	wav_encrypt_time = time.time()
	'''LSB image to wav (key, pathOriginalMusic, pathImageEmbbed, pathEmbbedWav)'''
	Itw.encrypt(key, "./music/source/"str(i) + "_source.wav", "./image/embed/"str(i) + "_embed.bmp", "./music/embed/"str(i) + "_embed.wav")
	wav_encrypt_time = time.time() - wav_encrypt_time

	all_encrypt_time = time.time() - all_encrypt_time

	'''decrypt time'''
	all_decrypt_time = time.time()

	wav_decrypt_time = time.time()
	'''LSB wav to image (key, pathEmbbedWav, pathDestinationImage, pathExtractWav)'''
	Itw.decrypt(key, "./music/embed/"str(i) + "_embed.wav", "./image/img_extract_wav/"str(i) + "_img_extract_wav.bmp", "./music/extract/"str(i) + "_extract.wav")
	wav_decrypt_time = time.time() - wav_decrypt_time

	img_decrypt_time = time.time()
	'''LSB image to text (key, pathEmbbedImage, pathDestinationText, pathExtractImage)'''
	Tti.decrypt(key, "./image/img_extract_wav/"str(i) + "_img_extract_wav.bmp", "./text/extract/"str(i) + "_extract.txt", "./image/img_extract_text/"str(i) + "_img_extract_text.bmp")
	img_decrypt_time = time.time() - img_decrypt_time

	text_decrypt_time = time.time()
	'''decrypt message (path of chipertext, path of decrypt)'''
	UseAES(key).openFileEncrypt("./text/extract/"str(i) + "_extract.txt", "./text/decrypt/"str(i) + "_decrypt.txt")
	text_decrypt_time = time.time() - text_decrypt_time

	all_decrypt_time = time.time() - all_decrypt_time

	all_time = time.time() - all_time

	file = open("./test/time/text_encrypt_time.txt","a+")
	file.write(str(text_encrypt_time))
	file.write("\n")
	file.close()

	file = open("./test/time/img_encrypt_time.txt","a+")
	file.write(str(img_encrypt_time))
	file.write("\n")
	file.close()

	file = open("./test/time/wav_encrypt_time.txt","a+")
	file.write(str(wav_encrypt_time))
	file.write("\n")
	file.close()

	file = open("./test/time/all_encrypt_time.txt","a+")
	file.write(str(all_encrypt_time))
	file.write("\n")
	file.close()

	file = open("./test/time/wav_decrypt_time.txt","a+")
	file.write(str(wav_decrypt_time))
	file.write("\n")
	file.close()

	file = open("./test/time/img_decrypt_time.txt","a+")
	file.write(str(img_decrypt_time))
	file.write("\n")
	file.close()

	file = open("./test/time/text_decrypt_time.txt","a+")
	file.write(str(text_decrypt_time))
	file.write("\n")
	file.close()

	file = open("./test/time/all_decrypt_time.txt","a+")
	file.write(str(all_decrypt_time))
	file.write("\n")
	file.close()

	file = open("./test/time/all_time.txt","a+")
	file.write(str(all_time))
	file.write("\n")
	file.close()


	'''testing method'''
	'''source with embed image'''
	im1 = cv2.imread("./image/source/LL_haar_1.bmp")
	im2 = cv2.imread("./image/embed/"str(i) + "_embed.bmp")

	file = open("./test/size/img_source.txt","a+")
	file.write(str(os.path.getsize("./image/source/LL_haar_1.bmp")))
	file.write("\n")
	file.close()
	file = open("./test/size/img_embed.txt","a+")
	file.write(str(os.path.getsize("./image/embed/"str(i) + "_embed.bmp")))
	file.write("\n")
	file.close()
	file = open("./test/size/img_extract.txt","a+")
	file.write(str(os.path.getsize("./image/img_extract_text/"str(i) + "_img_extract_text.bmp")))
	file.write("\n")
	file.close()
	file = open("./test/mse_psnr/mse_img_source_embed.txt","a+")
	file.write(str(Test.mse(im1,im2)))
	file.write("\n")
	file.close()
	file = open("./test/mse_psnr/psnr_img_source_embed.txt","a+")
	file.write(str(Test.psnr(im1,im2)))
	file.write("\n")
	file.close()

	im2 = cv2.imread("./image/img_extract_text/"str(i) + "_img_extract_text.bmp")
	file = open("./test/mse_psnr/mse_img_source_extract.txt","a+")
	file.write(str(Test.mse(im1,im2)))
	file.write("\n")
	file.close()
	file = open("./test/mse_psnr/psnr_img_source_extract.txt","a+")
	file.write(str(Test.psnr(im1,im2)))
	file.write("\n")
	file.close()
	# print(Test.mse(im1,im2))
	# print(Test.psnr(im1,im2))


	'''source with embed wav'''
	song1 = wave.open("./music/source/"str(i) + "_source.wav", mode='rb')
	song1 = list(song1.readframes(song1.getnframes()))
	song2 = wave.open("./music/embed/"str(i) + "_embed.wav", mode='rb')
	song2 = list(song2.readframes(song2.getnframes()))

	file = open("./test/size/wav_source.txt","a+")
	file.write(str(os.path.getsize("./music/source/"str(i) + "_source.wav")))
	file.write("\n")
	file.close()
	file = open("./test/size/wav_embed.txt","a+")
	file.write(str(os.path.getsize("./music/embed/"str(i) + "_embed.wav")))
	file.write("\n")
	file.close()
	file = open("./test/size/wav_extract.txt","a+")
	file.write(str(os.path.getsize("./music/extract/"str(i) + "_extract.wav")))
	file.write("\n")
	file.close()
	file = open("./test/mse_psnr/mse_wav_source_embed.txt","a+")
	file.write(str(Test.mse(song1,song2)))
	file.write("\n")
	file.close()
	file = open("./test/mse_psnr/psnr_wav_source_embed.txt","a+")
	file.write(str(Test.psnr(song1,song2)))
	file.write("\n")
	file.close()

	song2 = wave.open("./music/extract/"str(i) + "_extract.wav", mode='rb')
	song2 = list(song2.readframes(song2.getnframes()))
	file = open("./test/mse_psnr/mse_wav_source_extract.txt","a+")
	file.write(str(Test.mse(song1,song2)))
	file.write("\n")
	file.close()
	file = open("./test/mse_psnr/psnr_wav_source_extract.txt","a+")
	file.write(str(Test.psnr(song1,song2)))
	file.write("\n")
	file.close()
	# print(Test.mse(song1,song2))
	# print(Test.psnr(song1,song2))


	'''source with extract'''
	text1 = open("./text/encryption.txt", "r").read()
	text1 = list(map(int, list(text1)))
	text2 = open("./text/extract_from_image.txt", "r").read()
	text2 = list(map(int, list(text2)))

	file = open("./test/size/text_source.txt","a+")
	file.write(str(os.path.getsize("./text/encrypt/"str(i) + "_encrypt.txt")))
	file.write("\n")
	file.close()
	file = open("./test/size/text_extract.txt","a+")
	file.write(str(os.path.getsize("./text/extract/"str(i) + "_extract.txt")))
	file.write("\n")
	file.close()

	file = open("./test/mse_psnr/mse_text_encrypt_extract.txt","a+")
	file.write(str(Test.mse(text1,text2)))
	file.write("\n")
	file.close()
	file = open("./test/mse_psnr/psnr_text_encrypt_extract.txt","a+")
	file.write(str(Test.psnr(text1,text2)))
	file.write("\n")
	file.close()
	# print(Test.mse(text1,text2))
	# print(Test.psnr(text1,text2))

	print(i)