# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из
# примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections (пусть это и не
# # очевидно с первого раза. Вы же не Голландец ;-).
# Алгоритм:
# 1) принимаем вводимые числа как строки
# 2) сохраняем их как массивы
# 3) реверсируем их для сложения
# 4) складываем через цикл, занося сумму в новый массив
# 5) реверсируем массив с суммой обратно и выводим через цикл
# 6) умножаем через цикл, занося произведение в новый массив
# 7) выводим результат
#

import collections


def abs123(q):
    for i in range(len(q)):
        if q[i] == 'a':
            q[i] = 10
        elif q[i] == 'b':
            q[i] = 11
        elif q[i] == 'c':
            q[i] = 12
        elif q[i] == 'd':
            q[i] = 13
        elif q[i] == 'e':
            q[i] = 14
        elif q[i] == 'f':
            q[i] = 15
    return q


def to16(s):
    for i in range(len(s)):
        if s[i] == 10:
            s[i] = 'a'
        elif s[i] == 11:
            s[i] = 'b'
        elif s[i] == 12:
            s[i] = 'c'
        elif s[i] == 13:
            s[i] = 'd'
        elif s[i] == 14:
            s[i] = 'e'
        elif s[i] == 15:
            s[i] = 'f'
    return s


def sum16(x, y):
    z = []
    xx = abs123(x[::-1])
    yy = abs123(y[::-1])
    if len(xx) >= len(yy):
        for i in range(len(xx) - len(yy)):
            yy.append(0)
    else:
        for i in range(len(yy) - len(xx)):
            xx.append(0)
    p, zz, zzz = 0, 0, 0
    for i in range(len(xx)):
        zz = int(xx[i]) + int(yy[i]) + p
        if zz >= 16:
            p = zz // 16
            zzz = zz % 16
        else:
            zzz = zz
            p = 0
        z.append(zzz)
    if p > 0:
        z.append(p)
    # print(z, to16(z[::-1]))
    return to16(z[::-1])


def to10(x):
    xx = abs123(x)
    tenn = 0
    for i in range(len(xx)):
        ll = len(xx) - i - 1
        s = 16 ** ll
        ten = int(xx[i]) * s
        tenn += ten
    return tenn


a = input("\nВведите первое число в 16 формате: ")
b = input("Введите второе число в 16 формате: ")
# a = 'ff'
# b = 'fffff'
aa = list(a)
bb = list(b)

sum = sum16(aa, bb)

print(f"\nСумма чисел {a} и {b}:")
for i in sum:
    print(i, end="")

print()
# print("bb", to10(bb), "aa", to10(aa))

dd = aa
for i in range(to10(bb)-1):
    dd = sum16(aa, dd)

print(f"\nПроизведение чисел {a} и {b}:")
for i in dd:
    print(i, end="")
print(f"\n\nцифры в десятичном формате:\na = {to10(aa)}\nb = {to10(bb)}\nsum = {to10(sum)}\nmul = {to10(dd)}")
