import cv2


def to_bit_generator(msg):
    """Converts a message into a generator which returns 1 bit of the message
    each time."""
    for c in (msg):
    	o = ord(c)
    	for i in range(8):
        	yield (o & (1 << i)) >> i

def encrypt(key, pathOriginalImage, pathChiperText, pathDestinationImage):
	path_image = pathOriginalImage
	path_chiper = open(pathChiperText, "r").read()

    # Create a generator for the hidden message and key
	hidden_message = to_bit_generator(path_chiper)
	key_gen = to_bit_generator(key)

    # Read the original image
	img = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)
	key_list = list(key_gen)

	byte_iter = ""
	j = 0
	for i in (hidden_message):
		# Write the hidden message into the least significant bit
		img[0][0] = (img[0][0] & ~1) | (key_list[j] ^ i)
		byte_iter += str(img[0][0] & 0x01)

		j += 1
		if(j > len(bytes(key_list))-1):
			j = 0
		
	# Write out the image with hidden message
	cv2.imwrite(pathDestinationImage, img)

	# write length binary string in image
	file = open(pathDestinationImage, "rb+")
	fileList = file.readlines()
	
	file.write(b"\n")
	file.write(str.encode(byte_iter))

	file.close()

def decrypt(key, pathEmbbedImage, pathDestinationText, pathExtractImage):
	# Read the image and try to restore the message
	img = cv2.imread(pathEmbbedImage, cv2.IMREAD_GRAYSCALE)
	i = 0
	bits = ''
	chars = []
	key_gen = to_bit_generator(key)
	key_list = list(key_gen)

	# read image state
	file = open(pathEmbbedImage, "rb+")

	fileList = file.readlines()
	state = fileList[-1]
	state = list(str(state, 'utf-8'))
	len_text = len(state)

	file.close()

	m = len(state)-2
	k = (len_text % len(key_list))-1
	for j in range(len_text):
		# Write the hidden message into the least significant bit
		bits = bits + str((img[0][0] ^ key_list[k]) & 0x01)
		img[0][0] = (img[0][0] & ~1) | int(state[m])
		
		i += 1
		k -= 1
		m -= 1
		# loop key
		if(k < 0):
			k = len(key_list)-1
		# generate ascii
		if(i == 8):
			chars.append(chr(int(bits, 2)))
			i = 0
			bits = ''
	# reserve array
	chars.reverse()

	# create as txt file output
	file = open(pathDestinationText,"w+")
	file.write(str(''.join(chars)))
	file.close()

	# delete last line of file
	file = open(pathEmbbedImage, "rb+")
	fileList = file.readlines()
	lastLine = fileList[-2]
	lines = fileList[:-2]
	lines.append(lastLine[:-1])
	file.close()

	file = open(pathExtractImage, "wb+")
	file.writelines([item for item in lines])
	file.close()