# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.
# Алгоритм:
# 1) Сортируемый массив разбивается на две части примерно одинакового размера;
# 2) Каждая из получившихся частей сортируется отдельно, например — тем же самым алгоритмом;
# 3) Два упорядоченных массива половинного размера соединяются в один.
# https://tproger.ru/translations/algoritms-rulling-world/

from random import randint
import timeit

# Модуль соединения двух отсортированных массивов
def arrays_merge(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:]
    c += b[j:]
    return c
    # if len(a) == len(b):
    #     l = len(a)
    #     last = 0
    # elif len(a) > len(b):
    #     l = len(b)
    #     last = a.pop()
    # elif len(a) < len(b):
    #     l = len(a)
    #     last = b.pop()
    # # print("m", a, b, last)
    # for i in range(l):
    #     if a[i] <= b[i]:
    #         c.append(a[i])
    #         # c.append(b[i])
    #     else:
    #         c.append(b[i])
    #         # c.append(a[i])
    # if last:
    #     c.append(last)
    # return c


# Модуль разделения массива
# Вторая попытка - добавил рекурсионный вызов
def array_split(array):
    print("array", array)
    if len(array) < 2:
        return array
    mid = int(len(array) / 2)
    first = array_split(array[:mid])
    second = array_split(array[mid:])
    return arrays_merge(first, second)


# Модуль сортировки массива
# вторая попытка - убрал этот модуль - сортирую через мерж
# def buble3(array):
#     for j in range(len(array)):
#         maximum = max(array[:len(array) - j])
#         array.remove(maximum)
#         array.insert(len(array) - j, maximum)
#     return array

# вторая попытка - убрал этот модуль - сортирую через мерж
# def array_sort(t):
#     a = t[0]
#     b = t[1]
#     buble3(a)
#     buble3(b)
#     return a, b


# Создание исходного массива
n = int(input("Введите размер массива: "))
m = [randint(0, 50) for i in range(n)]
print("Исходный массив: \n", m)

# Сортировка
print("Отсортированный массив: \n", array_split(m))
# print(array_sort(array_split(m)))
# print(arrays_merge(array_sort(array_split(m))))
# print(timeit.timeit("array_split(array)", setup="from __main__ import array_split", number=1000, globals={"array": m}))

# Результат не правильный - при повторяющихся цифрах массив не сортируется - добавляю рекурсию (без рекурсии, простым
# алгоритмом не работает)

