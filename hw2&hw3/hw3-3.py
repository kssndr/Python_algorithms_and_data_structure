# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(1, 100) for i in range(1, 20)]
a_max = max(a)
a_min = min(a)
print(a, "\n", a_max, "\n", a_min)
for i in range(len(a)):
    if a[i] == a_max:
        a[i] = a_min
    elif a[i] == a_min:
        a[i] = a_max

print(a)
