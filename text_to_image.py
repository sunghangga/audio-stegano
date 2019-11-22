import cv2

# file = open("./image/image_resize.bmp", "rb+")
# fileList = file.readlines()

# file.write(b"\n")
# file.write(bytes([3]))
# print (fileList[-1])
# print (int.from_bytes(fileList[-1], byteorder='big'))

# file.close()


def to_bit_generator(msg):
    """Converts a message into a generator which returns 1 bit of the message
    each time."""
    for c in (msg):
        o = ord(c)
        for i in range(8):
            yield (o & (1 << i)) >> i

def encrypt():
    # Create a generator for the hidden message
    hidden_message = to_bit_generator(open("README.md", "r").read() * 10)
    
    # Read the original image
    img = cv2.imread('original.png', cv2.IMREAD_GRAYSCALE)
    for h in range(len(img)):
        for w in range(len(img[0])):
            # Write the hidden message into the least significant bit
            img[h][w] = (img[h][w] & ~1) | next(hidden_message)
    # Write out the image with hidden message
    cv2.imwrite("output.png", img)

def decrypt():
	# Read the image and try to restore the message
	img = cv2.imread('output.png', cv2.IMREAD_GRAYSCALE)
	i = 0
	bits = ''
	chars = []
	for row in img:
	    for pixel in row:
	        bits = str(pixel & 0x01) + bits
	        i += 1
	        if(i == 8):
	            chars.append(chr(int(bits, 2)))
	            i = 0
	            bits = ''
	print(''.join(chars))

encrypt()