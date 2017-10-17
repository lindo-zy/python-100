#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
题目：暂停一秒输出，并格式化当前时间。
'''
import time

time.sleep(1)
date = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', date))
