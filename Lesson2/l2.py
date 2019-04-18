# # Akcerman function
# def rec(m, n):
#     if m == 0:
#         return n+1
#     elif n == 0 and m > 0:
#         return rec(m-1, 1)
#     else:
#         return rec(m-1, rec(m, n-1))
#
#
# print(rec(4, 0))
#
#
# # Evklid function
# def nod(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
#
#
# print(nod(234, 43434))
#
# # Evklid function
#
#
# def nod(a, b):
#     if b == 0:
#         return a
#     else:
#         return nod(b, a % b)
#
#
# print(nod(2344344, 43434))
#
#
# num = 44
# s = ''
# while num != 0:
#     s = str(num % 2) + s
#     num //= 2
#
# print(s)

#
# def r(n):
#     if n == 1:
#         return "1"
#     else:
#         return r(n-1) + " " + n
#
# print(r(3))
#

#
# def print10(n):
#     if n < 11:
#         # print10(n + 1)
#         print(n, sep=" ", end=" ")
#         # print10(n - 1)
#         print10(n + 1)
#
#
# print10(1)


# def pow(n):
#
#     if n == 1:
#         return 1
#     return n + pow(n-1)
#
# print(pow(3))

# Даны два целых числа A и В (каждое в отдельной строке). Выведите все числа от A до B включительно, в порядке
# возрастания, если A < B, или в порядке убывания в противном случае.
#
# def row(a, b):
#     if a < b:
#         return str(a) + " " + row(a + 1, b)
#     else:
#         if a == b:
#             return str(a) + " "
#         return str(a) + " " + row(a - 1, b)
#
#
# s = 10
# d = 5
# print(row(s, d))


def row(a, b):
    print(a, end=" ")
    if a < b:
        row(a + 1, b)
    elif a > b:
        row(a - 1, b)


s = 10
d = 5
row(s, d)

