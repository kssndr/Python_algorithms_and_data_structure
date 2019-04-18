# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def row(num):
    if num == 1:
        return 1
    return num + row(num - 1)


n = int(input("Введите натуральное число: "))
r2 = n * (n + 1)/2
r1 = row(n)
if r1 == r2:
    print(f"для числа {n} равенство 1+2+...+n = n(n+1)/2 верно. \n{r1} = {int(r2)}")
else:
    print(f"для числа {n} равенство 1+2+...+n = n(n+1)/2 не верно. \n{r1} != {int(r2)}")
