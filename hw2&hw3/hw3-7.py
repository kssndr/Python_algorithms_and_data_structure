# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

from random import randint

a = [randint(1, 100) for i in range(1, 20)]
b = sorted(a)
print(a)
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i] > a [j]:
            a[i], a[j] = a[j], a[i]

# print(a)
print("два наименьших элемента {} и {} (решение один)".format(a[0], a[1]))

# print(b)
print("два наименьших элемента {} и {} (решение два)".format(b[0], b[1]))