#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
'''
def Rabbit(num):
    i = 1
    a, b = 1, 1
    while i <= num:
        yield a
        i += 1
        a, b = b, a + b
month = int(input('输入几个月：'))
list = [x for x in Rabbit(month)]
print('第%d个月，有%s只兔子' % (month, list[month - 1]))