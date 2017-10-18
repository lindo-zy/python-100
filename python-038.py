#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：求一个3*3矩阵对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = 0
for i in range(0, 3):
    s += matrix[i][i]
print(s)
