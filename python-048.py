'''
题目：数字比较
'''
i = 10
j = 20
d = i - j
if d > 0:
    print('%d 大于 %d ' % (i, j))
elif d == 0:
    print('%d 等于 %d ' % (i, j))
elif d < 0:
    print('%d 小于 %d' % (i, j))
