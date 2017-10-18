#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
'''
n = int(input('请输入行数:'))
for i in range(0, n):
    a = abs(i - int(n / 2))
    b = n - a
    print(' ' * a + '*' * (b - a))
