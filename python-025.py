#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘
'''
# 方法1
import math

s = 0
for i in range(1, 21):
    s = s + math.factorial(i)
print(s)

# 方法2
from functools import reduce

s = 0
for i in range(1, 21):
    s += reduce(lambda x, y: x * y, range(1, i + 1))
print(s)
