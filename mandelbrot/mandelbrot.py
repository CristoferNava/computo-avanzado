from PIL import Image
import numpy as np
import colorsys


def color_period(n: int):
    """ Associates a color to the integer n"""
    color = 255 * np.array(colorsys.hsv_to_rgb(n / 255.0, 1.0, 1.0))
    return tuple(color.astype(int))


def mandelbrot(x: int, y: int, n_iters: int):
    """ 
    Z_0 = 0 + 0i
    Z_N+1 = Z_N^2 + C 
    a cada pixel le corresponde un número complejo C
    """

    z_0 = complex(x, y)
    z = 0
    for i in range(1, n_iters):
        # if z diverges it leaves the circle of radius 2 in the complex plane
        # so it does not belong to the Mandelbrot set
        if abs(z) > 2:
            return color_period(i)
        z = z * z + z_0
    return (0, 0, 0)  # it belongs to Mandelbrot's set


def mandelbrot_set(width: int, height: int, n_iters: int):
    # creates the image in RGB
    img = Image.new('RGB', (width, height))
    pixels = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixels[x, y] = mandelbrot(x=(x - (0.75 * width)) / (width / 4),
                                      y=(y - (width / 4)) / (width / 4),
                                      n_iters=n_iters)

    img.show()
