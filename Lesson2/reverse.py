# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, то надо вывести число 6843.
#

#
# def reverse(num):
#     i = len(num)-1
#     r = ''
#     while i >= 0:
#         r += num[i]
#         print(num[i], end="")
#         i -= 1
#     return r
#
#
# n = input()
#
# print(reverse(n))


def reverse(num):
    if len(num)-1 == 0:
        return num
    return num[len(num)-1] + reverse(num[:len(num)-1])


n = str(input())
print(reverse(n))
