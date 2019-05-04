# import collections
#
# de = collections.deque([1,2,3])
# # de.append(4)
# # de.appendleft(6)
# # de.popleft()
# # de.extend([4,5,6])
# # de.extendleft([4,5,6])
#
# print(de.reverse)


def abs123(q):
    l = len(q)
    for i in range(l):
        if q[i] == '5':
            print(q[i])
            q[i] = '10'
        elif q[i] == 'b':
            print(q[i])
            q[i] = 11
        elif q[i] == 'c':
            print(q[i])
            q[i] = 12
        elif q[i] == 'd':
            print(q[i])
            q[i] = 13
        elif q[i] == 'e':
            print(q[i])
            q[i] = 14
        elif q[i] == 'f':
            print(q[i])
            q[i] = 15
    print(q)
    return q

a = 'b3a5e'
b = '3df'
aa = list(a)
abs123(aa)
