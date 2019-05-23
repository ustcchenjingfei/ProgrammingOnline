#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-16 20:31 
@Email: 953209336@qq.com
"""

import tkinter as tk

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题

f = tk.Frame(win, height=200, width=200)
lab1 = tk.Label(f, text='中国科学技术大学')
x = 0


def foo():
    global x
    x = x + 10
    if x > 200:
        x = 0
    lab1.place(x=x, y=0)  # place放置精确位置
    f.after(500, foo)


f.pack()
f.after(500, foo)  # 隔500ms执行foo()函数刷新屏幕

win.mainloop()  # 进入消息循环，也就是显示窗口
