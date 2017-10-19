'''
题目：求0-7所能组成的奇数个数。

'''
def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 7
    else:
        return f(n-1)*8
l = []
#算出每位数有多少奇数
for i in range(1,9):
    l.append(f(i-1)*4)
print(l)
#输出一共有多少个奇数
print(sum(l))

