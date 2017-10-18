#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：给一个不多于5位的正整数，要求：
一、求它是几位数，二、逆序打印出各位数字。
'''

a = int(input('请输一个整数:'))
print('是一个%d位数' % len(str(a)))
b = int(str(a)[::-1])
print('逆序输出为：', b)
