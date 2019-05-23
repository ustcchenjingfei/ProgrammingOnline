#!usr/bin/env python
# -*-coding:utf-8-*-

"""
@Author: jingfei Chen
@Time: 2019-05-16 20:30 
@Email: 953209336@qq.com
"""

import tkinter as tk

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

win = tk.Tk()  # 创建一个窗口对象
win.title('我的第一个Windows窗口')  # 设置窗口标题

f = tk.Frame(win, height=200, width=200)
f.color = 0
f['bg'] = colors[f.color]  # 设置框架背景颜色
lab1 = tk.Label(f, text='0')
lab1.pack()


def foo():
    f.color = (f.color + 1) % (len(colors))
    lab1['bg'] = colors[f.color]
    lab1['text'] = str(int(lab1['text']) + 1)
    f.after(500, foo)  # 隔500ms执行foo()函数刷新屏幕


f.pack()

f.after(500, foo)  # 递归

win.mainloop()  # 进入消息循环，也就是显示窗口
