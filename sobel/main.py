import matplotlib.pyplot as plt
import numpy as np
import multiprocessing as mp
from sobel import to_grayscale, sobel_op


image = "/Users/cristofer/Downloads/woman.jpeg"
dst_path = "/Users/cristofer/Downloads/sobel.png"

if __name__ == "__main__":
    # Kernels and image declaration
    kernel_x = np.array([
        [1.0, 0.0, -1.0],
        [2.0, 0.0, -2.0],
        [1.0, 0.0, -1.0]])

    kernel_y = np.array([
        [1.0, 2.0, 1.0],
        [0.0, 0.0, 0.0],
        [-1.0, -2.0, -1.0]])

    kernels = [kernel_x, kernel_y]
    grayscale_image = to_grayscale(image)

    # Multiprocessing
    pool = mp.Pool(2)
    results = [pool.apply_async(sobel_op, (kernel, grayscale_image))
               for kernel in kernels]
    pool.close()

    # Get the results of the multiprocessing and build the image
    Gx = results[0].get()
    Gy = results[1].get()
    sobel_image = np.hypot(Gx, Gy)
    sobel_image = sobel_image / np.max(sobel_image)

    plt.imsave(dst_path, sobel_image, cmap=plt.get_cmap('gray'))
