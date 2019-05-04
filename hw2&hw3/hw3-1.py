# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import random

a = [int(i + 1) for i in range(1, 99)]
for i in range(2, 10):
    c = 0
    for j in a:
        if j % i == 0:
            c += 1
    print(i, c)


