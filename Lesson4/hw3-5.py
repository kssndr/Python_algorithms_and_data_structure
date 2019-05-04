# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
import timeit

# решение через встроенные функции
def aut(f):
    min_a = min(f)
    i = f.index(min_a)
    # print(f"Максимально отрицательное число {min_a} на {i} месте в массиве {f}\n(первое решение)")


def grey(g):  # решение с использоанием встроенных функций и цикла
    index = 0
    min_a = min(g)
    for i in range(len(g)):
        if g[i] == min_a:
            index = i
    # print(f"Максимально отрицательное число {min_a} на {index} месте в массиве {g}\n(второе решение)")


def man(m):  # решение ручное
    min_a3 = 0
    index3 = 0
    for i in range(len(m)):
        if m[i] <= min_a3:
            min_a3 = m[i]
            index3 = i
    # print(f"Максимально отрицательное число {min_a3} на {index3} месте в массиве {m}\n(третье решение)")


aa = int(input("введите размер массива "))

a = [random.randint(-100, 100) for i in range(aa)]
# print(a)

print(timeit.timeit("aut(a)", setup="from __main__ import aut", number=10000, globals={"a": a}))
print(timeit.timeit("grey(a)", setup="from __main__ import grey", number=10000, globals={"a": a}))
print(timeit.timeit("man(a)", setup="from __main__ import man", number=10000, globals={"a": a}))


# https://www.yuripetrov.ru/edu/python/ch_06_01.html
