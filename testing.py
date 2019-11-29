import numpy
from skimage import io
import tensorflow as tf


# compare string
def compare_str():
    file = open("./text/plaintext.txt","r+")
    plaintext = file.read()
    file.close()

    file = open("./text/decryption.txt","r+")
    decrypt_text = file.read()
    file.close()
    return plaintext == decrypt_text

# compare img
def log10(x):
    numerator = tf.log(x)
    denominator = tf.log(tf.constant(10, dtype=numerator.dtype))
    return numerator / denominator

def psnr(im1, im2):
    img_arr1 = numpy.array(im1).astype('float32')
    img_arr2 = numpy.array(im2).astype('float32')
    mse = tf.reduce_mean(tf.squared_difference(img_arr1, img_arr2))
    psnr = tf.constant(255**2, dtype=tf.float32)/mse
    result = tf.constant(10, dtype=tf.float32)*log10(psnr)
    with tf.Session():
        result = result.eval()
    return result