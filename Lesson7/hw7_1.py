# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

from random import randint
import timeit
from memory_profiler import memory_usage

# Классический алгоритм пузырьковой сортировки
def buble_c(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            # print(n, i, array[i], array[i + 1])
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


# Сортировка во всем массиве сразу с использованием встроенной функции поиска максимального числа (ниже доработанный)
def buble1(array):
    for i in range(len(array)):
        for j in range(len(array[:len(array) - i])):
            maximum = max(array[:len(array) - i])
        array.remove(maximum)
        array.append(maximum)
    return array[::-1]


# Сортировка за один проход с использованием родных функций поиска максимального числа в массиве - удаляем найденное
# максималное число и вставляем его в конец списка, при возврате считываем массив в обратном порядке
def buble2(array):
    for j in range(len(array)):
        maximum = max(array[:len(array) - j])
        array.remove(maximum)
        array.append(maximum)
    return array[::-1]


# тоже самое что и предыдущий вариант, но вставляем максимальное число в начале списка, чтобы после сортировки список
# был в порядке возрастания
def buble3(array):
    for j in range(len(array)):
        maximum = max(array[:len(array) - j])
        array.remove(maximum)
        array.insert(len(array) - j, maximum)
    return array


# Сортировка встроенным методом sort
def buble4(array):
    array.sort()
    return array


# Сортировка однавременно с двух концов - влево минимальные числа, вправо - макисмальные (с использованием встроенных
# методов работы со списками - поиск min/max, удаление, вставка. Типа шейкерной сортировки получилось
def buble5(array):
    p = len(array)
    a = p
    if a % 2 != 0:
        array.append(555)
    j = 0
    while len(array[j:p - j]) > 0:
        p = len(array)
        maximum = max(array[j:p - j])
        minimum = min(array[j:p - j])
        array.remove(minimum)
        array.remove(maximum)
        array.insert(j, minimum)
        array.insert(p - j, maximum)
        j += 1
    if a % 2 != 0:
        array.remove(555)
    return array


# Сортировка однавременно с двух концов - влево минимальные числа, вправо - макисмальные без встроенных методов
def buble6(array):
    p = len(array)
    if p % 2 != 0:
        array.append(555)
    i = 0
    while len(array[i:p - i]) != 0:
        for j in range(p - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

        for k in range(p - i - 2):
            if array[p - k - 3] > array[p - k - 2]:  # and p - k - 3 > 0
                array[p - k - 2], array[p - k - 3] = array[p - k - 3], array[p - k - 2]

        i += 1

    if p % 2 != 0:
        array.remove(555)
    return array


def main():
    n = int(input("Введите размер массива: "))
    m = [randint(-100, 100) for i in range(n)]
    print(m)
    print("C: ", buble_c(m))
    print("1: ", buble1(m))
    print("2: ", buble2(m))
    print("3: ", buble3(m))
    print("4: ", buble4(m))
    print("5: ", buble5(m))
    print("6: ", buble5(m))

    print("C: ", timeit.timeit("buble_c(array)", setup="from __main__ import buble_c", number=1000, globals={"array": m}))
    print("1: ", timeit.timeit("buble1(array)", setup="from __main__ import buble1", number=1000, globals={"array": m}))
    print("2: ", timeit.timeit("buble2(array)", setup="from __main__ import buble2", number=1000, globals={"array": m}))
    print("3: ", timeit.timeit("buble3(array)", setup="from __main__ import buble3", number=1000, globals={"array": m}))
    print("4: ", timeit.timeit("buble4(array)", setup="from __main__ import buble4", number=1000, globals={"array": m}))
    print("5: ", timeit.timeit("buble5(array)", setup="from __main__ import buble5", number=1000, globals={"array": m}))
    print("6: ", timeit.timeit("buble6(array)", setup="from __main__ import buble6", number=1000, globals={"array": m}))
    print("использованно памяти", memory_usage())


if __name__ == "__main__":
    main()

# Самая быстра сортировка - сортировка встроенным методом sort, затем идут алгоритмы, в которых ипользовал встроенные
# методы работы со списками.
# использование insert замедляет программу(относительно метода append)
# Не смотря на уменьшения кол-во прогонов в два раза (в сортировке buble5), она оказалась медленнеею Предположительно
# из-за большо кол-ва вызова методов определения длины массива. сократил и результат улучшился но все равно медленнеей
# чем 3 вариант. Видимо инсерт и ремув тоже сильно тормозят алгоритм. при попытки избавиться от встроеных методов
# появился вариант 6. И все же самый быстрый - встроенный метод и второй это пузырьковый по всему массиву
