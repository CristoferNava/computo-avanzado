from types import FunctionType
import numpy as np
import time


def trapecio(f, a, b, n):
    h = (b-a) / n

    sum1 = (f(a) + f(b)) / 2
    sum2 = 0

    for k in range(1, n):
        sum2 += f(a + k*h)

    return h * (sum1 + sum2)


def trapecioNumpy(f, a, b, n):
    h = (b-a) / n
    sum1 = (f(a) + f(b)) / 2

    vector = np.array([f(a + k*h) for k in range(1, n)])
    sum2 = vector.sum()

    return h * (sum1 + sum2)


def trapecioNumpy2(f, a, b, n):
    h = (b-a) / n
    sum1 = (f(a) + f(b)) / 2

    vector = np.array([f(a + k*h) for k in np.arange(1, n)])
    sum2 = vector.sum()

    return h * (sum1 + sum2)


def trapecioNumpy3(f, a, b, n):
    h = (b-a)/n
    values = a + (np.arange(1, n) * h)
    values = np.array([f(x) for x in values])
    fa = f(a)
    fb = f(b)
    value = h * ((fa+fb)/2 + np.sum(values))
    return value


# Valores de entrada de las funciones
def f(x): return 3*x


a = 0
b = 2
n = 6

# Medición de los tiempos
start = time.time()
result1 = trapecio(f, a, b, n)
end = time.time() - start
print(end)

start = time.time()
result2 = trapecioNumpy(f, a, b, n)
end = time.time() - start
print(end)

start = time.time()
result3 = trapecioNumpy2(f, a, b, n)
end = time.time() - start
print(end)

start = time.time()
result4 = trapecioNumpy3(f, a, b, n)
end = time.time() - start
print(end)
