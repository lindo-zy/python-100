#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：对5个数进行排序
'''
s = input('输入5个数字(空格分隔):').split()
L = []
for i in s:
    L.append(i)
L.sort()
print(L)
