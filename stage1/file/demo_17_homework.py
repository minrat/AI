'''
1、指定新建目录文件夹，使用 try except 的方式完成目录的创建
2、在创建的文件夹下生成文件
3、向文件中增加内容
4、查看文件，内容是否成功写入
'''

import shutil
import os
print(os.getcwd())
try:
    os.chdir("vipJr")
except OSError:
    os.mkdir("vipJr")
    os.chdir("vipJr")
# 在vipJr 下面创建对应文件夹
dir_list = ['a', 'b', 'c', 'd']
for i in dir_list:
    os.mkdir(i)
# 执行文件夹移动
shutil.move("a", "b")
shutil.move("c", 'd')
# 执行文件生成
f = open("homework_17.py", "w+")
f.write("Homework 17 ")
f.close()
# 执行文件复制
shutil.copy2('homework_17.py', 'd/copy_homework_17.py')
# 查看文件
f = open("homework_17.py", "r")
content = f.read()
print(content)
f.close()
