'''
题目：从键盘输入一些字符，
逐个把它们写到磁盘文件上，直到输入一个 # 为止。
'''
filename=input('请输入文件名：')
f=open(filename,'w+')
ch=''
while '#' not in ch:
    f.write(ch)
    ch=input('输入写入内容：')
f.close()