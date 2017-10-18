#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
'''


def output(S, L):
    if L == 0:
        return
    print(S[L - 1])
    output(S, L - 1)


S = input('input a string:')
L = len(S)
output(S, L)
