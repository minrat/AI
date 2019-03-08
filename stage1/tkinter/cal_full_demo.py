from tkinter import *
import os

class Calculator:
    def __init__(self):
        self.root = Tk()
        # 设置标题
        self.root.title("XP计算器")
        # 设置计算器窗体大小
        self.root.geometry("300x200")
        # 设置窗体不能改变大小
        self.root.resizable(width=False, height=False)
        # 设置图标
        self.root.iconbitmap(os.getcwd() + '/cal.ico')
        # 文本框参数化设置
        self.showInfo = StringVar()
        self.showInfo.set("")
        self.showResult = StringVar()
        self.showResult.set("0")

        # 框架单元
        fm1 = Frame(self.root)
        # 文本框只读设置（state="readonly"）
        Entry(fm1, textvariable=self.showInfo, state="readonly").grid(row=0, column=0, columnspan=4)
        Entry(fm1, textvariable=self.showResult, state="readonly").grid(row=1, column=0, columnspan=4)
        fm1.pack(side=TOP, expand=YES)
        fm2 = Frame(self.root)
        # 清除功能
        Button(fm2, text="C", bg='#EE6A50', width=4, command=lambda: self.click_clear()).grid(row=1, column=0)
        # 百分功能
        Button(fm2, text="%", width=4, command=lambda: self.click_percent()).grid(row=1, column=1)
        # 删除功能
        Button(fm2, text="←", bg='#EE6A50', width=4, command=lambda: self.click_delete()).grid(row=1, column=3)

        Button(fm2, text="/", width=4, command=lambda: self.click_button("/")).grid(row=1, column=2)
        Button(fm2, text="7", width=4, command=lambda: self.click_button("7")).grid(row=2, column=0)
        Button(fm2, text="8", width=4, command=lambda: self.click_button("8")).grid(row=2, column=1)
        Button(fm2, text="9", width=4, command=lambda: self.click_button("9")).grid(row=2, column=2)
        Button(fm2, text="＊", width=4, command=lambda: self.click_button("*")).grid(row=2, column=3)
        Button(fm2, text="4", width=4, command=lambda: self.click_button("4")).grid(row=3, column=0)
        Button(fm2, text="5", width=4, command=lambda: self.click_button("5")).grid(row=3, column=1)
        Button(fm2, text="6", width=4, command=lambda: self.click_button("6")).grid(row=3, column=2)
        Button(fm2, text="-", width=4, command=lambda: self.click_button("-")).grid(row=3, column=3)
        Button(fm2, text="1", width=4, command=lambda: self.click_button("1")).grid(row=4, column=0)
        Button(fm2, text="2", width=4, command=lambda: self.click_button("2")).grid(row=4, column=1)
        Button(fm2, text="3", width=4, command=lambda: self.click_button("3")).grid(row=4, column=2)
        Button(fm2, text="+", width=4, command=lambda: self.click_button("+")).grid(row=4, column=3)
        Button(fm2, text="0", width=4, command=lambda: self.click_button("0")).grid(row=5, column=0)
        Button(fm2, text=".", width=4, command=lambda: self.click_button(".")).grid(row=5, column=2)

        # 等号计算
        Button(fm2, text="=", bg='#BFEFFF', width=5, command=lambda: self.get_result()).grid(row=5, column=3)
        # 执行打包
        fm2.pack(side=BOTTOM)
        # 事件循环
        self.root.mainloop()

    # 清除
    def click_clear(self):
        print("执行清空操作")
        self.showResult.set("0")
        self.showInfo.set("")

    # 输入预先校验
    def pre_check(self):
        tmp = self.showResult.get()
        if tmp == 0 or tmp.startswith("0"):
            return ""
        else:
            return tmp

    # 百分比
    def click_percent(self):
        print("执行百分号操作")
        src = self.showInfo.get()
        tmp = self.pre_check()+"%"
        if tmp != 0:
            dest = tmp.replace("%", "/100")
            # 百分数计算
            target = str(eval(dest))
            # 百分比赋值
            self.showInfo.set(src+target)
            # 输入框置空
            self.showResult.set("0")

    # 删除
    def click_delete(self):
        # 信息校验
        if self.pre_check() != 0 and self.pre_check() != "":
            self.showInfo.set(self.showInfo.get()+self.pre_check())
            self.showResult.set("0")

        src = self.showInfo.get()
        self.showInfo.set(src[:-1])

    # 按键
    def click_button(self, value):
        if value == "+" or value == "-" or value == "*" or value == "/":
            # 已有的数据
            src = self.showInfo.get()
            # 新输入数据
            new = self.pre_check()
            # 重写记录框
            self.showInfo.set(src + new + value)
            # 置空输入框
            self.showResult.set("0")
        else:
            self.showResult.set(self.pre_check()+value)
            pass

    #  计算运算结果
    def get_result(self):
        src = self.showInfo.get()
        wait = self.pre_check()
        print("wait"+wait)
        if wait != "0" and wait != "":
            self.showInfo.set(src+wait)
            # 执行计算
            result = eval(src+wait)
            # 结果重新赋值
            self.showResult.set(result)
        else:
            # 去除符号，重新赋值
            self.showInfo.set(src[:-1])
            # 执行计算
            result = eval(src[:-1])
            # 结果重新赋值
            self.showResult.set(result)


if __name__ == '__main__':
    c = Calculator()
