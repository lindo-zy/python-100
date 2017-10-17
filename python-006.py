#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
fn=f(n-1)+f(n-2)
'''
def Fib(n):
    a, b = 0, 1
    while n:
        a, b, n = b, a + b, n - 1
        print(a)
Fib(10)
