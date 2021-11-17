import threading
from math import sqrt

results = []  # memoria compartida


def cal_pi(li, ls, th_nums):
    pi_aprox = 0
    for k in range(li, ls+1, th_nums):
        pi_aprox += 6 / (k*k)

    results.append(pi_aprox)


n = 10_000_000
th_nums = 4
th_list = []
for _ in range(th_nums):
    th_list.append(threading.Thread(target=cal_pi, args=(1, n, th_nums)))
    th_list[-1].start()

for thread in th_list:
    thread.join()  # espera a que todos los hilos terminen

pi_aprox = sqrt(sum(results))
print(pi_aprox)
