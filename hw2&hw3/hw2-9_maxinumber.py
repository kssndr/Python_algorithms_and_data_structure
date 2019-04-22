# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.


def sx(a):
    if len(a)-1 == 0:
        return int(a)
    else:
        return int(a[len(a)-1]) + sx(a[:len(a) - 1])


print("определение наибольшего по сумме цифр. По окончанию ввода цифр нажмите 0\n")
num = 1
maxnum = 0
summax = 0
while num != "0":
    num = str(input("введите число: "))
    n = sx(num)
    if summax <= n:
        summax = n
        maxnum = num

print(f"Наибольшее число по сумме цифр {maxnum} - cумма цифр {summax}")

