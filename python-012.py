#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
题目：判断101-200之间有多少个素数，并输出所有素数
'''
def is_Prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
count = 0
for i in range(101, 200):
    if is_Prime(i):
        count = count + 1
        print('{}:{}'.format(count, i))