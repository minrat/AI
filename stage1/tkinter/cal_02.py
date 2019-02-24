from tkinter import *
class Cal:
    def __init__(self):
        # 加减乘除运算符号
        self.symbols = ["＋", "－", "＊", "/"]
        # 用来显示运算式子
        self.showText = ""
        # 用来显示运算结果
        self.showResult = ""

    # 清除功能
    def clear(self):
        self.showText = ""
        self.showResult = ""
        return [self.showText, self.showResult]

    # 保存功能
    def record(self, t):
        self.showText += t
        return self.showText

    # 设置百分比功能
    def percent(self):
        s = self.showText[::-1]
        if s[0] in self.symbols:
            return [self.showText, "错误"]
        self.showText += "%"
        for i in range(len(s)):
            if s[i] in self.symbols and self.isNum(s[i - 1]) == True:
                temp = s[i - 1::-1]
                temp = temp.replace("%", "/100")
                value = eval(temp) * 0.01
                temp2 = s[:i:-1]
                info = temp2 + s[i] + str(value)
                return [self.showText, str(eval(info))]
            else:
                num = self.showText[:len(self.showText) - 1]
                if self.isNum(num) == True:
                    return [self.showText, str(float(num) * 0.01)]
                else:
                    return [self.showText, "错误"]

    # 判断是否为数字
    def isNum(self, s):
        try:
           n = float(s)
           return True
        except ValueError:
           return False

class GUICal:
    def __init__(self, cal):
        self.root = Tk()
        # 设置标题
        self.root.title("计算器")
        # 设置计算器窗体大小
        self.root.geometry("300x200")
        self.cal = cal
        # 文本框参数化设置
        self.showInfo = StringVar()
        self.showInfo.set("0")
        self.showResult = StringVar()
        self.showResult.set("0")

        fm1 = Frame(self.root)
        Entry(fm1, textvariable=self.showInfo).grid(row=0, column=0, columnspan=4)
        Entry(fm1, textvariable=self.showResult).grid(row=1, column=0, columnspan=4)
        fm1.pack(side=TOP, expand=YES)
        fm2 = Frame(self.root)
        # 带真实清除功能
        Button(fm2, text="C", width=5, command=self.clearHandler).grid(row=1, column=0, columnspan=2)
        Button(fm2, text="%", command=self.cal.percent).grid(row=1, column=2)
        Button(fm2, text="/").grid(row=1, column=3)
        Button(fm2, text="7").grid(row=2, column=0)
        Button(fm2, text="8").grid(row=2, column=1)
        Button(fm2, text="9").grid(row=2, column=2)
        Button(fm2, text="X").grid(row=2, column=3)
        Button(fm2, text="4").grid(row=3, column=0)
        Button(fm2, text="5").grid(row=3, column=1)
        Button(fm2, text="6").grid(row=3, column=2)
        Button(fm2, text="-").grid(row=3, column=3)
        Button(fm2, text="1").grid(row=4, column=0)
        Button(fm2, text="2").grid(row=4, column=1)
        Button(fm2, text="3").grid(row=4, column=2)
        Button(fm2, text="+").grid(row=4, column=3)
        Button(fm2, text="0", width=5).grid(row=5, column=0, columnspan = 2)
        Button(fm2, text=".").grid(row=5, column=2)
        Button(fm2, text="=").grid(row=5, column=3)
        fm2.pack(side=BOTTOM)
        self.root.mainloop()

    def clearHandler(self):
        [info, value] = self.cal.clear()
        self.showInfo.set(info)
        self.showResult.set(value)


if __name__ == '__main__':
    cal = Cal()
    c = GUICal(cal)
