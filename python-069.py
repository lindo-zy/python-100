'''
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''
n = int(input('请输入人数n：'))
a = [i for i in range(1, n + 1)]
print(a)
i = 1
while len(a) > 1:
    if i % 3 == 0:
        a.pop(0)
    else:
        a.insert(len(a), a.pop(0))
    i += 1
print(a)