# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена


import timeit


def natur(ff: int):
    s = []
    for i in range(1, ff + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            s.append(i)


a = int(input())
natur(a)

print(timeit.timeit("natur(ff)", setup="from __main__ import natur", number=1, globals={"ff": ff}))

