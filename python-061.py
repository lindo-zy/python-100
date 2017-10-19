'''
题目：打印出杨辉三角形（要求打印出10行)
'''


# 方法1
def sj():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
n = 0
for i in sj():
    print(i)
    n += 1
    if n == 10:
        break


# 方法2
def triangles():
    T = [1]
    while True:
        yield T
        T = [(T + [0])[i] + ([0] + T)[i] for i in range(len(T + [0]))]
n = 0
for i in triangles():
    print(i)
    n += 1
    if n == 10:
        break
