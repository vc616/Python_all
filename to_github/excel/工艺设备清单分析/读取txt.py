#encoding=utf-8
import  os
print(os.getcwd()) #获取当前工作目录路径
print(os.path.abspath('.') )#获取当前工作目录路径
print (os.path.abspath('test.txt') )#获取当前目录文件下的工作目录路径
print (os.path.abspath('..')) #获取当前工作的父目录 ！注意是父目录路径
print (os.path.abspath(os.curdir)) #获取当前工作目录路径


f = open("C:\\Users\\vc\\Code_Python\\python_all\\to_github\\excel\\工艺设备清单分析\\set.txt",encoding='UTF-8')
s = f.readlines()
p = {}
for i in s:
    print(i)
    i = i.replace(" ","")
    if i.startswith("#") == False:
        i1 =  i.split("#", 1)
        i11 = i1[0].split(":", 1)
        p[i11[0]] = i11[1]
        print(p)






f.close