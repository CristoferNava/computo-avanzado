from PIL import Image
import numpy as np
import colorsys


def color_period(n: int):
    """ Associates a color to the integer n"""
    color = 255 * np.array(colorsys.hsv_to_rgb(n / 255.0, 1.0, 1.0))
    return tuple(color.astype(int))


def mandelbrot(c: complex, n_iters: int):
    z = 0
    for i in range(1, n_iters):
        # if z diverges it leaves the circle of radius 2 in the complex plane
        # so it does not belong to the Mandelbrot set
        if abs(z) > 2:
            return color_period(i)
        z = z * z + c
    return (0, 0, 0)  # it belongs to Mandelbrot's set


def mandelbrot_set(width: int, height: int, n_iters: int):
    # creates the image in RGB
    image = Image.new('RGB', (width, height))
    pixels = image.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            # converts pixel coordinate to complex number
            c = complex((x - (0.75 * width)) / (width / 4),
                        (y - (width / 4)) / (width / 4))
            pixels[x, y] = mandelbrot(c, n_iters)

    image.save("/Users/cristofer/Desktop/mandelbrot.png")
