#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
'''
import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
