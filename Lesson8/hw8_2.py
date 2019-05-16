# Закодировать любую строку по алгоритму Хаффмана.

# 1. вводим строку
# 2. создаем словарь с данными по буква: частота
# 3. создаем дерево по алгоритму Хаффмана
# 4. вывод дерева и таблицы буква: код

import random
from binarytree import Node
from binarytree import build

v = int(input("Сгенерировать строку автоматически или ввести вручную? (1/2) "))

if v == 1:
    n = int(input("Введите размер строки: "))
    source_string = ("".join([chr(random.randint(48, 52)) for i in range(n)]))
elif v == 2:
    source_string = (input("Введите строку: "))
    n = len(source_string)

print("*" * n, "\n", source_string, "\n", "*" * n)

ss = source_string

# 2. создаем словарь с данными по буква: частота
l_q = dict()
for i in range(len(ss)):
    q = 0
    for j in range(len(ss)):
        if ss[i] is not l_q and ss[i] == ss[j]:
            q += 1
    l_q[ss[i]] = q
print(l_q)
l_q_s = dict(sorted(l_q.items(), key=lambda x: x[1]))

# 3. создаем дерево по алгоритму Хаффмана


print("sorted dict", l_q_s)
k = l_q_s.keys()
v = l_q_s.values()
print("k", k)
print("v", v)
root = build(v)
print("root", root)
print("leaves", root.leaves)
