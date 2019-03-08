from tkinter import *
class GUICal:
    def __init__(self):
        self.root = Tk()
        self.root.title("计算器")
        fm1 = Frame(self.root)
        Entry(fm1).grid(row=0, column=0, columnspan = 4)
        Entry(fm1).grid(row=1, column=0, columnspan=4)
        fm1.pack(side = TOP, expand = YES)
        fm2 = Frame(self.root)
        Button(fm2, text = "C",width=5).grid(row=1, column = 0, columnspan = 2)
        Button(fm2, text = "%").grid(row = 1, column = 2)
        Button(fm2, text = "/").grid(row = 1, column = 3)
        Button(fm2, text = "7").grid(row = 2, column = 0)
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


if __name__ == '__main__':
    c = GUICal()
