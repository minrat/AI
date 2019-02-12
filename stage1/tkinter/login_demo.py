from tkinter import *
from tkinter.messagebox import *

root = Tk()
# 设置标题
root.title("vipJr程序登录")
# 设置框体
root.geometry('600x400')
# 单元框架
frame_1 = Frame(root)
# 标签
label_1 = Label(frame_1, text="账号：").grid(row=0, column=0, columnspan=2)
label_2 = Label(frame_1, text="密码：").grid(row=1, column=0, columnspan=2)
# 对话框
entry_account = StringVar()
Entry(frame_1, textvariable=entry_account).grid(row=0, column=5, columnspan=4)
entry_password = StringVar()
Entry(frame_1, textvariable=entry_password, show="*").grid(row=1, column=5, columnspan=4)
# 复选框
Checkbutton(frame_1, text="记录密码", onvalue=1, offvalue=0, height=5, width=10).grid(row=3, column=2, columnspan=2)
Checkbutton(frame_1, text="自动登录", onvalue=1, offvalue=0, height=5, width=10).grid(row=3, column=6, columnspan=2)
# 登录方法
def login():
    print("Welcome Login")
    root.title("登录中，请稍后....")
    account = entry_account.get()
    password = entry_password.get()
    # 校验输入内容
    if account == "admin" and password == "123":
        print("登录成功")
        showinfo("成功", message="["+str(account)+"] 登录成功")
        root.title("登录成功")
    else:
        print("登录失败")
        showerror("失败", message="["+str(password)+"] 登录失败，请重试！")
        root.title(" 登录失败")


# 按钮
Button(frame_1, text="登录", command=login).grid(row=5, column=3, columnspan=2)
Button(frame_1, text="退出", command=root.quit).grid(row=5, column=6, columnspan=2)
# 组件打包
frame_1.pack(side=TOP, expand=YES)
root.mainloop()

