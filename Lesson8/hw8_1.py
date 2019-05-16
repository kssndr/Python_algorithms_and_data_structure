# Определить количество различных подстрок с использованием хеш-функции. Задача: на вход функции дана строка, требуется
# вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

# Алгоритм решения:
# 0. С помощью рандома создадим строку
# 1. Создадим двойной цикл по строке перебирать все варианты
# 2. Каждый результат переборов будем прогонять через Хэш-функцию и результаты сохарнять в массив-множество
# 3. Возврат размера множества и будет показывать кол-во различных подстрок

import hashlib
import random

v = int(input("Сгенерировать строку автоматически или ввести вручную? (1/2) "))

if v == 1:
    n = int(input("Введите размер строки: "))
    source_string = ("".join([chr(random.randint(48, 52)) for i in range(n)]))
elif v == 2:
    source_string = (input("Введите строку: "))
    n = len(source_string)
# elif v = int(input("Сгенерировать строку автоматически или ввести вручную? (1/2)"))

print("*" * n, "\n", source_string, "\n", "*" * n)
ss = source_string
many_substrings = set()
for i in range(1, len(ss)):
    for j in range(i, len(ss)):
        hash_ss = hashlib.sha1(ss[i:j].encode('utf-8')).hexdigest()
        many_substrings.add(hash_ss)
print("Кол-во различных подстрок: ", len(many_substrings))
# for i in many_substrings:
#     print(i)
