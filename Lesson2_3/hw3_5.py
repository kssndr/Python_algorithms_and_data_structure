# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-100, 100) for i in range(20)]

min_a = min(a)
i = a.index(min_a)
min_a3 = 0
index = 0
index3 = 0
print(f"Максимально отрицательное число {min_a} на {i} месте в массиве {a}\n(первое решение)")
for i in range(len(a)):
    if a[i] == min_a:
        index = i
print(f"Максимально отрицательное число {min_a} на {index} месте в массиве {a}\n(второе решение)")
for i in range(len(a)):
    if a[i] <= min_a3:
        min_a3 = a[i]
        index3 = i
print(f"Максимально отрицательное число {min_a3} на {index3} месте в массиве {a}\n(третье решение)")
