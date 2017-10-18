#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：将一个数组逆序输出。
程序分析：用第一个与最后一个交换。
'''
#方法1
L=[1,2,3,4]
S=L[::-1]
print(S)

#方法2
L=[1,2,3,4]
L.reverse()
print(L)