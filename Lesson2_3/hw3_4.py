# 4. Определить, какое число в массиве встречается чаще всего.

import random

a = [random.randint(1, 5) for i in range(10)]
print(a)
print("Число {} встречается {} раз(первое решение)".format(max(set(a), key=a.count), a.count(max(set(a), key=a.count))))
c = 0
cc = 0
max_c_num = 0
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c += 1
    if c >= cc:
        max_c_num = a[i]
        cc = c
print("Число {} встречается {} раз(втрое решение)".format(max_c_num, cc))
