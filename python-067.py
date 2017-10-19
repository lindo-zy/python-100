'''
题目：输入数组，最大的与第一个元素交换，
最小的与最后一个元素交换，输出数组
'''
s = input('输入一个数组（空格分隔）').split()
L = sorted(list(s))
L[0], L[len(s) - 1] = L[len(s) - 1], L[0]
print(L)
