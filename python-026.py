#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：利用递归方法求5!。
程序分析：递归公式：fn=(fk)*4!    5!=5*4!

'''


def Factorial(n):
    if n == 1:
        fn = 1
    else:
        fn = n * Factorial(n - 1)
    return fn
print(Factorial(5))
