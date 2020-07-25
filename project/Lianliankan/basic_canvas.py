from tkinter import *

tk = Tk()
tk.title("连连看")
screen_w = tk.winfo_screenwidth()
screen_h = tk.winfo_screenheight()
size_w = 800
size_h = 600
size = "%dx%d+%d+%d" %(size_w, size_h, (screen_w-size_w)/2, (screen_h-size_h)/2)
tk.geometry(size)
tk.minsize(size_w, size_h)
tk.maxsize(size_w, size_h)

m1 = Menu(tk)
m2 = Menu(m1)


def start_game():
    print("游戏开始")
    # Here Need Add Some ...


def end_game():
    print("游戏结束")
    # Here Need Add Some ...

    # exit
    tk.quit()


m2.add_command(label="开始新游戏", command=start_game)
m2.add_command(label="退出游戏", command=end_game)
m2.add_separator()

m1.add_cascade(label="Game", menu=m2)
tk.configure(menu=m1)

# 画布
canvas = Canvas(tk, bg='pink', width=500, height=500)
canvas.pack(side=TOP, pady=5)

tk.mainloop()
