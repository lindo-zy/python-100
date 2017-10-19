'''
题目：有两个磁盘文件A和B,各存放一行字母,
要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
'''
f1 = open('A.txt')
a = f1.read()
f1.close()
f2 = open('B.txt')
b = f2.read()
f2.close()
f3 = open('C.txt', 'w+')
f3.write(a + b)
f3.close()
