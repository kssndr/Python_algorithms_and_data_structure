
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

print("Ex.1")
num = int(input('add 3 digit number: '))
n1 = num // 100
n2 = (num - n1 * 100) // 10
n3 = num - n1 * 100 - n2 * 10
sum = n1 + n2 + n3
mul = n1 * n2 * n3
print('The sum of the digits = {}, product = {}'.format(sum, mul))


# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
#

print('Ex.2')