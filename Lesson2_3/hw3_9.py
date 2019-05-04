# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

m, n = [int(i) for i in input("введите размер матрицы M x N: ").split()]
b = []
for i in range(m):
    a = [randint(0, 100) for i in range(n)]
    b.append(a)
s = []
for i in range(m):
    for j in range(1, n):
        j_min = b[i][j]
        if b[i][j] < j_min:
            j_min = b[i][j]
        s.append(j_min)

for row in b:
    print(" ".join([str(el) for el in row]))
print(f"\n{max(s)} - это максимальный элемент среди минимальных элементов столбцов матрицы ")
