import cv2
import numpy as np
import matplotlib.pyplot as plt

import pywt


path = "./image/image.bmp"
typeImage = path.split(".")

# resize image
def resize_img():
    width = 200
    height = 200
    image = cv2.imread(path)
    resized_image = cv2.resize(image, (width, height))

    cv2.imwrite("./image/image_resize." + str(typeImage[-1]), resized_image)

# rgb to grayscale
def rgb_to_gray(value = False):
    path1 = "./image/image_resize." + str(typeImage[-1])
    image = cv2.imread(path1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite("./image/grayscale." + str(typeImage[-1]), gray)
    
    if (value == True):
        return gray
    
# haar wavelet
def haar_wave():
    image = rgb_to_gray(True)
    cv2.imshow("Image", image)

    # Convert to float for more resolution for use with pywt
    image = np.float32(image)
    image /= 255
    
    coeffs = pywt.dwt2(image, 'haar', 'smooth')
    LL, (LH, HL, HH) = coeffs

    # Convert back to uint8 OpenCV format
    LL *= 255
    LL = np.uint8(LL)

    cv2.imshow("LL Image", LL)
    cv2.waitKey(0)
    cv2.destroyAllWindows()