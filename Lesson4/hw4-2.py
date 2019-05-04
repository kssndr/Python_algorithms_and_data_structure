# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена


import timeit
import cProfile
# нахождение простых числе через перебор делителей


def natur(f):
    s = []
    for i in range(2, f + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            s.append(i)
    return s


# нахождение через решето
def erat(f):
    s = []
    e = [int(i) for i in range(2, f + 1)]
    num = 2  # установка первого простого числа
    n = 2
    for i in range(1, len(e)):  # запуск перебора чисел
        while n <= f:  # запуск цикла перебора чисел кратных простому
            for j in range(i+1, len(e)):  # проверка на кратность
                if e[j] == n:
                    e[j] = 0  # "прокол" числа, кратного взятому простому числу
                    break  # остановка прогона, после нахождения
                elif e[j] > n:
                    break  # остановка прогона, после прохождения установленного числа для проверки кратности
            n += num  # установка следующего кратного числа
        if e[i] > num:  # поиск оставшегося в решете числа, после цикла удаления кратных чисел по предудущему простому числу
            num = e[i]
            n = num
    for i in e:  # создание списка простых чисел в заданном диапозоне
        if i > 0:
            s.append(i)
    return s


def main():
    f = int(input())
    print(natur(f))
    print(timeit.timeit("natur(f)", setup="from __main__ import natur", number=1, globals={"f": f}))
    print(erat(f))
    print(timeit.timeit("erat(f)", setup="from __main__ import erat", number=1, globals={"f": f}))


main()

cProfile.run("main()")




