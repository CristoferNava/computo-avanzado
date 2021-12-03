from mandelbrot import mandelbrot_set

width = int(input("Introduzca el ancho de la imagen en pixeles: "))
height = int(input("Introduzca el alto de la imagen en pixeles: "))
n_iters = int(input("Introduzca el número de iteraciones: "))

print("Procesando...")
mandelbrot_set(width, height, n_iters)
print("Listo!")
