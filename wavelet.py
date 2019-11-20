import pywt
import numpy as np
import cv2


path = "./image/image.bmp"

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

def coeffs_visualization(cof):
    norm_cof0 = cof[0]
    norm_cof0 = image_normalization(norm_cof0) # OK even if removed
    merge = norm_cof0
    for i in range(1, len(cof)):
        merge = merge_images(merge, cof[i])  # Combine four images
    cv2.imshow('', merge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def coeffs_visual_transform(cof):
    LL, (LH, HL, HH) = cof
    cv2.imshow ("LL", image_normalization(LL))
    cv2.imshow ("LH", image_normalization(LH))
    cv2.imshow ("HL", image_normalization(HL))
    cv2.imshow ("HH", image_normalization(HH))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def wavelet_transform_for_image(src_image, level, M_WAVELET="db1", mode="sym"):
    data = src_image.astype(np.float64)
    coeffs = pywt.wavedec2(data, M_WAVELET, level=level, mode=mode)
    return coeffs

def wavelet_image(write = False, show = False):
    filename = "./image/image_resize.bmp"
    LEVEL = 1

    # 'haar', 'db', 'sym' etc...
    # URL: http://pywavelets.readthedocs.io/en/latest/ref/wavelets.html
    MOTHER_WAVELET = "haar"

    im = cv2.imread(filename)

    # print('LEVEL :', LEVEL)
    # print('MOTHER_WAVELET', MOTHER_WAVELET)
    # print('original image size: ', im.shape)

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
        coeffs_visual_transform(coeffs_B)

# resize image
def resize_img():
    width = 200
    height = 200
    image = cv2.imread(path)
    resized_image = cv2.resize(image, (width, height))

    cv2.imwrite("./image/image_resize." + str(typeImage[-1]), resized_image)