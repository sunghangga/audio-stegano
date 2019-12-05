import wave
import cv2
import numpy as np

def encrypt(key, pathOriginalMusic, pathImageEmbbed, pathEmbbedWav):
    # read wave audio file
    song = wave.open(pathOriginalMusic, mode='rb')
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # open image
    path_image = pathImageEmbbed
    typeImage = path_image.split(".")
    
    # read length text and state
    file = open(pathImageEmbbed, "rb+")
    fileList = file.readlines() 
    state = fileList[-1]
    file.close()

    # from img to bytes
    img = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)
    is_success, im_buf_arr = cv2.imencode("." + str(typeImage[-1]), img)
    byte_im = im_buf_arr.tobytes()
    nparr = np.fromstring(byte_im, np.uint8)
    # convert to bit array
    nparr = list(map(int, ''.join([bin(i).lstrip('0b').rjust(8,'0') for i in nparr])))

    # Convert text to bit array
    key_list = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in key])))

    # Replace LSB of each byte of the audio data by one bit from the text bit array
    byte_iter = ""
    j = 0
    for i in nparr:
        # Write the hidden message into the least significant bit
        frame_bytes[0] = (frame_bytes[0] & ~1) | (key_list[j] ^ i)
        byte_iter += str(frame_bytes[0] & 0x01)

        j += 1
        if(j > len(bytes(key_list))-1):
            j = 0

    # Get the modified bytes
    frame_modified = bytes(frame_bytes)

    # Write bytes to a new wave audio file
    with wave.open(pathEmbbedWav, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
        
    # write length binary string in image
    file = open(pathEmbbedWav, "rb+")
    fileList = file.readlines()
    
    file.write(b"\n")
    file.write(state)
    file.write(b"\n")
    file.write(str.encode(byte_iter))
    file.close()

    song.close()

def decrypt(key, pathEmbbedWav, pathDestinationImage, pathExtractWav):
    song = wave.open(pathEmbbedWav, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # read music state
    file = open(pathEmbbedWav, "rb+")

    fileList = file.readlines()
    state = fileList[-1]
    state = list(str(state, 'utf-8'))
    len_text = len(state)

    # read image state
    state_img = fileList[-2]
    state_img = list(str(state_img, 'utf-8'))
    del state_img[-1]

    file.close()

    # Convert text to bit array
    key_list = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in key])))

    i = 0
    bits = ''
    wav_arr = []
    # process decode image
    m = len(state)-2
    k = (len_text % len(key_list))-1
    for j in range(len_text):
        # Write the hidden message into the least significant bit
        wav_arr.insert(0, (frame_bytes[0] ^ key_list[k]) & 0x01)
        # bits = bits + str((frame_bytes[0] ^ key_list[k]) & 0x01)
        frame_bytes[0] = (frame_bytes[0] & ~1) | int(state[m])
        
        i += 1
        k -= 1
        m -= 1
        # loop key
        if(k < 0):
            k = len(key_list)-1
    
    song.close()


    # convert bit array to list of int
    wav_arr = np.packbits(wav_arr, axis=-1)

    img_decode = cv2.imdecode(wav_arr, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(pathDestinationImage, img_decode)

    # write length binary string in image
    file = open(pathDestinationImage, "rb+")
    fileList = file.readlines()
    file.write(b"\n")
    file.write(str.encode(''.join(state_img)))
    file.close()

    # delete last line wav
    file = open(pathEmbbedWav, "rb+")
    fileList = file.readlines()
    lines = fileList[:-2]
    file.close()
    file = open(pathExtractWav, "wb+")
    file.writelines([item for item in lines])
    file.close()