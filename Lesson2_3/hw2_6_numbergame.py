# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что
# загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random


def wc(a, b):
    if b < a:
        return print("загаданное число больше")
    return print("загаданное число меньше")


n = random.randint(0, 100)
p = 1
while p <= 10:
    o = int(input("отгадайте число: "))
    if o == n:
        print("Вы отгадали!")
    else:
        wc(n, o)
    p += 1

print(f"Было загадано число {n}")

