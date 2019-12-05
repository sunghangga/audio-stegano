import math
import numpy as np
from skimage import io
import tensorflow as tf


def mse(var1, var2):
    var1 = np.array(var1, dtype=np.float64)
    var2 = np.array(var2, dtype=np.float64)
    mse = np.mean((var1 - var2)**2)

    return mse

def psnr(var1, var2):
    var1 = np.array(var1, dtype=np.float64)
    var2 = np.array(var2, dtype=np.float64)

    mse = np.mean((var1 - var2)**2)
    if mse == 0:
        return float('inf')
        
    psnr = 20 * math.log10(255.0 / math.sqrt(mse))
    return psnr