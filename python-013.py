#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：
'''
start, end = input('请输入范围（空格分隔）：').split()
sum = 0
for num in range(int(start), int(end)):
    n = len(str(num))
    for i in str(num):
        sum = sum + int(i) ** n
    if num == sum:
        print(num)
    sum = 0
