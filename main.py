import cv2
import numpy as np
from math import sqrt

A = cv2.imread("/Users/cristofer/Downloads/valve.PNG", 0)


def convulution_transform(image):
    image_copy = image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image_copy[i][j] = image[image.shape[0]-i-1][image.shape[1]-j-1]
    return image_copy


def convolution(kernel, image):
    # kernel = convulution_transform(kernel)
    image_h = image.shape[0]
    image_w = image.shape[1]

    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    h = kernel_h // 2
    w = kernel_w // 2

    image_conv = np.zeros(image.shape)

    for i in range(h, image_h-h):
        for j in range(w, image_w-w):
            sum = 0

            for m in range(kernel_h):
                for n in range(kernel_w):
                    sum = (sum + kernel[m][n]*image[i-h+m][j-w+n])
            image_conv[i][j] = sum
    # cv2.imshow("Convolved image", image_conv)
    return image_conv


def norm(img1, img2):
    img_copy = np.zeros(img1.shape)  # image with initial zero values

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            q = sqrt(img1[i][j]**2 + img2[i][j]**2)
            if q > 120:
                img_copy[i][j] = 255
            else:
                img_copy[i][j] = 0
    return img_copy


kernel = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]], dtype="float64")

# gy = convolution(kernel, A)
# cv2.imshow("gradient_y", gy)
gy = np.sum(np.multiply(kernel, A))


kernel = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]], dtype="float64")
# gx = convolution(kernel, A)
# cv2.imshow("gradient_x", gx)
gx = np.sum(np.multiply(kernel, A))


g_sobel = norm(gx, gy)

cv2.imshow("Sobel_edge", g_sobel)
# g_sobel = convulution_transform(image)

cv2.imwrite("/Users/cristofer/Downloads/sobel.png", g_sobel)
# cv2.waitKey(0)
cv2.destroyAllWindows()