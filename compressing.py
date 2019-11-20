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

def image_normalization(src_img):
    """
    Normalization processing to prevent overexposure
    Necessary when displaying wavelet converted images with cv2.imshow (only for images with large values)
    """
    norm_img = (src_img - np.min(src_img)) / (np.max(src_img) - np.min(src_img))
    return norm_img

# haar wavelet
def haar_wave():
    image = rgb_to_gray(True)

    # Convert to float for more resolution for use with pywt
    image = np.float64(image)
    image /= 255
    
    coeffs = pywt.dwt2(image, 'haar', 'smooth')
    LL, (LH, HL, HH) = coeffs

    # Convert back to uint8 OpenCV format
    LL = image_normalization(LL)
    LL *= 255
    LL = np.uint8(LL)

    cv2.imshow("LL Image", LL)
    cv2.imwrite("./image/test.bmp", LL)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

haar_wave()