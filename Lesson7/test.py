import cProfile


def main():
    array = [8, 7, 6, 5, 4, 3, 2, 1, 0]
    print("   ",array)
    p = len(array)
    a = p
    if a % 2 != 0:
        array.append(555)
    i = 0
    while len(array[i:p - i]) != 0:
        # p = len(array[i:p - i])
        # j = i
        # print("p", p, array)
        for j in range(p - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            # print("f", j, array, array[i:p - i])
        # k = i
        # print("k", k)
        for k in range(p - i - 2):
            # print(k, array[p - k - 3], array[p - k - 2])
            if array[p - k - 3] > array[p - k - 2]: # and p - k - 3 > 0
                array[p - k - 2], array[p - k - 3] = array[p - k - 3], array[p - k - 2]
            # print("r", k,  array, array[i:p - i])
        i += 1
        # print('c', i)

    if a % 2 != 0:
        array.remove(555)
    print(array)

main()

cProfile.run('main()')

