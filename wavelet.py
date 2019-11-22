import pywt
import numpy as np
import cv2

import imghdr


path = "./image/image.bmp"
typeImage = path.split(".")

def image_normalization(src_img):
    """
    Normalization processing to prevent overexposure
    Necessary when displaying wavelet converted images with cv2.imshow (only for images with large values)
    """
    norm_img = (src_img - np.min(src_img)) / (np.max(src_img) - np.min(src_img))
    return norm_img

def merge_images(cA, cH_V_D):
    """Concatenate four numpy.array (upper left, (upper right, lower left, lower right))"""
    cH, cV, cD = cH_V_D
    cH = image_normalization(cH) # OK even if removed
    cV = image_normalization(cV) # OK even if removed
    cD = image_normalization(cD) # OK even if removed
    cA = cA[0:cH.shape[0], 0:cV.shape[1]] # If the original image is not a power of 2, it may be rounded, so the size is matched. Match the smaller one

    return np.vstack((np.hstack((cA,cH)), np.hstack((cV, cD)))) # Attach pixels at upper left, upper right, lower left, lower right

# show image in single window
def coeffs_visualization(cof):
    norm_cof0 = cof[0]
    norm_cof0 = image_normalization(norm_cof0) # OK even if removed
    merge = norm_cof0
    for i in range(1, len(cof)):
        merge = merge_images(merge, cof[i])  # Combine four images

    cv2.imshow('', merge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Convert back to uint8 OpenCV format
def normalization_image_uint8(image):
    image = image_normalization(image)
    image *= 255
    image = np.uint8(image)
    return image

# show image with many window
def coeffs_visual_haar_transform(cof):
    LH, HL, HH = cof[1]

    cv2.imshow ("LL", normalization_image_uint8(cof[0]))
    cv2.imshow ("LH", normalization_image_uint8(LH))
    cv2.imshow ("HL", normalization_image_uint8(HL))
    cv2.imshow ("HH", normalization_image_uint8(HH))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def write_image(cof, wave_name, level):
    LH, HL, HH = cof[1]

    cv2.imwrite("./image/LL_" + str(wave_name) + "_" + str(level) + "." + str(typeImage[-1]), normalization_image_uint8(cof[0]))
    cv2.imwrite("./image/LH_" + str(wave_name) + "_" + str(level) + "." + str(typeImage[-1]), normalization_image_uint8(LH))
    cv2.imwrite("./image/HL_" + str(wave_name) + "_" + str(level) + "." + str(typeImage[-1]), normalization_image_uint8(HL))
    cv2.imwrite("./image/HH_" + str(wave_name) + "_" + str(level) + "." + str(typeImage[-1]), normalization_image_uint8(HH))

def wavelet_transform_for_image(src_image, level, M_WAVELET="db1", mode="sym"):
    data = src_image.astype(np.float64)
    coeffs = pywt.wavedec2(data, M_WAVELET, level=level, mode=mode)
    return coeffs

def wavelet_image(level, write = False, show = False):
    filename = "./image/image_resize.bmp"
    LEVEL = level

    # 'haar', 'db', 'sym' etc...
    # URL: http://pywavelets.readthedocs.io/en/latest/ref/wavelets.html
    MOTHER_WAVELET = "haar"

    im = cv2.imread(filename)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    """
    Conversion for each BGR channel
    Note that cv2.imread spits out images in the order of B, G, R
    """
    B = 0
    G = 1
    R = 2
    coeffs_B = wavelet_transform_for_image(im[:, :, B], LEVEL, M_WAVELET=MOTHER_WAVELET)
    coeffs_G = wavelet_transform_for_image(im[:, :, G], LEVEL, M_WAVELET=MOTHER_WAVELET)
    coeffs_R = wavelet_transform_for_image(im[:, :, R], LEVEL, M_WAVELET=MOTHER_WAVELET)


    # coeffs_visualization(coeffs_B)
    # coeffs_visualization(coeffs_G)
    # coeffs_visualization(coeffs_R)

    if(show == True):
        # coeffs_visual_haar_transform(coeffs_B)
        coeffs_visualization(coeffs_B)
    if(write == True):
        write_image(coeffs_B, MOTHER_WAVELET, LEVEL)


    # testing
    # 1
    # LL, (LH, HL, HH) = coeffs_B
    # print(im)
    # print(coeffs_B[0])
    # print(normalization_image_uint8(coeffs_B[0]))

    # im = cv2.imread("./image/LL_haar_1.bmp")
    # print(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY))

    # print(np.array_equal(normalization_image_uint8(coeffs_B[0]),cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)))

    # 2
    # LL, (LH, HL, HH) = coeffs_B
    # cof = LL, (LH, HL, HH)
    # cofRec = pywt.waverec2(cof, "haar")
    # A = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # B = cofRec.astype(np.int64)

    # print(A)
    # print(B)
    # print(np.array_equal(A,B))


# resize image
def resize_img():
    width = 200
    height = 200
    image = cv2.imread(path)
    resized_image = cv2.resize(image, (width, height))

    cv2.imwrite("./image/image_resize." + str(typeImage[-1]), resized_image)