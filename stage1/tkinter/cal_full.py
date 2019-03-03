import tkinter  # 导入tkinter模块
import time

root = tkinter.Tk()
root.minsize(280, 500)
root.title('计算器')

# 显示输入和结果
result = tkinter.StringVar()
result.set(0)
# 显示式子
result2 = tkinter.StringVar()
result2.set('')
label = tkinter.Label(root, font=('微软雅黑', 20), bg='#EEE9E9', bd='9', fg='#828282', anchor='se', textvariable=result2)
label.place(width=280, height=170)
label2 = tkinter.Label(root, font=('微软雅黑', 30), bg='#EEE9E9', bd='9', fg='black', anchor='se', textvariable=result)
label2.place(y=170, width=280, height=60)

# 数字键按钮
btn7 = tkinter.Button(root, text='7', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('7'))
btn7.place(x=0, y=285, width=70, height=55)
btn8 = tkinter.Button(root, text='8', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('8'))
btn8.place(x=70, y=285, width=70, height=55)
btn9 = tkinter.Button(root, text='9', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('9'))
btn9.place(x=140, y=285, width=70, height=55)

btn4 = tkinter.Button(root, text='4', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('4'))
btn4.place(x=0, y=340, width=70, height=55)
btn5 = tkinter.Button(root, text='5', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('5'))
btn5.place(x=70, y=340, width=70, height=55)
btn6 = tkinter.Button(root, text='6', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('6'))
btn6.place(x=140, y=340, width=70, height=55)

btn1 = tkinter.Button(root, text='1', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('1'))
btn1.place(x=0, y=395, width=70, height=55)
btn2 = tkinter.Button(root, text='2', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('2'))
btn2.place(x=70, y=395, width=70, height=55)
btn3 = tkinter.Button(root, text='3', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('3'))
btn3.place(x=140, y=395, width=70, height=55)
btn0 = tkinter.Button(root, text='0', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('0'))
btn0.place(x=0, y=450, width=140, height=55)

# 运算符号按钮
btnac = tkinter.Button(root, text='C', bd=0.5, font=('微软雅黑', 20), fg='orange', command=lambda: pressCompute('AC'))
btnac.place(x=0, y=230, width=70, height=55)
btnneg = tkinter.Button(root, text='±', font=('微软雅黑', 20), fg='orange', bd=0.5, command=lambda: pressCompute('n'))
btnneg.place(x=70, y=230, width=70, height=55)
btnper = tkinter.Button(root, text='%', font=('微软雅黑', 20), fg='orange', bd=0.5, command=lambda: pressCompute('%'))
btnper.place(x=140, y=230, width=70, height=55)
btndivi = tkinter.Button(root, text='÷', font=('微软雅黑', 20), fg='orange', bd=0.5,
                         command=lambda: pressCompute('/'))
btndivi.place(x=210, y=230, width=70, height=55)
btnmul = tkinter.Button(root, text='×', font=('微软雅黑', 20), fg='orange', bd=0.5,
                        command=lambda: pressCompute('*'))
btnmul.place(x=210, y=285, width=70, height=55)
btnsub = tkinter.Button(root, text='-', font=('微软雅黑', 20), fg='orange', bd=0.5,
                        command=lambda: pressCompute('-'))
btnsub.place(x=210, y=340, width=70, height=55)
btnadd = tkinter.Button(root, text='+', font=('微软雅黑', 20), fg='orange', bd=0.5,
                        command=lambda: pressCompute('+'))
btnadd.place(x=210, y=395, width=70, height=55)
btnequ = tkinter.Button(root, text='=', font=('微软雅黑', 20), fg='orange', bd=0.5,
                        command=lambda: pressEqual())
btnequ.place(x=210, y=450, width=70, height=55)
btnpoint = tkinter.Button(root, text='.', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('.'))
btnpoint.place(x=140, y=450, width=70, height=55)

lists = []  # 设置一个变量，保存运算数字和符号的列表
isPressSign = False  # 是否按下运算符号
isPressEqual = False  # 是否按下等号


# 数字输入处理
def pressNum(num):
    global lists
    global isPressSign
    global isPressEqual

    if isPressEqual:
        result2.set('')
        result.set('0')
    if isPressSign:
        result.set(0)
        isPressSign = False

    oldnum = result.get()
    if num != '.':
        if oldnum == '0' or isPressEqual:  # 如过界面上数字为0，则获取按下的数字
            result.set(num)
            isPressEqual = False
        elif oldnum == '-0':
            result.set('-' + num)
        else:
            newnum = oldnum + num
            result.set(newnum)
    else:
        newnum = oldnum + num
        result.set(newnum)


# 运算函数
def pressCompute(sign):
    global lists
    global isPressSign
    global isPressEqual

    if isPressEqual:
        isPressEqual = False
    num = result.get()  # 获取界面数字
    if sign == 'n':  # 如果按下的是'±'
        if num[0] == '-':
            result.set(num[1:])
        else:
            result.set('-' + num)
        isPressSign = False
        return
    if isPressSign:
        try:
            lists[-1] = sign
        except IndexError:
            pass
        if sign == 'AC':
            result2.set('')
            lists.clear()
        else:
            result2.set(''.join(lists))
        result.set('0')
        isPressSign = False
        return
    if sign == '%':
        isPressSign = False
        num = str(float(num) / 100)
    lists.append(num)  # 保存界面获取的数字到列表中
    if sign != '%':
        lists.append(sign)  # 讲按下的运算符号保存到列表中
        isPressSign = True

    if sign == 'AC':  # 如果按下的是'AC'按键，则清空列表内容，讲屏幕上的数字键设置为默认数字0
        lists.clear()
        result.set(0)
    result2.set(''.join(lists))
    result.set('0')


# 获取运算结果函数
def pressEqual():
    global lists
    global isPressEqual

    if lists and lists[-1] == '%':
        pass
    else:
        curnum = result.get()
        lists.append(curnum)

    computrStr = ''.join(lists)  # 讲列表内容用join命令将字符串链接起来
    computrStr = computrStr.replace('%', '/100')
    try:
        endNum = eval(computrStr)  # 用eval命令运算字符串中的内容
        endNum = round(endNum, 6)
    except Exception:
        lists.clear()
        result.set('0')
        result2.set('Wrong formula')
    else:
        result.set(endNum)  # 讲运算结果显示到屏幕1
        result2.set(computrStr)  # 将运算过程显示到屏幕2
        lists.clear()  # 清空列表内容
    isPressEqual = True


root.mainloop()
