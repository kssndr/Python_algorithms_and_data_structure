# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена


import timeit


def nat(n):
    for i in range(1, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)



print(timeit.timeit("nat(20)", setup="from __main__ import nat", number=100))
