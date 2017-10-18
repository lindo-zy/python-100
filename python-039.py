#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：有一个已经排好序的数组。
现输入一个数，要求按原来的规律将它插入数组中

程序分析：首先判断此数是否大于最后一个数，
然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
'''
#方法1
L = [1, 2, 3, 4, 5]
a = 2
if a >= L[len(L) - 1]:
    L.append(a)
    print(L)
elif a <= L[0]:
    L.insert(0, a)
    print(L)
else:
    for i in range(2, len(L) - 1):
        if a >= i and a <= i + 1:
            L.insert(i, a)
            print(L)

#方法2
L=[1,3,5,7,8]
a=2
L.append(a)
L.sort()
print(L)
