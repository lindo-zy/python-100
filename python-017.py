#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n
'''
import re

s = input('input a string：\n')
r1 = re.compile('[a-zA-Z]')
r2 = re.compile('[0-9]')
print('英文个数为：%d' % len(re.findall(r1, s)))
print('数字个数为：%d' % len(re.findall(r2, s)))
print('空格个数为:%d' % len(re.findall(' ', s)))
print('其他字符个数为%d:' %(len(s) - len(re.findall(r1, s)) - len(re.findall(r2, s)) - len(re.findall(' ', s))))
