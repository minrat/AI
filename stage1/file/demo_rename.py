import os
print(os.getcwd())
try:
    os.chdir("vipJr")
except OSError:
    os.mkdir("vipJr")
    os.chdir("vipJr")
# 获取当前目录位置
path = os.getcwd()
# 打印当前目录下内容
content = os.listdir(path)
# 打印文件的绝对路径
for file in content:
    file_path = path+"\\"+file
    print(file_path)
    # 变更文件名称
    dir_path = os.path.split(file_path)
    tmp_path = dir_path[1].split(".")
    # 执行变更
    os.rename(file_path, dir_path[0] + '\\' "new_" + tmp_path[0] + "." +tmp_path[1])
