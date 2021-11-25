from numba import jit
from matplotlib.image import imread
import numpy as np


def to_grayscale(image):
    image = imread(image)

    # Getting RGBs
    red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    # gamma and consts to transform to grayscale
    gamma = 1.400
    red_const, green_const, blue_const = 0.2126, 0.7152, 0.0722
    grayscale_image = (red_const * red ** gamma) + \
                      (green_const * green ** gamma) + \
                      (blue_const * blue ** gamma)

    return grayscale_image


@jit
def sobel_op(kernel, grayscale_image):
    [rows, columns] = np.shape(grayscale_image)
    sobel_image = np.zeros(shape=(rows, columns))

    for i in range(rows - 2):
        for j in range(columns - 2):
            sobel_image[i+1, j+1] = np.sum(np.multiply(kernel,
                                           grayscale_image[i:i + 3, j:j + 3]))
    return sobel_image
