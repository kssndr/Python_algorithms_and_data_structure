# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = [random.randint(1, 100) for i in range(1, 20)]
a_max = max(a)
a_min = min(a)
min_i = a.index(a_min)
max_i = a.index(a_max)
sum = 0

if min_i < max_i:
    for i in range(min_i+1, max_i):
        print(a[i])
        sum += a[i]
else:
    for i in range(max_i+1, min_i):
        print(a[i])
        sum += a[i]
print(f"\nсумму элементов {sum}, находящихся между минимальным {a_min} и максимальным {a_max} элементами\n массива {a}")
